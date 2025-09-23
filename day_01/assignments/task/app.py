from flask import Flask, jsonify, redirect, url_for, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Flask API App!</h1>"

@app.route("/predict-age")
def predict_age():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Name query parameter is required"}), 400

    response = request.get(f"https://api.agify.io/?name={name}")
    data = response.json()
    return jsonify(data)


@app.route("/submit-name", methods=["GET"])
def submit_name():
    name = request.args.get("name")
    if not name:
        return redirect(url_for("home"))
    return redirect(url_for("predict_age", name=name))

if __name__ == "__main__":
    app.run(debug=True)

