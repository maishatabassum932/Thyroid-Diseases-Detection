# Thyroid Disease Recurrence Prediction

This project aims to analyze and build predictive models for recurrence of **well-differentiated thyroid cancer** using clinicopathologic features. The dataset is sourced from the [Thyroid Disease Dataset](https://www.kaggle.com/datasets/jainaru/thyroid-disease-data) on Kaggle.

## 📁 Dataset Information

- Duration: Collected over 15 years
- Follow-up: Each patient tracked for at least 10 years
- Source: UCI Machine Learning Repository (hosted on Kaggle)

### 📊 Features

| Feature               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Age                  | Patient's age at diagnosis/treatment                                        |
| Gender               | Male or Female                                                              |
| Smoking              | Smoking status (Yes/No)                                                     |
| Hx Smoking           | Smoking history                                                             |
| Hx Radiotherapy      | Prior radiotherapy for any condition                                        |
| Thyroid Function     | Functional status of the thyroid gland                                      |
| Physical Examination | Results from thyroid physical examination                                   |
| Adenopathy           | Presence of lymph node enlargement                                          |
| Pathology            | Type of thyroid cancer (based on pathology)                                 |
| Focality             | Whether cancer is unifocal or multifocal                                    |
| Risk                 | Cancer risk category                                                        |
| T                    | Tumor classification (size and invasion)                                    |
| N                    | Lymph node involvement classification                                       |
| M                    | Distant metastasis classification                                           |
| Stage                | Combined stage (based on T, N, M)                                            |
| Response             | Response to treatment                                                       |
| Recurred             | Whether the cancer recurred after treatment (Target Variable)               |


#  Objective
I tried to use all the thing that I have learn through my MAchine learning course to build a machine learning model that can **predict the recurrence of thyroid cancer** based on historical clinicopathologic features.

# Tools and Technologies

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook / VS Code
- Random Forest
- XGBoost


## 🚀 Project Goals

- Data Visualization & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Selection
- Model Training ( Random Forest, XGBoost)
- Model Evaluation (Accuracy, ROC-AUC, etc.)
- Final Prediction and Interpretation

