import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
data = pd.read_csv('hospital_readmissions.csv')

# Basic preprocessing
# Drop columns if needed, handle missing values
data = data.fillna('Missing')

# Encode categorical columns using Label Encoding for simplicity
categorical_cols = ['age', 'medical_specialty', 'diag_1', 'diag_2', 'diag_3',
                    'glucose_test', 'A1Ctest', 'change', 'diabetes_med']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col].astype(str))

# Define features and target
X = data.drop('readmitted', axis=1)
y = data['readmitted'].apply(lambda x: 1 if x == 'yes' else 0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost classifier
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'hospital_readmission_model.pkl')
print("Model saved as hospital_readmission_model.pkl")
