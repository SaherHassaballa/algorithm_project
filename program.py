# app.py
import streamlit as st
from student_class import Student
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("🎓 Student Dashboard")

# Apply dark theme and improve layout
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff7f0e;
        color: black;
    }
    .stDataFrame {
        background-color: #1e1e1e;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a header image for excitement
st.image(
    "https://via.placeholder.com/1200x300.png?text=Welcome+to+Student+Dashboard",
    use_column_width=True,
)

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
    grades = [s["Grade"] for s in Student.get_all_students()]
    mean_val = Student.calculate_mean(grades)
    median_val = Student.calculate_median(grades)
    mode_val = Student.calculate_mode(grades)
    col1, col2, col3 = st.columns(3)
    col1.metric("Mean Grade", f"{mean_val:.2f}" if mean_val is not None else "—")
    col2.metric("Median Grade", f"{median_val:.2f}" if median_val is not None else "—")
    col3.metric("Mode Grade", f"{mode_val}" if mode_val is not None else "—")

    # Enhanced visuals for histogram
    st.subheader("Grade Distribution Histogram")
    hist_df = pd.DataFrame(grades, columns=["Grade"])
    fig = px.histogram(
        hist_df,
        x="Grade",
        nbins=10,
        title="Histogram of Student Grades",
        color_discrete_sequence=["#636EFA"],
    )
    fig.update_layout(
        xaxis_title="Grade",
        yaxis_title="Count",
        template="plotly_dark",
        bargap=0.1,
        font=dict(color="white"),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Add pie chart for performance distribution
    st.subheader("Performance Distribution")
    performance_counts = (
        pd.DataFrame(Student.get_sorted_performance(), columns=["Performance"])
        .value_counts()
        .reset_index(name="Count")
    )
    pie_fig = px.pie(
        performance_counts,
        names="Performance",
        values="Count",
        title="Performance Distribution",
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    pie_fig.update_layout(template="plotly_dark", font=dict(color="white"))
    st.plotly_chart(pie_fig, use_container_width=True)

# Individual Sort Buttons with Visuals
st.subheader("Sort Data Individually")
sort_option = st.radio("Sort by:", ["Name", "Grade", "Performance"], horizontal=True)

if sort_option == "Name":
    sorted_data = pd.DataFrame(Student.get_sorted_names(), columns=["Name"])
    st.table(sorted_data)
    st.bar_chart(sorted_data["Name"].value_counts())
elif sort_option == "Grade":
    sorted_data = pd.DataFrame(Student.get_sorted_grades(), columns=["Grade"])
    st.table(sorted_data)
    st.bar_chart(sorted_data["Grade"].value_counts())
elif sort_option == "Performance":
    sorted_data = pd.DataFrame(
        Student.get_sorted_performance(), columns=["Performance"]
    )
    st.table(sorted_data)
    st.bar_chart(sorted_data["Performance"].value_counts())
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
        st.table(
            pd.DataFrame(Student.get_sorted_performance(), columns=["Performance"])
        )

# Add a footer for branding
st.markdown(
    """
    <hr style="border:1px solid #ffffff;">
    <p style="text-align:center; color:gray;">
        Built with ❤️ using Streamlit | © 2023 Student Dashboard
    </p>
    """,
    unsafe_allow_html=True,
)
