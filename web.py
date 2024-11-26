import streamlit as st
from PIL import Image

if "photo" not in st.session_state:
    st.session_state.photo = None

if "biography" not in st.session_state:
    st.session_state.biography = {
        "Name": "Vanezza Boholst Ragutero",
        "Age": "18",
        "About Me": (
            "As a youthful member of Gen Z, I consider myself a passionate and diligent 18-year-old student "
            "pursuing a Bachelor of Science in Computer Engineering at Surigao del Norte State University. "
            "With a passion for learning and gaining a deeper understanding of emerging technologies while "
            "honing my communication skills, I thrive on challenges that foster not just my personal growth "
            "but also professional growth. I am not only academically inclined but also an avid sports "
            "enthusiast, particularly in badminton, and I enjoy exploring diverse perspectives and reading "
            "books in my free time."
        ),
        "Education": [
            "Bachelor of Science in Computer Engineering, Surigao del Norte State University, 2024 (1st year)"
        ],
        "Skills": ["Good Communication Skill"],
        "Hobbies": ["Playing Sports Games"],
        "Contact": {
            "Email": "vragutero@gmail.com",
            "LinkedIn": "https://linkedin.com/in/yourprofile",
        },
    }

default_photo_path = "c:/Users/User/Pictures/Camera Roll/1732190184893.jpg"

st.subheader("Upload Your Photo")
uploaded_photo = st.file_uploader("Upload a photo (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_photo:
    st.session_state.photo = uploaded_photo
    st.success("Photo uploaded successfully!")

if st.session_state.photo:
    st.image(st.session_state.photo, caption="Uploaded Photo", width=200)
else:
    try:
        default_image = Image.open(default_photo_path)
        st.image(default_image, caption="Default Photo", width=200)
    except FileNotFoundError:
        st.error("Default photo not found. Please upload a photo.")

st.subheader("Biography")
for key, value in st.session_state.biography.items():
    if isinstance(value, list):
        st.write(f"**{key}:** {', '.join(value)}")
    elif isinstance(value, dict):
        st.write(f"**{key}:**")
        for sub_key, sub_value in value.items():
            st.write(f"- {sub_key}: {sub_value}")
    else:
        st.write(f"**{key}:** {value}")

st.subheader("Add to Biography")
add_section = st.selectbox("Select Section to Add to:", list(st.session_state.biography.keys()))
new_entry = st.text_input("Enter New Entry")
if st.button("Add"):
    if add_section in st.session_state.biography:
        if isinstance(st.session_state.biography[add_section], list):
            st.session_state.biography[add_section].append(new_entry)
            st.success(f"Added '{new_entry}' to {add_section}.")
        elif isinstance(st.session_state.biography[add_section], dict):
            sub_key = st.text_input("Enter Sub-Category")
            if sub_key and new_entry:
                st.session_state.biography[add_section][sub_key] = new_entry
                st.success(f"Added '{sub_key}: {new_entry}' to {add_section}.")
        else:
            st.session_state.biography[add_section] = new_entry
            st.success(f"Updated {add_section} with '{new_entry}'.")
    else:
        st.error("Section not found.")

st.subheader("Delete from Biography")
delete_section = st.selectbox("Select Section to Delete from:", list(st.session_state.biography.keys()))
if isinstance(st.session_state.biography[delete_section], list):
    delete_entry = st.selectbox("Select Entry to Delete:", st.session_state.biography[delete_section])
    if st.button("Delete"):
        st.session_state.biography[delete_section].remove(delete_entry)
        st.success(f"Deleted '{delete_entry}' from {delete_section}.")
elif isinstance(st.session_state.biography[delete_section], dict):
    delete_key = st.selectbox("Select Sub-Category to Delete:", list(st.session_state.biography[delete_section].keys()))
    if st.button("Delete"):
        del st.session_state.biography[delete_section][delete_key]
        st.success(f"Deleted '{delete_key}' from {delete_section}.")
else:
    if st.button("Delete"):
        st.session_state.biography[delete_section] = None
        st.success(f"Deleted content of {delete_section}.")
