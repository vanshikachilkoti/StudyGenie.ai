def validate_form_data(data):
    required_fields = ["topic", "level", "goal", "hours", "formats", "email", "learning_style", "deadline"]

    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing or empty field: {field}"

    # Extra email check (very basic)
    if "@" not in data["email"]:
        return False, "Invalid email address."

    return True, None
