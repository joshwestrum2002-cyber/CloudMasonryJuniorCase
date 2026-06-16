import os
from flask import Flask, render_template, jsonify, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize the NASA API
NASA_API_KEY = os.getenv("NASA_API_KEY")
NASA_IMAGE_ENDPOINT = "https://images-api.nasa.gov"

# Run Index
@app.route("/")
def home():
    return render_template("index.html")

# Search for photos
@app.route("/search")
def search_photos():
    keyword = request.args.get("q", "").strip()
    startDate = request.args.get("yearStart")
    endDate = request.args.get("yearEnd")
    yearStart = startDate[:4] if startDate else None
    yearEnd = endDate[:4] if endDate else None

    # Validate the inputs
    if not keyword or not startDate or not endDate:
        return jsonify({"error": "Keyword, Start Date, and End Date are required"}), 400

    if not yearStart or not yearEnd:
        return jsonify({"error": "Start Date and End Date are required"}), 400

    params = {
        "q": keyword,
        "yearStart": yearStart,
        "yearEnd": yearEnd,
        "media_type": "image",
        "api_key": NASA_API_KEY
    }

    # Get request to the NASA API
    try:
        response = requests.get(NASA_IMAGE_ENDPOINT, params=params, timeout=20)
    except Exception as e:
        return jsonify({"error": f"Error occurred while fetching data: {str(e)}"}), 500

    if response.status_code != 200:
        return jsonify({"error": "NASA API error"}), 502

    # Parse the JSON response
    try:
        data = response.json()
    except:
        return jsonify({"error": "NASA returned invalid JSON"}), 502

    
    # Extract the photos from the response
    items = data.get("collection", {}).get("items", [])
    photos = []
    for item in items:
        if "links" in item and len(item["links"]) > 0:
            photos.append(item["links"][0].get("href", ""))

    if not photos:
        return jsonify({"photos": [], "error": "No photos found"}), 200

    return jsonify({"photos": photos})

if __name__ == "__main__":
    app.run(debug=True)
