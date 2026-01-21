from flask import Flask, request, jsonify
from model.intent_model import IntentModel
import os

app = Flask(__name__)
model = IntentModel()

@app.route("/health")
def health():
    return jsonify({"status":"ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")
    return jsonify(model.predict(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
