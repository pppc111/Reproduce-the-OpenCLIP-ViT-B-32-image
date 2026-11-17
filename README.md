# Project 1 : reproduce the final project's image encoder

# **Submission**

## Files

- `image_encoder.py`: completed NumPy implementation of the OpenCLIP ViT-B-32 image encoder.
- `helpers.py`: provided runtime dependency required by `image_encoder.py`.
- `project1_numpy.tex`: experiment report based on the supplied Shenzhen University template. Upload both to Overleaf and compile with XeLaTeX.
- `project1_numpy.pdf`: compiled report.
- `figs/`: all image assets used in the experiment report.
- `course_resources/`: stores course-provided resources, including weight files, image assets, `reference_outputs.npz` and so on.

Pretrained weight files are not included in this repository due to GitHub file size limits. Please download them from the course link provided.

## Run

Place `image_encoder.py` and `helpers.py` beside the course-provided `weights/`, `assets/`, `runtime.py`, and `check.py`, then run:

```powershell
python check.py --stage all
python run.py --output output_tokens.npz
```

## Numerical verification

The implementation was checked against `assets/reference_outputs.npz` using the provided independent checker.

| Stage         | Shape               | Maximum absolute error | Mean absolute error | Result |
| ------------- | ------------------- | ----------------------:| -------------------:| ------ |
| preprocess    | `(10, 3, 224, 224)` | `0.000e+00`            | `0.000e+00`         | PASS   |
| patches       | `(2, 49, 3072)`     | `0.000e+00`            | `0.000e+00`         | PASS   |
| input tokens  | `(2, 50, 768)`      | `7.153e-06`            | `2.597e-07`         | PASS   |
| block 0       | `(2, 50, 768)`      | `7.540e-06`            | `2.455e-07`         | PASS   |
| last tokens   | `(2, 50, 768)`      | `4.196e-05`            | `2.438e-06`         | PASS   |
| output tokens | `(10, 512)`         | `7.302e-07`            | `8.244e-08`         | PASS   |
| batch         | `(3, 512)`          | `4.992e-07`            | `7.769e-08`         | PASS   |

## Implementation note

All six required TODO groups are implemented: patch order, head split/merge, stored-weight transposition, both residual paths, CLS/position construction, final projection, and unit normalization agree with the independent reference. 


