from flask import Flask, request, jsonify
from predictor import predict_url

app = Flask(__name__)


@app.route("/")
def home():
    return "PhishGuard AI ML Service Running"


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    result = predict_url(data["url"])

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
