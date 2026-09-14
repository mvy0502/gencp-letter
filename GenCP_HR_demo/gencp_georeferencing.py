import argparse
import os
import glob
import rasterio
import rasterio.mask


def geoloc_generated_images(reference_path, generated_path, output_dir):
    """
    Georeference generated images based on real images metadata

    Args:
        reference_path (str): path to input reference (OSM geo-referenced raster)
        generated_path (str): path to generated image patch (not georeferenced)
        output_dir (str): path to output directory for georeferenced generated images: GenCP DB
    """

    filename = os.path.basename(reference_path)[:-4]

    with rasterio.open(generated_path) as src_test:
        test_img = src_test.read()

    test_img = test_img[:, :, :]

    out_image = f"{output_dir}/{filename}.tif"
    with rasterio.open(reference_path) as src:
        with rasterio.open(
            out_image,
            "w",
            driver="GTiff",
            count=3,
            height=test_img.shape[1],
            width=test_img.shape[2],
            dtype=test_img.dtype,
            crs=src.crs,
            transform=src.transform,
        ) as dst:
            dst.write(test_img)


def get_args():

    parser = argparse.ArgumentParser(description="Geo-Reference generated images")
    parser.add_argument(
        "--generated_dir",
        "-t",
        type=str,
        help="Path to directory containing generated image patches",
    )
    parser.add_argument(
        "--input_dir",
        "-i",
        type=str,
        help="Path to directory containing input OSM rasters",
    )
    parser.add_argument("--output_dir", "-o", type=str, help="Path to output directory")

    args = parser.parse_args()
    return args


def main():

    args = get_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for name in os.listdir(args.generated_dir):

        # Retrieve real image name
        if "fake" in name:
            ref_name = name[:-9] + ".tif"

            ref_path = os.path.join(args.input_dir, f"{ref_name}")
            if os.path.isfile(ref_path):
                geoloc_generated_images(
                    ref_path, os.path.join(args.generated_dir, name), args.output_dir
                )


if __name__ == "__main__":
    main()
