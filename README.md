# 💳 Credit Card Fraud Detection

A Machine Learning project that predicts whether a credit card transaction is **fraudulent or genuine**.

The trained Machine Learning model is integrated with a **Streamlit web application** so users can enter transaction details and get a prediction.

## 🚀 Live Demo

The model is deployed using Streamlit Community Cloud.

## 📌 Project Overview

Credit card fraud is a major problem in digital payments. This project uses Machine Learning classification techniques to identify potentially fraudulent transactions.

### Project Workflow

Dataset
↓
Data Preprocessing
↓
Exploratory Data Analysis
↓
Feature Engineering
↓
Model Training
↓
Model Evaluation
↓
Model Saving
↓
Streamlit Application
↓
Deployment

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📊 Machine Learning Models

The following classification models were evaluated:

- Logistic Regression
- Decision Tree Classifier

The **Decision Tree Classifier** performed better for this dataset and was selected as the final model.

## 📈 Model Performance

### Decision Tree Classifier

| Metric | Score |
|---|---:|
| Precision | 0.8032 |
| Recall | 0.8382 |
| F1 Score | 0.8203 |

### Confusion Matrix

```text
[[368125    401]
 [   316   1637]]
