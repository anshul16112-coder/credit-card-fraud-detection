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

🔧 Data Processing

The dataset was processed using techniques including:

Categorical feature encoding
Date/time feature extraction
Removing unnecessary columns
Feature preparation for Machine Learning
Train-test splitting

Date-related features were extracted from transaction and birth-date information, including:

Transaction year
Transaction month
Transaction day
Transaction hour
Birth year
Birth month
Birth day
🌐 Streamlit Application

A Streamlit interface was created to allow users to enter transaction information and receive a prediction.

The application returns:

✅ Genuine Transaction
🚨 Fraudulent Transaction
💾 Model Saving

The trained Decision Tree model was saved using Joblib:

joblib.dump(tree_model, "fraud_detection_model.pkl")
📁 Project Structure
credit-card-fraud-detection/
│
├── app.py
├── fraud_detection_model.pkl
├── requirements.txt
└── README.md
▶️ Run the Project Locally

Clone the repository:

git clone https://github.com/anshul16112-coder/credit-card-fraud-detection.git

Move into the project directory:

cd credit-card-fraud-detection

Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will open in your browser.

🔮 Future Improvements
Improve the prediction pipeline
Add automatic categorical encoding
Create more user-friendly dropdown inputs
Improve model performance
Add additional Machine Learning models
Add better fraud-risk visualization
Improve the Streamlit UI
👨‍💻 Author

Anshul Pal

B.Tech — Data Science
