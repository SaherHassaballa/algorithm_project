import streamlit as st
from student_class import Student
import pyodbc
from student_sorted import merge_sort
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=student;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()


name = st.text_input('Enter your name:', key='name_input')
grade = st.slider('Enter your grade:', key='grade_input')
performance = st.text_input('Enter your performance:', key='performance_input')


if st.button('submit'):
    cursor.execute('''INSERT INTO student_table (name, grade, perf) VALUES (?, ?, ?)''', (name, grade, performance))
    conn.commit()
    st.success("Data inserted successfully")
    st.write(f"Name: {name}, Grade: {grade}, Performance: {performance}")

if st.button('sort grades'):
    list_grade=[]
    cursor.execute('''select grade from student_table ''')
    grades = cursor.fetchall()
    for i in grades:
        list_grade.append(i[0])
    sorted_grades =merge_sort(list_grade)
    st.write(f'{sorted_grades}')
    if grades:
        # fig = px.histogram(sorted_grades , nbins=30, title="Histogram with Plotly", range_x=[0, 100])
        # st.plotly_chart(fig)
        # fig = plt.figure()
        # sns.histplot(sorted_grades , bins=10)
        # st.pyplot(fig)
        fig, ax = plt.subplots(figsize=(10, 5))
        # sns.set_style("whitegrid")
        # sns.histplot(sorted_grades, bins=10, kde=True, color="#36a2eb", edgecolor="black", ax=ax)
        
        # ax.set_title("Histogram of Grades", fontsize=16, fontweight='bold')
        # ax.set_xlabel("Grades", fontsize=14)
        # ax.set_ylabel("Frequency", fontsize=14)
        # ax.tick_params(axis='both', labelsize=12)

        # st.pyplot(fig)
        df = pd.DataFrame(sorted_grades)
        st.write(f'''# the mean , median , mode of class grade {round(df.mean()[0] ,2)} , {round(df.median()[0] ,2)} ,  {round(df.mode()[0][0],2)}''')
        fig = px.histogram(sorted_grades, nbins=10, title="Histogram of Grades", 
                        labels={'value': 'Grade'}, color_discrete_sequence=['#00cc99'])
        
        # إضافة بعض التحسينات في الشكل
        fig.update_layout(
            title="Histogram of Student Grades",
            xaxis_title="Grades",
            yaxis_title="Frequency",
            template="plotly_dark",  # تغيير القالب لواحد تفاعلي
            bargap=0.1,  # المسافة بين الأعمدة
            hovermode="closest",  # جعل التفاعل مع أقرب نقطة
            xaxis=dict(tickmode='linear', tick0=0, dtick=10)  # تخصيص التواريخ
        )
        
        st.plotly_chart(fig)
    else:
        st.warning("there is no grades")



