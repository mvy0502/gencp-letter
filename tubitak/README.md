# tubitak/

The research record behind the letter, at the paths the letter's data-availability
statement gives. The root [README](../README.md) explains the repository and how to verify a
number.

| path | what it holds |
|---|---|
| `docs/` | the record: registrations (`*-registration.md`, written before the runs they govern), results documents (`*-results.md`), `corrections-log.md`, `standing-practices.md`, `open-items.md`, and the audits of the record itself |
| `docs/evidence/` | the per-chip artifacts the reported numbers derive from, every file pinned by sha256 and byte size in `docs/evidence/MANIFEST.md`; `BACKUP.md` and `checkpoints_modal_MANIFEST.md` describe what is held outside the repository |
| `docs/gates/` | training-loss logs and run logs of the training runs |
| `scripts/` | the frozen analysis and figure scripts, the self-test gate and the pre-commit hook (`scripts/hooks/pre-commit`) |
| `configs/` | the matcher configuration the residuals were scored with |
| `gencp_core/`, `qgis_plugin/`, `sr/`, `tests/` | the internship delivery's plugin code, carried with the history; the delivery itself is at [`mvy0502/gencp-validation`](https://github.com/mvy0502/gencp-validation) |
| `modal/`, `kaggle/` | the training and scoring harnesses used on the two platforms |
