# 🚨 Credit Card Fraud Detection | End-to-End MLOps Project

<p align="center">
  <b>Production-Ready Fraud Detection System using XGBoost, FastAPI, MLflow, Docker, GitHub Actions, and Render</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue">
  <img src="https://img.shields.io/badge/FastAPI-API-green">
  <img src="https://img.shields.io/badge/XGBoost-ML-orange">
  <img src="https://img.shields.io/badge/MLflow-Experiment%20Tracking-blueviolet">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED">
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI/CD-black">
  <img src="https://img.shields.io/badge/Render-Deployed-success">
</p>

---

## 🌐 Live Application

**Application URL**

https://fraud-detection-mlops-3llr.onrender.com

---

# 📌 Project Overview

Credit card fraud causes billions of dollars in losses every year. Detecting fraudulent transactions quickly and accurately is a major challenge due to:

* Highly imbalanced datasets
* Evolving fraud patterns
* Large transaction volumes
* Need for real-time predictions

This project builds a complete Machine Learning and MLOps pipeline capable of predicting fraudulent credit card transactions through a production-ready web application.

---

# 🎯 Business Objective

Develop an intelligent fraud detection system that:

* Identifies suspicious transactions in real time
* Minimizes financial losses
* Reduces manual fraud investigation effort
* Provides scalable prediction services
* Demonstrates real-world MLOps practices

---

# 🛠️ Tech Stack

## Programming

* Python
* Pandas
* NumPy

## Machine Learning

* Scikit-Learn
* XGBoost
* Logistic Regression
* SMOTE

## Experiment Tracking

* MLflow
* Model Registry

## Backend

* FastAPI
* Pydantic

## Frontend

* HTML
* CSS

## MLOps & Deployment

* Docker
* GitHub
* GitHub Actions
* Render

---

# 📊 Dataset

Dataset contains anonymized credit card transactions with:

* Time
* Amount
* V1 – V28 PCA-transformed features
* Class (Target)

Target:

* 0 → Legitimate Transaction
* 1 → Fraudulent Transaction

---
## Current Application Input:

To generate predictions, users are required to provide:

- Time
- Amount
- V1 – V28 values

This design reflects the structure of the dataset and allows direct interaction with the trained model.

### Why This Limitation Exists?

Because the dataset only provides PCA-transformed features, it is not possible to build a realistic transaction entry interface that automatically derives V1–V28 from business information.

---

# 🔬 Machine Learning Experiments

- Model 1: Logistic Regression

- Model 2: Logistic Regression + SMOTE

- Model 3: XGBoost Baseline

- Model 4: Tuned XGBoost (Final Model)
---

# 🏆 Final Model:

### Production Model

**Tuned XGBoost Classifier**

Why selected?

* Highest ROC-AUC
* Best Precision
* Strong Recall
* Lowest False Positive Rate
* Excellent Fraud Detection Performance

---

# 📈 MLflow Experiment Tracking

Implemented MLflow for:

* Experiment Tracking
* Parameter Logging
* Metric Logging
* Model Artifact Storage
* Model Versioning
* Model Registry

Tracked Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Tracked Models:

* Logistic Regression
* Logistic Regression + SMOTE
* XGBoost Baseline
* Tuned XGBoost

---

# 🏗️ End-to-End MLOps Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                      DATA LAYER                              │
├──────────────────────────────────────────────────────────────┤
│ Credit Card Fraud Dataset                                    │
│ 284,807 Transactions                                         │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                DATA PROCESSING LAYER                         │
├──────────────────────────────────────────────────────────────┤
│ • Missing Value Analysis                                     │
│ • Feature Scaling                                            │
│ • Class Imbalance Analysis                                   │
│ • Train-Test Split                                           │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                 MODEL TRAINING LAYER                         │
├──────────────────────────────────────────────────────────────┤
│ • Logistic Regression                                        │
│ • Logistic Regression + SMOTE                                │
│ • XGBoost Baseline                                           │
│ • Tuned XGBoost (Best Model)                                 │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│               MLFLOW EXPERIMENT TRACKING                     │
├──────────────────────────────────────────────────────────────┤
│ • Parameter Logging                                          │
│ • Metric Logging                                             │
│ • Artifact Storage                                           │
│ • Model Comparison                                           │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                  MODEL REGISTRY                              │
├──────────────────────────────────────────────────────────────┤
│ FraudDetectionModel                                          │
│ Version 1 → Production                                       │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                  INFERENCE LAYER                             │
├──────────────────────────────────────────────────────────────┤
│ Tuned XGBoost Production Model                               │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                    FASTAPI SERVICE                           │
├──────────────────────────────────────────────────────────────┤
│ • Input Validation                                           │
│ • Feature Scaling                                            │
│ • Real-Time Prediction                                       │
│ • JSON Response                                              │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                    FRONTEND UI                               │
├──────────────────────────────────────────────────────────────┤
│ HTML + CSS + JavaScript                                      │
│ Risk Meter                                                   │
│ Fraud Probability Score                                      │
│ Transaction Analysis Dashboard                               │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                  DOCKER CONTAINER                            │
├──────────────────────────────────────────────────────────────┤
│ Containerized Deployment                                     │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                GITHUB ACTIONS CI/CD                          │
├──────────────────────────────────────────────────────────────┤
│ Code Push                                                    │
│      ↓                                                       │
│ Automated Build                                              │
│      ↓                                                       │
│ Continuous Integration                                       │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                 RENDER DEPLOYMENT                            │
├──────────────────────────────────────────────────────────────┤
│ Public Fraud Detection Application                           │
│ Live API + Web Interface                                     │
└──────────────────────────────────────────────────────────────┘
```

---

# 🚀 Features

### Machine Learning

✅ Data Preprocessing

✅ Feature Scaling

✅ SMOTE Balancing

✅ Model Training

✅ Model Evaluation

✅ Fraud Classification

---

### MLOps

✅ MLflow Tracking

✅ Model Registry

✅ Docker Containerization

✅ GitHub Version Control

✅ GitHub Actions Workflow

✅ Production Deployment

---

### Web Application

✅ Modern Responsive UI

✅ Real-Time Predictions

✅ Probability Score

✅ Risk Assessment

---

# 📂 Project Structure

```text
Fraud-Detection-MLOps/
│
├── .github/
│   └── workflows/
│
├── models/
│   ├── xgboost_fraud_model.pkl
│   ├── amount_scaler.pkl
│   └── time_scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── Credit_card_fraud_prediction.ipynb
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t fraud-api .
```

## Run Container

```bash
docker run -p 8000:8000 fraud-api
```

Open:

```text
http://localhost:8000
```

---

# ⚡ API Endpoint

## Predict Fraud

```http
POST /predict
```

### Input

```json
{
  "Time": 5000,
  "Amount": 150,
  "V1": 0.5,
  ...
  "V28": -0.2
}
```

### Output

```json
{
  "prediction": 1,
  "fraud_probability": 0.993
}
```

---

# 📊 Business Impact

* Faster fraud detection
* Reduced financial risk
* Automated transaction screening
* Improved operational efficiency
* Scalable prediction infrastructure
---

# 👨‍💻 Author

## Kashish Pundir

B.Tech – Computer Science Engineering (Data Science)

Interested in:

* Data Science
* Machine Learning
* MLOps
* Artificial Intelligence
* Production ML Systems

---

⭐ If you found this project useful, consider giving it a star!
