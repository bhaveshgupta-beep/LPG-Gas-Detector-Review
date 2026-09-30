from flask import Flask, render_template, request
from datetime import datetime
import urllib.request
import json

app = Flask(__name__)

REVIEWS_FILE = "reviews.txt"

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxfhrGMgKvfuhCbSjPhZwDsaHHScO6km-GrVBG_8X5AlPW2A-vJPE0yZv3ZNGtyLUUk/exec"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit_review():

    name = request.form.get("name", "").strip()
    review = request.form.get("review", "").strip()
    rating = request.form.get("rating", "5")

    try:
        rating = int(rating)
    except ValueError:
        rating = 5

    rating = max(1, min(5, rating))

    if name and review:

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Save a local copy
        with open(REVIEWS_FILE, "a", encoding="utf-8") as file:

            file.write("\n")
            file.write("=" * 45 + "\n")
            file.write("       LPG GAS GUARDIAN - REVIEW\n")
            file.write("=" * 45 + "\n\n")

            file.write(f"Name: {name}\n")
            file.write(f"Rating: {rating}/5\n")
            file.write(f"Review: {review}\n")
            file.write(f"Date: {current_time}\n")

            file.write("\n" + "=" * 45 + "\n")

        # Send review to Google Sheet
        data = {
            "name": name,
            "rating": rating,
            "review": review
        }

        try:

            json_data = json.dumps(data).encode("utf-8")

            req = urllib.request.Request(
                GOOGLE_SCRIPT_URL,
                data=json_data,
                headers={
                    "Content-Type": "application/json"
                },
                method="POST"
            )

            urllib.request.urlopen(req, timeout=10)

        except Exception as error:

            print("Google Sheet error:", error)

    return render_template("success.html")


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )