import joblib

model = joblib.load("../models/phishguard_model.pkl")

print("Model:", model)
print("Number of features:", model.n_features_in_)

try:
    print("Classes:", model.classes_)
except Exception:
    print("No classes found")
