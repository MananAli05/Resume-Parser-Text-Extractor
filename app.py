import streamlit as st
import fitz 
import re
st.title("Resume Parsing (Extract Text)")
file=st.file_uploader("Upload A PDF",type=['pdf','docx'])
if file is not None:
    doc=fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text=page.get_text()
        st.subheader("Extracted Text")
        st.write(text)
        st.title("Find Emails and Phone No in Resume Using Regex")
        email=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_no=r'\b\d{13}\b'
        found_emails = re.findall(email,text)
        found_phones = re.findall(phone_no, text)
        st.subheader("Found Emails")
        st.write(found_emails)
        st.subheader("Found Phone Numbers")
        st.write(found_phones)
        skills = ['Python', 'Java', 'JavaScript', 'C++', 'SQL','Django', 'Flask', 'React', 'Node.js','Machine Learning', 'Deep Learning','Html', 'CSS', 'Bootstrap','Power BI', 'Tableau']
        for skill in skills:
            if skill in text:
                st.write(f"Found skill: {skill}")
        st.title("Education and Experience")
        education= r'\b(Matriculation|Intermediate|Bachelor|Master|PhD|BSc|MSc|B.E.|B.Tech|M.Tech)\b'
        experience = r'\b(\d+ years? of experience|fresher|entry-level)\b'
        found_education = re.findall(education,text)
        found_experience = re.findall(experience, text)
        st.subheader("Found Education")
        st.write(found_education)
        st.subheader("Found Experience")
        st.write(found_experience)

