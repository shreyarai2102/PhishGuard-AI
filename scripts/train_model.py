import os
import sys
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# IMPORT FEATURE EXTRACTOR
# ============================================================

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ML_SERVICE_PATH = os.path.join(
    PROJECT_ROOT,
    "ml-service"
)

sys.path.insert(0, ML_SERVICE_PATH)

from feature_extractor import extract_features


# ============================================================
# PATHS
# ============================================================

DATASET_PATH = os.path.join(
    PROJECT_ROOT,
    "dataset",
    "PhiUSIIL_Phishing_URL_Dataset.csv"
)

MODEL_DIR = os.path.join(
    PROJECT_ROOT,
    "models"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "phishguard_model.pkl"
)

FEATURE_PATH = os.path.join(
    MODEL_DIR,
    "feature_columns.pkl"
)


# ============================================================
# LOAD DATASET
# ============================================================

print("\nLoading dataset...")

df = pd.read_csv(DATASET_PATH)

print("Dataset shape:", df.shape)

print("\nLabel distribution:")
print(df["label"].value_counts())


# ============================================================
# EXTRACT FEATURES
# ============================================================

print("\nExtracting URL features...")
print("This may take a few minutes...\n")


feature_rows = []

for i, url in enumerate(df["URL"]):

    try:
        features = extract_features(str(url))
        feature_rows.append(features)

    except Exception as e:
        print(f"Error processing URL at index {i}: {e}")
        feature_rows.append({})

    if i % 10000 == 0:
        print(f"Processed {i}/{len(df)} URLs")


X = pd.DataFrame(feature_rows)

y = df["label"]


# ============================================================
# CLEAN FEATURES
# ============================================================

X = X.fillna(0)


print("\nFeature shape:", X.shape)

print("\nFeatures:")
print(list(X.columns))


# ============================================================
# SAVE FEATURE ORDER
# ============================================================

feature_columns = list(X.columns)

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(
    feature_columns,
    FEATURE_PATH
)

print("\nFeature columns saved.")


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# RANDOM FOREST
# ============================================================

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced_subsample",
    min_samples_leaf=2
)

model.fit(
    X_train,
    y_train
)

print("Training complete!")


# ============================================================
# EVALUATION
# ============================================================

print("\nEvaluating model...")

y_pred = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n======================================")
print(f"Accuracy: {accuracy * 100:.2f}%")
print("======================================")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["SAFE", "PHISHING"]
    )
)


# ============================================================
# CONFUSION MATRIX
# ============================================================

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

print("\nFeature Importance:")

importance = sorted(
    zip(
        X.columns,
        model.feature_importances_
    ),
    key=lambda x: x[1],
    reverse=True
)

for feature, score in importance:

    print(
        f"{feature:30s} {score:.4f}"
    )


# ============================================================
# SAVE MODEL
# ============================================================

joblib.dump(
    model,
    MODEL_PATH
)


print("\n======================================")
print("MODEL SAVED")
print("======================================")

print("Model:", MODEL_PATH)
print("Features:", FEATURE_PATH)
print("Number of features:", model.n_features_in_)