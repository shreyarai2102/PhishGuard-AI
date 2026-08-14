import os
import joblib


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ============================================================
# MODEL PATH
# ============================================================

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "phishguard_model.pkl"
)


FEATURE_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "feature_columns.pkl"
)


# ============================================================
# CHECK FILES
# ============================================================

print("\n======================================")
print("PHISHGUARD MODEL INSPECTION")
print("======================================")

print("\nProject root:")
print(PROJECT_ROOT)

print("\nModel path:")
print(MODEL_PATH)

print("\nFeature path:")
print(FEATURE_PATH)


if not os.path.exists(MODEL_PATH):
    print("\nERROR: Model file not found!")
    raise SystemExit(1)


if not os.path.exists(FEATURE_PATH):
    print("\nERROR: Feature columns file not found!")
    raise SystemExit(1)


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(MODEL_PATH)

feature_columns = joblib.load(FEATURE_PATH)


# ============================================================
# MODEL INFORMATION
# ============================================================

print("\n======================================")
print("MODEL INFORMATION")
print("======================================")

print("\nModel type:")
print(type(model).__name__)

print("\nNumber of features:")
print(model.n_features_in_)

print("\nNumber of saved feature columns:")
print(len(feature_columns))

print("\nClasses:")
print(model.classes_)


# ============================================================
# FEATURE COLUMNS
# ============================================================

print("\n======================================")
print("FEATURE COLUMNS")
print("======================================")

for i, feature in enumerate(feature_columns, start=1):
    print(f"{i:2}. {feature}")


# ============================================================
# RANDOM FOREST INFORMATION
# ============================================================

if hasattr(model, "n_estimators"):
    print("\n======================================")
    print("RANDOM FOREST")
    print("======================================")

    print("Number of trees:")
    print(model.n_estimators)

    print("\nMinimum samples per leaf:")
    print(model.min_samples_leaf)


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

if hasattr(model, "feature_importances_"):

    print("\n======================================")
    print("FEATURE IMPORTANCE")
    print("======================================")

    importance = sorted(
        zip(
            feature_columns,
            model.feature_importances_
        ),
        key=lambda x: x[1],
        reverse=True
    )

    for feature, score in importance:
        print(f"{feature:35} {score:.6f}")


print("\n======================================")
print("INSPECTION COMPLETE")
print("======================================")