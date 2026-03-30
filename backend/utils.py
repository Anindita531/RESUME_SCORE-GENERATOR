def extract_skills(text):
    skills_db = [
        "python", "java", "sql", "machine learning",
        "pandas", "numpy", "scikit-learn", "html", "css", "git", "github"
    ]

    found = set()

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found.add(skill)

    return found


def calculate_score(found_skills, required_skills):
    if not required_skills:
        return 0

    match = len(set(found_skills).intersection(set(required_skills)))
    total = len(required_skills)

    return (match / total) * 100