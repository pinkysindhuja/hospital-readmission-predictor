from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Save the training columns for alignment
trained_columns = model.feature_names_in_

@app.route("/")
def home():
    return "Hospital Readmission Predictor API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        df = pd.DataFrame([data])

        # Convert YES/NO strings to 1/0 automatically
        for col in df.columns:
            df[col] = df[col].replace({"YES": 1, "NO": 0})

        # Convert categorical columns to dummies
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

        # Add missing columns from training
        for col in trained_columns:
            if col not in df.columns:
                df[col] = 0

        # Keep columns in the same order as training
        df = df[trained_columns]

        # Make predictions
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[:, 1][0]

        return jsonify({
            "readmitted": int(prediction),
            "probability": float(probability)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run on localhost and accessible on your local network
    app.run(debug=True, host="0.0.0.0", port=5000)
