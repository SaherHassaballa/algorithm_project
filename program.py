# app.py
import streamlit as st
from student_class import Student
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("🎓 Student Dashboard")

# Inputs
name = st.text_input("Enter your name:")
grade = st.text_input("Enter your grade:")
performance = st.text_input("Enter your performance (e.g., A+):")
student = Student(name, grade, performance)

# Submit
if st.button("Submit"):
    if student.insert_to_db():
        st.success("Data inserted successfully")
    else:
        st.error("Please fill all fields correctly")

# Display Sorted Table and Histogram with Statistics
if st.button("Display Data"):
    data = Student.sort_students()
    df = pd.DataFrame(data)
    st.subheader("Students (Sorted by Performance & Grade)")
    st.dataframe(df, use_container_width=True)

    # Calculate statistics
    grades = [s['Grade'] for s in Student.get_all_students()]
    mean_val = Student.calculate_mean(grades)
    median_val = Student.calculate_median(grades)
    mode_val = Student.calculate_mode(grades)
    col1, col2, col3 = st.columns(3)
    col1.metric("Mean Grade", f"{mean_val:.2f}" if mean_val is not None else "—")
    col2.metric("Median Grade", f"{median_val:.2f}" if median_val is not None else "—")
    col3.metric("Mode Grade", f"{mode_val}" if mode_val is not None else "—")

    # Histogram of all grades
    st.subheader("Grade Distribution Histogram")
    hist_df = pd.DataFrame(grades, columns=["Grade"])
    fig = px.histogram(hist_df, x="Grade", nbins=10,
                        title="Histogram of Student Grades")
    fig.update_layout(xaxis_title="Grade", yaxis_title="Count",
                        template="plotly_dark", bargap=0.1)
    st.plotly_chart(fig, use_container_width=True)

# Individual Sort Buttons
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Names Only"):
        st.table(pd.DataFrame(Student.get_sorted_names(), columns=["Name"]))
with col2:
    if st.button("Grades Only"):
        st.table(pd.DataFrame(Student.get_sorted_grades(), columns=["Grade"]))
with col3:
    if st.button("Performance Only"):
        st.table(pd.DataFrame(Student.get_sorted_performance(), columns=["Performance"]))
