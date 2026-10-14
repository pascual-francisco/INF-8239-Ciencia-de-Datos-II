# U03.E06 - Autoencoders and Variational Autoencoders

**Course:** INF-8239 Data Science II  
**Unit:** 03 - Generative Algorithms and Features  
**Student:** Francisco Pascual

---

# Project Overview

This project explores representation learning and generative modeling through the implementation of an Autoencoder (AE) and a Variational Autoencoder (VAE) using the Fashion-MNIST dataset.

The objective is to compare deterministic and probabilistic latent representations, evaluate reconstruction quality, generate new synthetic images, analyze latent-space interpolation, and assess the tradeoff between reconstruction fidelity and generative capabilities.

Implemented components:

- Autoencoder (AE)
- Variational Autoencoder (VAE)
- Random latent-space sampling
- Latent-space interpolation
- Generated sample analysis
- Nearest-neighbor comparison
- Streamlit inference application
- Model Card and AI Use Declaration

---

# Project Structure

```text
U03.E06/
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   ├── autoencoder.keras
│   └── decoder.keras
│
├── reports/
│   ├── ae_vae_panel.png
│   ├── interpolation.png
│   └── training_metrics.json
│
├── scripts/
│   └── train_ae_vae.py
│
├── src/
│   └── inf8239_u03_gen/
│       ├── __init__.py
│       ├── data.py
│       └── models.py
│
├── tests/
│   ├── test_data.py
│   └── test_models.py
│
├── notebooks/
│   └── U03_E06_Autoencoders_VAE.ipynb
│
├── MODEL_CARD.md
├── AI_USE_DECLARATION.md
├── README.md
├── requirements.txt
└── uv.lock
```

## Directory Description

### app/

Contains the Streamlit application used to generate images from the trained decoder.

### models/

Stores trained model artifacts used during inference.

### reports/

Contains generated figures, evaluation panels and training metrics.

### scripts/

Contains executable training scripts used to train and evaluate the models.

### src/

Contains reusable project source code, including dataset utilities and model architectures.

### tests/

Contains automated unit tests used to verify data preprocessing and model construction.

### notebooks/

Contains the executed notebook documenting the complete workflow and results.

### Documentation Files

- **README.md**: Project overview and results.
- **MODEL_CARD.md**: Model description, limitations and intended use.
- **AI_USE_DECLARATION.md**: Disclosure of AI-assisted development.
- **requirements.txt / uv.lock**: Dependency management and reproducibility.

---

# Generated Artifacts

The following artifacts are produced during execution:

- reports/ae_vae_panel.png
- reports/interpolation.png
- reports/training_metrics.json
- models/autoencoder.keras
- models/decoder.keras

---

# Learning Objectives

The objective of this exercise is to understand:

- How Autoencoders compress image information.
- How Variational Autoencoders learn probabilistic latent representations.
- The difference between reconstruction and generation.
- The role of latent spaces in representation learning.
- The purpose of KL divergence.
- Latent-space interpolation.
- Generative AI evaluation concepts.
- Diversity, fidelity and memorization risks.
- Responsible deployment of generative models.

---

# Dataset

## Fashion-MNIST

Fashion-MNIST is a collection of grayscale images representing clothing items and accessories.

### Dataset Characteristics

| Metric | Value |
|----------|----------:|
| Training Images | 60,000 |
| Test Images | 10,000 |
| Resolution | 28 × 28 |
| Channels | 1 |
| Classes | 10 |

The images were normalized to the range:

```text
[0,1]
```

before training.

---

# Autoencoder (AE)

## Purpose

The Autoencoder learns a compressed representation of an image and attempts to reconstruct it as accurately as possible.

Conceptual workflow:

```text
Input Image
      ↓
Encoder
      ↓
Latent Representation
      ↓
Decoder
      ↓
Reconstructed Image
```

The objective is to minimize reconstruction error while preserving relevant visual information.

---

# Variational Autoencoder (VAE)

## Purpose

The Variational Autoencoder extends the Autoencoder by learning probability distributions in latent space rather than fixed latent vectors.

The encoder predicts:

```text
Mean (μ)
Log Variance (log σ²)
```

A latent vector is sampled and passed to the decoder to generate an image.

Conceptual workflow:

```text
Input Image
      ↓
Encoder
      ↓
μ , σ²
      ↓
Sampling
      ↓
Latent Vector
      ↓
Decoder
      ↓
Generated Image
```

---

# VAE Loss Function

The Variational Autoencoder minimizes two objectives simultaneously.

## Reconstruction Loss

Measures how closely reconstructed images match the original images.

Question:

> How much visual information was preserved?

## KL Divergence

Measures how closely the latent representation follows a normal distribution.

Question:

> Is the latent space structured and suitable for generation?

Total loss:

```text
Total Loss =
Reconstruction Loss +
KL Divergence
```

---

# Training Results

## Autoencoder

### Training History

| Epoch | Train Loss | Validation Loss |
|---------|---------:|---------:|
| 1 | 0.4529 | 0.3698 |
| 2 | 0.3458 | 0.3364 |
| 3 | 0.3270 | 0.3244 |
| 4 | 0.3175 | 0.3172 |
| 5 | 0.3116 | 0.3122 |
| 6 | 0.3073 | 0.3084 |

### Interpretation

The Autoencoder consistently reduced both training and validation loss.

The convergence pattern suggests successful learning without evidence of significant overfitting.

The reconstructed images preserved most structural features of the garments while maintaining relatively sharp contours.

---

## Variational Autoencoder

### Training History

| Epoch | Total Loss | Reconstruction | KL |
|---------|---------:|---------:|---------:|
| 1 | 304.94 | 297.33 | 7.61 |
| 2 | 293.10 | 286.35 | 6.76 |
| 3 | 289.90 | 283.22 | 6.69 |
| 4 | 287.92 | 281.54 | 6.38 |
| 5 | 286.16 | 279.76 | 6.39 |
| 6 | 285.08 | 278.84 | 6.24 |
| 7 | 283.83 | 277.51 | 6.32 |
| 8 | 283.04 | 276.87 | 6.17 |

### Interpretation

The reconstruction loss decreased throughout training while the KL divergence stabilized around six units.

This behavior indicates that the model successfully balanced reconstruction quality and latent-space regularization.

---

# Evaluation with Unselected Panels

To avoid selection bias, a fixed random seed (`SEED = 42`) was used to randomly select sixteen test examples.

The evaluation panel included:

- Original images.
- Autoencoder reconstructions.
- Variational Autoencoder reconstructions.
- Newly generated samples.

No examples were manually selected.

---

# Reconstruction Analysis

## Autoencoder

Observed characteristics:

- Sharper reconstructions.
- Better preservation of visual details.
- More faithful contours.
- Lower reconstruction error.

### Interpretation

The Autoencoder focused entirely on reconstruction fidelity and therefore preserved image quality more effectively.

---

## Variational Autoencoder

Observed characteristics:

- Smoother reconstructions.
- Slightly blurred edges.
- Reduced detail.
- Better organized latent representation.

### Interpretation

The VAE sacrificed part of the reconstruction quality in exchange for generation capabilities and a structured latent space.

---

# Generated Samples

New images were generated from randomly sampled latent vectors.

Observed characteristics:

- Multiple clothing categories appeared.
- Samples were visually distinct.
- No obvious mode collapse was observed.
- Generated images remained consistent with Fashion-MNIST patterns.

### Interpretation

The decoder learned reusable visual concepts that allowed the creation of plausible synthetic clothing images.

---

# Diversity Analysis

Evidence of diversity included:

- Different silhouettes.
- Different garment categories.
- Variation in contours.
- Variation in texture and shapes.

Generated samples did not appear identical and showed meaningful variability.

---

# Latent Space Interpolation

Interpolation was performed between two latent-space points.

Visual observations:

- Smooth transitions between images.
- Progressive transformation of shapes.
- No abrupt jumps during interpolation.

The effect resembled a garment being gradually drawn or transformed from one form into another.

### Interpretation

The interpolation experiment suggests that the VAE learned a continuous latent space where nearby points correspond to visually similar representations.

---

# Nearest Neighbor Comparison

Generated samples were compared against the closest training images using Euclidean distance.

Observations:

- Generated images resembled real Fashion-MNIST samples.
- No exact copies were observed.
- Generated samples appeared to combine learned visual patterns rather than memorizing single examples.

### Interpretation

The results suggest that the model learned general visual representations instead of directly reproducing training examples.

---

# Computational Cost

| Metric | Result |
|----------|----------:|
| AE Training Time | 15.56 s |
| VAE Training Time | 31.82 s |
| AE Parameters | 25,888 |
| Decoder Parameters | 101,520 |

### Interpretation

The Variational Autoencoder required approximately twice the training time of the Autoencoder because of probabilistic sampling and KL divergence computation.

---

# Risks and Limitations

## Visual Ambiguity

Certain Fashion-MNIST classes share similar visual features.

Examples:

- T-shirt/Top vs Shirt
- Pullover vs Coat
- Sneaker vs Ankle Boot

---

## Reconstruction Quality

The VAE produces smoother outputs that may lose fine details.

---

## Memorization Risk

Although nearest-neighbor analysis did not reveal exact copies, visual inspection alone cannot completely eliminate memorization concerns.

---

## Dataset Limitations

Generated outputs can only reflect patterns learned from Fashion-MNIST and do not generalize beyond the information contained in the training dataset.

---

# Local Application and Cloud Readiness

A Streamlit application was developed to demonstrate inference using the trained decoder.

Characteristics:

- Loads `models/decoder.keras`.
- Performs inference only.
- Does not retrain models.
- Supports local execution.
- Suitable for cloud deployment with limited resources.

The training process is separated from deployment, allowing the application to operate efficiently without requiring model retraining.

---

# Automated Testing

Quality verification was performed using automated tests.

Results:

```text
4 passed in 9.07s
```

The project includes:

- Source code.
- Automated tests.
- Model Card.
- AI Use Declaration.
- Generated reports.
- Saved models.

---

# Final Conclusions

This project demonstrated the progression from deterministic reconstruction models to probabilistic generative models.

Key findings:

- Autoencoders achieved superior reconstruction quality.
- Variational Autoencoders learned structured latent spaces.
- Generated samples exhibited reasonable diversity.
- Latent-space interpolation demonstrated continuity of the learned representation.
- No obvious evidence of direct memorization was observed.
- The VAE sacrificed reconstruction fidelity in exchange for generative capabilities.

Overall, the Autoencoder is better suited for reconstruction tasks, while the Variational Autoencoder is more appropriate for generative applications, latent-space exploration, interpolation, and synthetic image generation.
