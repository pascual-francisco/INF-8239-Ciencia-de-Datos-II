# U02.LAB07 - Computer Vision: Fashion-MNIST Classification

## Overview

This laboratory explores image classification using the Fashion-MNIST
dataset. Two neural network architectures were evaluated:

- Dense Baseline Neural Network
- Convolutional Neural Network (CNN)

The objective was to compare predictive performance, model complexity,
computational cost, and efficiency under the same experimental
conditions while applying Green AI principles.

---

## Dataset

Fashion-MNIST contains grayscale clothing images divided into ten
categories.

Dataset characteristics:

- 70,000 images
- 28 × 28 pixels
- 10 classes
- 60,000 training images
- 10,000 testing images

Classes:

- T-shirt/top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle Boot

---

## Data Partitioning

The original Fashion-MNIST training set was divided into:

- Training set: 54,000 images
- Validation set: 6,000 images

The official test set contains:

- Test set: 10,000 images

All models were evaluated using the same data partition to ensure a fair
comparison.

---

## Project Structure

```text
cv_image_classification/
├── models/
│   └── best_cnn.keras
├── reports/
│   ├── cv_metrics.json
│   ├── confusion_cnn.png
│   └── cnn_errors.png
├── scripts/
│   ├── check_runtime.py
│   └── train_cv.py
├── src/
│   └── inf8239_u02_cv/
├── tests/
├── MODEL_CARD.md
├── README.md
├── pyproject.toml
├── requirements-colab.txt
└── uv.lock
```

---

## Installation

### Local CPU Environment

Install the base dependencies and the TensorFlow CPU extra:

```bash
uv sync --extra cpu
```

### Local GPU Environment

For a compatible WSL2 or Linux environment with an NVIDIA GPU already
configured:

```bash
uv sync --extra gpu
```

Do not reinstall CUDA without first diagnosing the existing environment.

### Runtime Verification

Verify the Python, operating system, TensorFlow version, and available
hardware:

```bash
uv run python scripts/check_runtime.py
```

---

## Training

Train the Dense Baseline and CNN using eight epochs:

```bash
uv run python scripts/train_cv.py --epochs 8
```

The script performs the following operations:

1. Downloads Fashion-MNIST through TensorFlow.
2. Normalizes and validates the images.
3. Creates the training, validation, and test partitions.
4. Trains the Dense Baseline.
5. Trains the CNN.
6. Measures inference time five times for each model.
7. Calculates the average inference latency and standard deviation.
8. Generates performance reports and visual artifacts.
9. Saves the best CNN model.

Expected generated artifacts:

```text
models/best_cnn.keras
reports/cv_metrics.json
reports/confusion_cnn.png
reports/cnn_errors.png
```

---

## Results

### Dense Baseline

- Macro F1-score: 0.864
- Trainable parameters: 50,890
- Training time: 11.00 seconds
- Mean inference time: 0.075 ms/image
- Inference standard deviation: 0.010 ms/image

### CNN

- Macro F1-score: 0.789
- Trainable parameters: 19,466
- Training time: 371.04 seconds
- Mean inference time: 0.299 ms/image
- Inference standard deviation: 0.111 ms/image

Small numerical differences may occur because of hardware conditions,
software versions, system load, and execution variability.

---

## Key Findings

- The Dense Baseline achieved the highest Macro F1-score.
- The Dense Baseline trained approximately 34 times faster than the CNN.
- The Dense Baseline produced approximately four times lower inference
  latency.
- The CNN contained fewer trainable parameters but required more
  computational time.
- The most difficult class for the CNN was Shirt.
- The most frequent visual confusion occurred between Coat and Pullover.
- The CNN did not provide a predictive improvement that justified its
  additional computational cost.

---

## Repeated Inference Benchmark

Inference time was measured five times for each model using the same
Fashion-MNIST test set.

### Dense Baseline

```text
Run 1: 0.061 ms/image
Run 2: 0.068 ms/image
Run 3: 0.089 ms/image
Run 4: 0.081 ms/image
Run 5: 0.076 ms/image
```

Summary:

- Mean: 0.075 ms/image
- Standard deviation: 0.010 ms/image

### CNN

```text
Run 1: 0.253 ms/image
Run 2: 0.248 ms/image
Run 3: 0.520 ms/image
Run 4: 0.236 ms/image
Run 5: 0.239 ms/image
```

Summary:

- Mean: 0.299 ms/image
- Standard deviation: 0.111 ms/image

Repeated measurements reduce the risk of drawing conclusions from a
single timing result and reveal execution variability.

---

## Green AI Perspective

Green AI encourages the evaluation of predictive performance together
with computational cost.

Model selection should consider:

- Predictive performance
- Number of parameters
- Training time
- Inference latency
- Hardware requirements
- Resource consumption
- Practical deployment constraints

Although CNNs are generally preferred for computer vision tasks, the
Dense Baseline achieved superior predictive performance and
computational efficiency in this experiment.

The additional computational cost of the CNN was not justified because
the CNN required more training and inference time while producing a
lower Macro F1-score.

This result applies only to the specific models, dataset partition, and
experimental configuration used in this laboratory. It does not imply
that dense neural networks are generally superior to CNNs.

---

## Visual Error Analysis

The file below contains selected CNN classification errors:

```text
reports/cnn_errors.png
```

Each image title uses the following notation:

```text
R = Real class
P = Predicted class
```

For example:

```text
R:4 P:2
```

means that the real class was Coat, but the CNN predicted Pullover.

The most frequent visual error occurred between Coat and Pullover.
Additional errors involved Shirt being classified as Coat or
T-shirt/top.

These categories share similar silhouettes and grayscale appearance,
making them difficult to distinguish at the 28 × 28 pixel resolution.

---

## Confusion Matrix

The CNN confusion matrix is stored at:

```text
reports/confusion_cnn.png
```

The confusion matrix supports the visual analysis by showing repeated
errors between visually similar categories, especially:

- Coat and Pullover
- Shirt and Coat
- Shirt and T-shirt/top
- Ankle Boot and Sneaker

---

## Contract Testing

Run the automated contract tests:

```bash
uv run pytest -q
```

The tests verify:

- Image shape
- Image normalization range
- Expected number of classes
- Model output dimensions
- Finite output probabilities
- Probability sums approximately equal to one

Successful execution confirms that the data pipeline and model outputs
satisfy the expected project requirements.

---

## Google Colab Execution

Install the Colab-specific dependencies:

```python
%pip install -r requirements-colab.txt
```

Fashion-MNIST is publicly available and is downloaded automatically by
TensorFlow when required.

Do not upload the `.venv` directory. Dependencies should be recreated
from the project configuration and requirements files.

---

## Model Card

The complete Model Card is available at:

```text
MODEL_CARD.md
```

The Model Card documents:

- Intended use
- Out-of-scope uses
- Dataset and partitions
- Preprocessing
- Global and class-level metrics
- Hardware and environment
- Limitations
- Risks
- Human oversight

---

## Reproducibility

This laboratory was designed to be reproducible from a clean
environment. A new user should be able to clone the repository, install
the required dependencies, execute the notebook cells in order, and
generate comparable outputs.

### Clone the Repository

```bash
git clone https://github.com/pascual-francisco/INF-8239-Ciencia-de-Datos-II.git
cd INF-8239-Ciencia-de-Datos-II/Unit_02_Natural_Language_Processing/cv_image_classification
```

### Prepare the Environment

For the CPU route:

```bash
uv sync --extra cpu
```

For a compatible GPU environment:

```bash
uv sync --extra gpu
```

Verify the runtime:

```bash
uv run python scripts/check_runtime.py
```

### Notebook Execution Order

To reproduce the complete laboratory, execute every notebook cell
sequentially from the first cell to the last cell without skipping
steps.

Recommended execution order:

1. Configure and verify the execution environment.
2. Install the required dependencies.
3. Download and validate Fashion-MNIST.
4. Train the Dense Baseline and CNN.
5. Interpret training and validation behavior.
6. Compare predictive performance.
7. Compare model complexity.
8. Repeat inference measurements.
9. Evaluate the models from a Green AI perspective.
10. Inspect the confusion matrix and visual errors.
11. Execute the contract tests.
12. Generate the Model Card.
13. Generate the README documentation.

Running cells out of order may cause:

- Missing variables
- Missing generated files
- Incorrect paths
- Dependency errors
- Incomplete evaluation results

### Reproduce the Training Experiment

Execute:

```bash
uv run python scripts/train_cv.py --epochs 8
```

### Reproduce the Contract Tests

Execute:

```bash
uv run pytest -q
```

### Expected Artifacts

Verify that the following files are generated:

```text
models/best_cnn.keras
reports/cv_metrics.json
reports/confusion_cnn.png
reports/cnn_errors.png
MODEL_CARD.md
README.md
```

### Expected Results

Approximate experimental results:

```text
Dense Macro F1: 0.864
CNN Macro F1:   0.789
```

Exact timing values may vary depending on:

- CPU or GPU availability
- TensorFlow version
- Operating system
- Background system load
- Runtime configuration
- Hardware performance

### Reproducibility Checklist

Before considering the practice successfully reproduced, verify that:

- The repository was cloned successfully.
- The correct project directory was selected.
- Dependencies were installed without errors.
- TensorFlow detected the intended runtime.
- All notebook cells were executed in order.
- Both models completed training.
- Inference was measured five times for each model.
- `cv_metrics.json` was generated.
- `confusion_cnn.png` was generated.
- `cnn_errors.png` was generated.
- `best_cnn.keras` was generated.
- Contract tests passed.
- `MODEL_CARD.md` was created.
- `README.md` was created.

---

## Limitations

Fashion-MNIST is a simplified educational benchmark composed of
low-resolution grayscale images.

Good performance on this dataset does not demonstrate that a model is
ready for:

- Medical image analysis
- OCR applications
- Industrial inspection
- Surveillance systems
- Safety-critical environments
- Other real-world computer vision domains

Additional domain-specific data, validation, risk analysis, and human
oversight would be required before considering deployment in another
application.

---

## Conclusion

The Dense Baseline provided the best balance between predictive
performance and computational efficiency in this experiment.

The CNN required substantially more training and inference time while
obtaining a lower Macro F1-score. Therefore, the additional
computational cost of the CNN was not justified under the experimental
conditions used in this laboratory.

The main lesson is that model selection should be based on a fair
comparison of performance, computational cost, latency, limitations,
and deployment requirements rather than architecture complexity alone.
