# Retail Demand Forecasting using Machine Learning

## Project Overview

Retail demand forecasting is essential for businesses to efficiently manage inventory, plan promotions, and reduce stockouts.
This project builds a **machine learning pipeline to predict daily retail store sales using historical data**.

The project implements a **complete ML workflow**, including data ingestion, feature engineering, model training, evaluation, and prediction.

---

## Problem Statement

Retail stores generate large amounts of historical sales data. Analyzing this data can help predict future demand and assist businesses in making better operational decisions.

This project aims to build a **machine learning model that forecasts retail sales based on historical store data and promotional activities**.

---

## Dataset Information

The dataset contains historical information about retail store sales.

Key features include:
* Store ID
* Date
* Day of Week
* Promotions
* School Holiday
* Customers
* Competition Distance
* Store Assortment

**Target Variable**
* `Sales

## Machine Learning Models Used

The following models were trained and evaluated:
* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

### Model Performance

| Model             | MAE     | RMSE    | R² Score |
| ----------------- | ------- | ------- | -------- |
| Linear Regression | 1024    | 1417    | 0.78     |
| Random Forest     | 727     | 1050    | 0.88     |
| XGBoost           | **667** | **943** | **0.90** |

**Best Performing Model:** XGBoost Regressor

## Project Pipeline

Data Ingestion
↓
Data Cleaning
↓
Feature Engineering
↓
Model Training
↓
Model Evaluation
↓
Prediction


## Project Structure

```
Retail-Demand-Forecasting
│
├── notebook
│   └── RDF.ipynb
│
├── src/mlProject
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── utils.py
│   └── logger.py
│
├── main.py
├── requirements.txt
└── README.md
```

