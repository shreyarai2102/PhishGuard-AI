import os
import joblib
import pandas as pd

from feature_extractor import extract_features


# Project root
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "phishguard_model.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "models",
    "feature_columns.pkl"
)


# Load model
model = joblib.load(MODEL_PATH)

# Load feature order
feature_columns = joblib.load(FEATURE_PATH)


def predict_url(url):

    # Extract features
    features = extract_features(url)

    # Convert to DataFrame
    X = pd.DataFrame(
        [features]
    )

    # Ensure same feature order
    X = X.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(X)[0]

    # Probability
    probabilities = model.predict_proba(X)[0]

    confidence = probabilities[
        list(model.classes_).index(prediction)
    ] * 100

    return {
        "url": url,
        "prediction": (
            "PHISHING"
            if prediction == 0
            else "SAFE"
        ),
        "confidence": round(
            float(confidence),
            2
        )
    }