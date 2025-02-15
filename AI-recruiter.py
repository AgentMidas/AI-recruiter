import streamlit as st
import ollama

# Define the AI model
model = "llama3"

# Function to analyze the resume
def analyze_resume(resume_text):
    prompt = f"Analyze the following resume and extract key skills, experiences, and qualifications:\n\n{resume_text}"
    response = ollama.generate(model=model, prompt=prompt)
    return response["response"]

# Function to match resume with job description
def match_candidate(job_description, candidate_profile):
    prompt = f"Match the following candidate profile to the job description:\n\nJob Description:\n{job_description}\n\nCandidate Profile:\n{candidate_profile}"
    response = ollama.generate(model=model, prompt=prompt)
    return response["response"]

# Streamlit UI
st.title("📄 Resume Analyzer & Job Matcher")

# File upload
uploaded_file = st.file_uploader("Upload your resume (TXT file only)", type=["txt"])

# Job description input
job_description = st.text_area("Enter the job description")

if uploaded_file is not None:
    # Read file contents
    resume_text = uploaded_file.read().decode("utf-8")

    # Show resume text
    st.subheader("Uploaded Resume Content:")
    st.text(resume_text)

    # Analyze Resume
    if st.button("Analyze Resume"):
        analysis = analyze_resume(resume_text)
        st.subheader("Resume Analysis:")
        st.write(analysis)

    # Match with Job Description
    if job_description and st.button("Match with Job"):
        match_result = match_candidate(job_description, resume_text)
        st.subheader("Candidate Match Result:")
        st.write(match_result)
