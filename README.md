# 🎓 Algorithm Project with Student Dashboard

This project combines classical **sorting algorithms** (Quick Sort, Merge Sort, and Radix Sort) with an interactive **Student Dashboard** built using Streamlit to manage and visualize student data.

---

## 📌 Project Structure

- `program.py` (formerly `student_dashboard.py`): Streamlit web app for data input, sorting, and visualization.
- `sorting_algorithms.py`: Contains implementations of Quick, Merge, and Radix sorting algorithms.
- `database.py`: Handles storing and retrieving student data.
- `generate_report.py` / `generate_report_pdf.py`: Scripts to produce the PDF dashboard report.
- `README.md`: Project documentation.

---

## 🎯 Goals

- Practice core algorithmic concepts.
- Integrate sorting logic with real-world student data.
- Visualize and analyze student performance in an interactive UI.

---

## 📊 Student Dashboard

### ✅ Overview

The **Student Dashboard** is a web application built using the Streamlit framework. It provides an interactive platform for managing and visualizing student data, including names, grades, and performance levels. The application features a modern dark theme and a responsive layout.

---

### ✨ Features

1. **Dark Theme and Styling**

   - Custom dark mode applied using CSS.
   - Modern styling for buttons, tables, and charts.

2. **Header and Footer**

   - Engaging header image.
   - Footer with branding and copyright.

3. **Data Input**

   - Enter student name, grade, and performance.
   - “Submit” button saves data into the database.

4. **Data Display**

   - Display all student records sorted by grade and performance.
   - Interactive, styled table for readability.

5. **Statistics**

   - Calculates and shows mean, median, and mode of grades via `st.metric`.

6. **Visualizations**

   - **Histogram** of grades (Plotly).
   - **Pie chart** of performance levels.

7. **Sorting Options**
   - Sort students by name, grade, or performance.
   - Visualize each sort with a bar chart.

---

## 🧮 Sorting Algorithms

Implemented and applied on student data:

- **Quick Sort**: Efficient divide-and-conquer algorithm.
- **Merge Sort**: Stable recursive sorting algorithm.
- **Radix Sort**: Fast non-comparative sorting for integers.

These algorithms demonstrate how different sorting methods affect the dataset and allow interactive exploration through the dashboard.

---

## ⚙️ Technologies Used

- **Python**
- **Streamlit**
- **Plotly**
- **SQLite** or **CSV** for storage
- **Custom CSS** for theming

---

## 🚀 How to Run the App

1. تثبيت المتطلبات:
   ```bash
   pip install streamlit plotly
   ```
