import streamlit as st 
from database.mongodb import students_collection
st.title("Student Registration")

first_name =st.text_input(

    "first name"
)
last_name =st.text_input(

    "last name"
)
email =st.text_input(

    "email"
)
course =st.text_input(

    "course"
)
if st.button("Register Student"):
    students_collection.insert_one({
          "first_Name": first_name,
          "last_Name": last_name,

    })
    st.success(
        "Student registered Sucessfully"
    )