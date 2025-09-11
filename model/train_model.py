import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset
df = pd.read_csv("dataset.csv")

# Print columns to confirm
print("Columns in dataset:", df.columns.tolist())

# Set target column
TARGET_COLUMN = "readmitted"

# Encode categorical variables automatically
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
if TARGET_COLUMN in categorical_cols:
    categorical_cols.remove(TARGET_COLUMN)

df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Split features & target
X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model in backend folder
backend_path = os.path.join("..", "backend")
os.makedirs(backend_path, exist_ok=True)
model_file = os.path.join(backend_path, "model.pkl")
joblib.dump(model, model_file)

print(f"✅ Model trained and saved as {model_file}")
