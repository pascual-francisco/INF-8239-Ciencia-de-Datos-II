
# U03.E05 - Recommender Systems

**Course:** INF-8239 Data Science II  
**Unit:** 03 - Generative Algorithms and Features  
**Student:** Francisco Pascual

---

# Project Overview

This project explores multiple recommendation strategies using the MovieLens dataset.

The work progresses from simple recommendation approaches to more advanced collaborative and hybrid recommender systems.

Implemented approaches:

1. Popularity-based recommendation
2. Content-based recommendation
3. Collaborative filtering with matrix factorization
4. Hybrid recommendation system

The project evaluates not only predictive accuracy but also ranking quality, catalog coverage, cold start behavior, and computational cost.

---

# Learning Objectives

The objective of this exercise is to understand:

- How recommendation systems operate.
- The difference between content-based and collaborative recommendation.
- Matrix factorization and latent factors.
- Offline evaluation procedures.
- Temporal train/test splitting.
- Ranking metrics.
- Cold start problems.
- Green AI tradeoffs between utility and computational cost.

---

# Dataset

## MovieLens Latest Small

MovieLens contains user interactions with movies through explicit ratings.

### Dataset Characteristics

| Metric | Value |
|----------|----------|
| Users | 610 |
| Movies | 9,742 |
| Ratings | 100,836 |
| Density | 0.01697 |

---

# LAB08 - Popularity and Content-Based Recommendation

## Popularity Baseline

The popularity baseline recommends items using:

- Average rating
- Rating count
- Bayesian smoothing

### Purpose

Provide a recommendation strategy even when user information is unavailable.

### Advantages

- Very simple.
- Easy to explain.
- Effective for cold-start situations.

### Limitations

- Not personalized.
- Popularity bias.

---

## Content-Based Recommendation

### Features Used

- Movie genres
- TF-IDF encoding
- Cosine similarity

### Workflow

Movie
→ Genres
→ TF-IDF
→ Cosine Similarity
→ Similar Movies

### Example

Toy Story

Generated recommendations:

- Toy Story 2
- Monsters Inc.
- Antz
- Turbo

### Conclusions

The model successfully identified similar movies based on genre information.

However:

- User preferences were ignored.
- Recommendations became highly specialized.
- No personalization was performed.

---

# LAB09 - Matrix Factorization and Hybrid Recommendation

## Collaborative Filtering

Collaborative filtering was implemented using matrix factorization.

The idea is to learn latent representations of:

- Users
- Movies

using historical ratings.

### Conceptual Workflow

User Ratings
→ Matrix Factorization
→ User Latent Vectors
→ Movie Latent Vectors
→ Rating Prediction
→ Recommendation Ranking

---

## Understanding Latent Factors

The algorithm learns a vector for each user and movie.

Example:

User 414

[0.82, 0.14, 0.73, ...]

Movie

[0.79, 0.11, 0.69, ...]

The interaction between both vectors is used to predict future ratings.

---

# Temporal Split

A temporal split was applied to avoid information leakage.

For each eligible user:

- Historical interactions were used for training.
- The most recent interaction was reserved for testing.

This simulates a realistic recommendation environment where only past data is available when making future recommendations.

---

# Evaluation Metrics

## RMSE

Measures rating prediction error.

Lower values indicate better approximation of observed ratings.

---

## HitRate@10

Measures whether the held-out item appears in the Top-10 recommendations.

Higher values indicate better ranking quality.

---

## Catalog Coverage

Measures how much of the movie catalog appears in recommendations.

Higher values indicate greater diversity.

---

# Hybrid Recommender

The hybrid system combines:

## Collaborative Component

Generated through matrix factorization.

## Content Component

Generated through:

- Genres
- TF-IDF
- Cosine similarity

### Hybrid Score

Hybrid Score =
α × Collaborative Score +
(1 − α) × Content Score

---

# Alpha Comparison

## Alpha = 0.25

Content-dominated configuration.

Results:

- RMSE: 1.0264
- HitRate@10: 0.0324
- Coverage: 0.1065

---

## Alpha = 0.75

Collaborative-dominated configuration.

Results:

- RMSE: 1.0264
- HitRate@10: 0.0375
- Coverage: 0.0775

---

## Selected Configuration

Alpha = 0.75

Reason:

The collaborative signal achieved the highest HitRate@10 while maintaining a similar computational cost.

---

# User Profile Evaluation

## Large History User

User ID: 414

Ratings:

2698

Characteristics:

- Strong collaborative signal.
- Stable latent representation.
- Highly personalized recommendations.

---

## Small History User

User ID: 406

Ratings:

20

Characteristics:

- Limited collaborative information.
- More dependence on content information.
- Less stable recommendations.

---

## New User

Characteristics:

- No ratings available.
- No collaborative representation can be built.

Fallback strategy:

- Rating average
- Rating count
- Popularity ranking

Recommendations are not personalized.

---

# Utility vs Cost Analysis

## Configuration A

- Factors: 10
- Epochs: 8
- RMSE: 1.0820
- HitRate@10: 0.0290
- Coverage: 0.0861
- Training Time: 9.25 s

## Configuration B

- Factors: 20
- Epochs: 12
- RMSE: 1.0264
- HitRate@10: 0.0375
- Coverage: 0.0775
- Training Time: 14.16 s

## Configuration C

- Factors: 40
- Epochs: 20
- RMSE: 1.0037
- HitRate@10: 0.0307
- Coverage: 0.1013
- Training Time: 22.45 s

---

# Pareto Analysis

Configuration A was dominated due to lower utility.

Configurations B and C remained on the Pareto frontier.

### Configuration B

Prioritizes:

- Better ranking quality.
- Lower computational cost.

### Configuration C

Prioritizes:

- Lower RMSE.
- Higher coverage.

---

# Green AI Perspective

The largest model was not automatically selected.

Although Configuration C achieved the lowest RMSE, it required:

- More factors
- More epochs
- More training time

while producing a lower HitRate@10 than Configuration B.

Therefore, Configuration B provided the best balance between utility and computational cost.

---

# Risks

## Popularity Bias

Popular items may dominate recommendations.

### Mitigation

Diversification strategies.

---

## Filter Bubble

Users may repeatedly receive similar content.

### Mitigation

Increase recommendation diversity.

---

## Selection Bias

Only observed interactions are available.

### Mitigation

Incorporate implicit feedback.

---

## Lack of Demographic Information

Population-level conclusions cannot be made.

### Mitigation

Include demographic attributes when available.

---

## Feedback Loops

Recommendations influence future training data.

### Mitigation

Continuous monitoring and periodic retraining.

---

# Final Conclusions

This project demonstrated the evolution of recommendation systems from popularity-based methods to hybrid recommendation architectures.

Key findings:

- Content-based recommendation identifies similar items.
- Collaborative filtering learns user preferences.
- Good rating prediction does not automatically imply good ranking quality.
- Hybrid recommenders balance multiple information sources.
- Larger models do not necessarily provide better practical performance.
- Green AI principles are useful when selecting recommendation models.

The final selected model was:

- 20 latent factors
- 12 training epochs
- Alpha = 0.75

because it achieved the best balance between recommendation quality and computational efficiency.
