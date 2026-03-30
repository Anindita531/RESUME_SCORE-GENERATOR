from flask import Flask, request, jsonify
from utils import extract_skills, calculate_score

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data.get("text", "")
    required_skills = data.get("required_skills", [])

    found_skills = extract_skills(resume_text)
    score = calculate_score(found_skills, required_skills)

    missing_skills = list(set(required_skills) - set(found_skills))

    return jsonify({
        "skills": list(found_skills),
        "score": score,
        "missing_skills": missing_skills
    })

if __name__ == "__main__":
    app.run(debug=True)