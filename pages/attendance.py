import streamlit as st
from database.mongodb import (
    students_collection,
    attendance_collection
)

st.title(":rainbow[Attendance Management]")

# Fetch students
students = list(students_collection.find())

if not students:
    st.warning("No students available")
    st.stop()

# Build student name list
student_names = []
for student in students:
    full_name = student["first_Name"].title() + " " + student["last_Name"].title()
    student_names.append(full_name)

# Input fields
selected_student = st.selectbox("Select student", student_names)
attendance_date = st.date_input("Attendance date")
status = st.selectbox("Status", ["Present", "Absent"])

# Save attendance
if st.button("Save attendance"):
    # Prevent duplicate entry for same student/date
    existing = attendance_collection.find_one({
        "student_name": selected_student,
        "date": str(attendance_date)
    })
    if existing:
        st.warning("Attendance already recorded for this student on this date.")
    else:
        attendance_collection.insert_one({
            "student_name": selected_student,   # ✅ consistent field name
            "date": str(attendance_date),
            "status": status.lower()            # store lowercase for consistency
        })
        st.success("Attendance saved")

# Show records
st.subheader("Attendance Records")
records = list(attendance_collection.find())
for record in records:
    st.write(
        record["student_name"], "|",
        record["date"], "|",
        record["status"]
    )

# Attendance summary
st.subheader("Attendance Summary")
for student in student_names:
    total = attendance_collection.count_documents({"student_name": student})
    present = attendance_collection.count_documents({
        "student_name": student,
        "status": "present"
    })

    if total > 0:
        percentage = (present / total) * 100
        st.write(f"{student}: {round(percentage, 2)}%")
