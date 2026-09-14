import numpy as np
import glob
import tifffile
import os
import argparse
from tensorflow.keras.models import load_model
from osgeo import gdal

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process VHR images and generate predictions.")
parser.add_argument("--model_path", type=str, required=True, help="Path to the trained model.")
parser.add_argument("--img_files", type=str, required=True, help="Glob pattern for input images.")
parser.add_argument("--masks_files", type=str, required=True, help="Glob pattern for mask images.")
parser.add_argument("--output_folder", type=str, required=True, help="Folder to save output predictions.")
args = parser.parse_args()

# Define paths for images and masks
img_files = glob.glob(args.img_files)
masks_files = glob.glob(args.masks_files)

# Initialize arrays for images and masks
test_images = np.zeros((len(img_files), 256, 256, 3))
test_masks = np.zeros((len(masks_files), 256, 256, 3))

# Load images
for indx, img_path in enumerate(img_files):
    img = tifffile.imread(img_path)
    img[img == -32768] = 0  # Replace invalid values with 0
    test_images[indx] = img[:, :, :3]

# Load masks
for indx, mask_path in enumerate(masks_files):
    mask = tifffile.imread(mask_path)
    mask[mask == -32768] = 0  # Replace invalid values with 0
    test_masks[indx] = mask[:, :, :3]

X_val = test_images
y_val = test_masks

# Load the trained model
model = load_model(args.model_path)

# Print model summary
print("\n=== Model Summary ===")
model.summary()

# Print training parameters if available
if model.optimizer is not None:
    if "epochs" in model.optimizer.get_config():
        print(f"Number of training epochs: {model.optimizer.get_config()['epochs']}")

# Normalize images to [0, 1] range
y_val_norm = (y_val - 127.5) / 127.5
y_val_norm = (y_val_norm + 1) / 2.0

X_val_norm = (X_val - 127.5) / 127.5
X_val_norm = (X_val_norm + 1) / 2.0

# Make predictions
preds = model.predict(y_val_norm)
preds = (preds + 1) / 2.0
preds_8bit = (preds * 255).astype(np.uint8)

# Define output folder
os.makedirs(args.output_folder, exist_ok=True)

# Save predictions as GeoTIFF
for idx, img_path in enumerate(img_files):
    src_ds = gdal.Open(img_path)
    geotransform = src_ds.GetGeoTransform()
    projection = src_ds.GetProjection()
    src_ds = None  # Close source dataset
    
    pred = preds_8bit[idx]
    base_name = os.path.basename(img_path)[:-4]
    output_file = os.path.join(args.output_folder, f"{base_name}_preds.tif")
    
    driver = gdal.GetDriverByName("GTiff")
    rows, cols = pred.shape[:2]
    out_ds = driver.Create(output_file, cols, rows, 3, gdal.GDT_Byte)
    out_ds.SetGeoTransform(geotransform)
    out_ds.SetProjection(projection)
    
    for band in range(3):  # Save each channel
        out_band = out_ds.GetRasterBand(band + 1)
        out_band.WriteArray(pred[:, :, band])
        out_band.FlushCache()
    
    out_ds = None  # Close output dataset

print("Prediction files have been saved as RGB GeoTIFFs!")
