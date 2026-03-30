import streamlit as st
import requests
import pdfplumber

st.title("Resume Analyzer 🔥")

# 📁 File Upload
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

skills_input = st.text_input("Required Skills (comma separated)")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


if st.button("Analyze"):

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)

        required_skills = [s.strip().lower() for s in skills_input.split(",")]

        response = requests.post(
            "http://127.0.0.1:5000/analyze",
            json={
                "text": resume_text,
                "required_skills": required_skills
            }
        )

        result = response.json()

        st.subheader("Score")
        st.write(result["score"])

        st.subheader("Detected Skills")
        st.write(result["skills"])

        st.subheader("Missing Skills")
        st.write(result["missing_skills"])

    else:
        st.error("Please upload a PDF file")