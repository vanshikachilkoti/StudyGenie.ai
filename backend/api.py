from flask import Flask, request, jsonify
from flask_cors import CORS
from validators import validate_form_data
from roadmap_generator import generate_roadmap
from email_service import send_email
from calendar_service import add_to_calendar

app = Flask(__name__)
CORS(app)  # Allow cross-origin from Streamlit

@app.route("/generate-roadmap", methods=["POST"])
def generate_roadmap_route():
    data = request.get_json()

    # Step 1: Validate Input
    is_valid, error = validate_form_data(data)
    if not is_valid:
        return jsonify({"error": error}), 400

    try:
        # Step 2: Generate Roadmap using Gemini
        roadmap = generate_roadmap(data)

        # Step 3: Email the roadmap
        send_email(to=data["email"], subject="🎓 Your StudyGenie.ai Roadmap", body=roadmap)

        # Step 4: Optionally Add to Google Calendar
        if data.get("add_to_calendar"):
            add_to_calendar(data["email"], roadmap, data["deadline"])

        return jsonify({"roadmap": roadmap}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
