import joblib
import pandas as pd

from feature_extractor import extract_features

# Load model and feature order
model = joblib.load("../models/phishguard_model.pkl")
feature_columns = joblib.load("../models/feature_columns.pkl")


def predict_url(url):
    # Extract features
    features = extract_features(url)

    # Convert to DataFrame
    X = pd.DataFrame([features])

    # Ensure correct column order
    X = X[feature_columns]

    # Prediction
    prediction = model.predict(X)[0]

    # Confidence
    confidence = model.predict_proba(X)[0].max() * 100

    return {
        "url": url,
        "prediction": "PHISHING" if prediction == 1 else "SAFE",
        "confidence": round(float(confidence), 2)
    }
