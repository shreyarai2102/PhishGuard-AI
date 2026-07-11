from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/phishguard_model.pkl")

@app.route("/")
def home():
    return "PhishGuard AI ML Service Running"

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(debug=True)