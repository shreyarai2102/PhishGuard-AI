import os
import joblib
import pandas as pd

from feature_extractor import extract_features


# ============================================================
# PROJECT PATHS
# ============================================================

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


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(MODEL_PATH)

feature_columns = joblib.load(
    FEATURE_PATH
)


print("PhishGuard model loaded")
print("Model:", MODEL_PATH)
print("Number of features:", model.n_features_in_)
print("Classes:", model.classes_)


# ============================================================
# PREDICT URL
# ============================================================

def predict_url(url):

    # --------------------------------------------------------
    # 1. Extract features
    # --------------------------------------------------------

    features = extract_features(url)


    # --------------------------------------------------------
    # 2. Convert to DataFrame
    # --------------------------------------------------------

    X = pd.DataFrame([features])


    # --------------------------------------------------------
    # 3. Make sure feature order is EXACTLY the same
    # --------------------------------------------------------

    X = X.reindex(
        columns=feature_columns,
        fill_value=0
    )


    # --------------------------------------------------------
    # 4. Prediction
    # --------------------------------------------------------

    prediction = model.predict(X)[0]


    # --------------------------------------------------------
    # 5. Probabilities
    # --------------------------------------------------------

    probabilities = model.predict_proba(X)[0]


    # --------------------------------------------------------
    # 6. Get probability belonging to predicted class
    # --------------------------------------------------------

    predicted_class_index = list(
        model.classes_
    ).index(prediction)


    confidence = (
        probabilities[predicted_class_index]
        * 100
    )


    # ========================================================
    # IMPORTANT
    #
    # Your PhiUSIIL dataset uses:
    #
    # label 0 = PHISHING
    # label 1 = SAFE
    #
    # Therefore DO NOT use:
    #
    # prediction == 1 -> PHISHING
    #
    # ========================================================

    if prediction == 0:

        result = "PHISHING"

    else:

        result = "SAFE"


    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {
        "url": url,
        "prediction": result,
        "confidence": round(
            float(confidence),
            2
        )
    }