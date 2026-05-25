# Customer Churn Prediction using Machine Learning

## Project Overview

This project focuses on predicting customer churn in the telecommunications industry using Machine Learning techniques.

Customer churn prediction helps businesses identify customers who are likely to discontinue their services, allowing companies to take proactive retention measures.

---

## Problem Statement

Customer retention is one of the biggest challenges in the telecom industry. Acquiring new customers is significantly more expensive than retaining existing ones.

The goal of this project is to analyse customer behaviour and build predictive models capable of identifying potential churn customers.

---

## Dataset Information

- Dataset: Telco Customer Churn Dataset
- Source: Kaggle
- Rows: 7043
- Columns: 21

Dataset Link:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

## Exploratory Data Analysis

The EDA process included:

- Missing value analysis
- Customer churn distribution
- Monthly charges analysis
- Tenure analysis
- Correlation analysis
- Contract type behaviour

---

## Machine Learning Models

The following models were implemented:

1. Logistic Regression
2. Random Forest Classifier

---

## Evaluation Metrics

- Accuracy Score
- Classification Report
- ROC-AUC Score
- Confusion Matrix

---

## Key Insights

- Customers with month-to-month contracts are more likely to churn.
- High monthly charges increase churn probability.
- Long-term customers are less likely to leave.

---

## Project Structure

```bash
customer-churn-prediction/
│
├── customer_churn_prediction.ipynb
├── report.pdf
├── requirements.txt
├── app.py
└── dataset.csv
```

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## Future Improvements

- Hyperparameter tuning
- XGBoost implementation
- Deployment using Flask/FastAPI
- SHAP explainability
- Real-time API integration

---

## Author

Nidhi Yadav
