import pandas as pd
import joblib

from feature_extractor import extract_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

# Load dataset
df = pd.read_csv("../dataset/PhiUSIIL_Phishing_URL_Dataset.csv")

print("Dataset loaded:", df.shape)

# Extract features
feature_list = []

for i, url in enumerate(df["URL"]):
    feature_list.append(extract_features(url))

    if (i + 1) % 10000 == 0:
        print(f"Processed {i + 1} URLs")

X = pd.DataFrame(feature_list)
y = df["label"]

print("Feature matrix:", X.shape)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

print("Training model...")
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

print("\n========== RESULTS ==========")
print("Accuracy :", accuracy_score(y_test, pred))
print("Precision:", precision_score(y_test, pred))
print("Recall   :", recall_score(y_test, pred))
print("F1 Score :", f1_score(y_test, pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred))

# Save model
joblib.dump(model, "../models/phishguard_model.pkl")
joblib.dump(list(X.columns), "../models/feature_columns.pkl")

print("\nModel saved successfully!")
print("Feature columns saved!")
