from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/photos")
def photos():
    url = "https://jsonplaceholder.typicode.com/photos?_limit=10"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)