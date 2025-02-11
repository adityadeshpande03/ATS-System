import streamlit as st
import os
from config import get_gemini_response
from input import input_pdf_content, input_prompt1, input_prompt2

st.set_page_config(page_title="ATS System")
st.header("📄 ATS Resume Tracking System")

# Sidebar with instructions
st.sidebar.title("📌 Instructions")
st.sidebar.write("1️⃣ Enter the job description in the text area.")
st.sidebar.write("2️⃣ Upload your resume in PDF format 📄.")
st.sidebar.write("3️⃣ Click '🔍 Tell Me About The Resume' to get an analysis.")
st.sidebar.write("4️⃣ Click '📊 Percentage Match' to see how well your resume matches the job description.")
st.sidebar.write("5️⃣ Review the output and make improvements to your resume accordingly.")

# Main content
input_text = st.text_area("📝 Job Description: ", key="input")

uploaded_file = st.file_uploader("📤 Upload your resume [PDF format]", type=["pdf"])

if uploaded_file is not None:
    st.write("✅ Resume uploaded successfully!")

submit1 = st.button("🔍 Tell Me About The Resume")
submit4 = st.button("📊 Percentage Match")

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_content(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("📢 The response is...")
        st.write(response)
    else:
        st.write("⚠️ Please upload the resume file")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_content(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("📢 The response is...")
        st.write(response)
    else:
        st.write("⚠️ Please upload the resume file")
