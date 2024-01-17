from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "manish.docx (4).pdf"
profile_pic = current_dir / "assets" / "profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Manish Kumar Singh"
PAGE_ICON = ":wave:"
NAME = "Manish Kumar Singh"
DESCRIPTION = """
Software Developer 
"""
EMAIL = "manish9984821560@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": " www.linkedin.com/in/manish-kumar-singh-0086a32",
    "GitHub": " https://github.com/mannu1995 ",
}
PROJECTS = {
    "🏆 EmployeeManagement - I workedandcreatedtheCRUDoperationforadding": " https://github.com/mannu1995/Emoployee_management_system",
    "🏆 Schoot_Tearchers_Student_data_API - Web app with mySQL database": " https://github.com/mannu1995/School_Teacher_Studend_api",
    "🏆  I havecreated this project in which we canconvert the image....": "https://github.com/mannu1995/Image_editer",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️  NareshIT, Hyderabad—PythonDjango
 Developer
 June 2023– August 2023
 I havedonemytrainingfromNareshITforPythonandDjango.Here,I
 learnt about Python andDjangoandtheirfunctionality .I learnt how third
 party applications can communicate through APIs.
 ● HereIworkedonaSchoolmanagementprojectwith5
 teammembers.
 ● IworkedonCRUDoperations,onewithDjangoandotherone
 with Django, Ajax andjQuery


-✔️ SwamiVivekanandUniversitySagar(M.P.)—B.Sc.
 ● Percentage:64.69%
 ● Division:FirstDivision

"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, HTML
- 📊  API,Github
- 📚 Framework : Django, Rest_Fremwork
- 🗄️ Databases:  MySQL
"""
)


st.write('\n')
st.subheader("Address")
st.write(
    """
- 👩‍💻 Kashahai Road karwi chitrkoot(up)
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")