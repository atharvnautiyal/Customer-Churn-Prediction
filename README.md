# Customer-Churn-Prediction

Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to churn (leave the service) based on demographic and service usage features.

The project demonstrates a basic end-to-end machine learning workflow including data preprocessing, model training, evaluation, and deployment using a simple web interface built with Streamlit.

Tech Stack

Python
Pandas
Scikit-learn
Matplotlib
Streamlit
Joblib

```
Project Structure
customer-churn-project
│
├── app
│   └── app.py
│
├── data
│   └── churn.csv
│
├── images
│   └── image.png
│
├── models
│   ├── accuracy.pkl
│   └── model.pkl
│
├── notebooks
│   └── churn_analysis.ipynb
│
├── requirements.txt
|
└── README.md
```

Dataset

The project uses the Telco Customer Churn Dataset.
The dataset contains information about telecom customers including:

Senior Citizen status
Partner
Dependents
Tenure
Internet service
Online security
Contract type
Payment method
Monthly charges
Total charges
Target variable:
Churn

1 → Customer will churn
0 → Customer will stay

Model
Model used: Decision Tree
Preprocessing steps:
Removed unnecessary identifier column (customerID)
Converted TotalCharges to numeric
Handled missing values
Encoded categorical variables using Label Encoding
Train/test split (80/20)
Model accuracy: ~78–82% (depending on split)

Running the Project

Clone the repository
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git

Install dependencies
pip install -r requirements.txt

Train the model
Run the notebook:
notebooks/churn_analysis.ipynb

This will generate:
models/model.pkl

Run the Streamlit app

streamlit run app/app.py
Application Preview
images/image.png

The Streamlit interface allows users to input customer details and receive a churn prediction instantly.

Possible Improvements

Compare multiple models (Logistic Regression, Random Forest)
Perform feature importance analysis
Deploy the Streamlit application online
Add more evaluation metrics
