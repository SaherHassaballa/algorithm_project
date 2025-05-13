from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)


def create_project_report_pdf(filepath):
    # Create a PDF document
    pdf = SimpleDocTemplate(filepath, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Title
    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=20,
        alignment=1,  # Center alignment
        textColor=colors.darkblue,
    )
    elements.append(Paragraph("Student Dashboard - Project Report", title_style))
    elements.append(Spacer(1, 20))

    # Overview
    elements.append(Paragraph("Overview", styles["Heading2"]))
    elements.append(
        Paragraph(
            "The Student Dashboard is a web application built using the Streamlit framework. "
            "It provides an interactive platform for managing and visualizing student data, "
            "including names, grades, and performance levels. The application is designed with "
            "a modern dark theme and includes various features for data input, visualization, "
            "and statistical analysis.",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Features
    elements.append(Paragraph("Features", styles["Heading2"]))
    features = [
        "Dark Theme and Styling: A custom dark theme is applied using CSS for a visually appealing interface.",
        "Header and Footer: A header image is included to make the app more engaging, and a footer with branding is added.",
        "Data Input: Users can input student details (name, grade, and performance) through text fields.",
        "Data Display: Displays all student records in a sorted table (sorted by performance and grade).",
        "Statistics: Calculates and displays key statistics for grades (Mean, Median, Mode).",
        "Visualizations: Includes a histogram for grades and a pie chart for performance distribution.",
        "Individual Sorting: Allows sorting data by name, grade, or performance with interactive visuals.",
    ]
    for feature in features:
        elements.append(Paragraph(f"- {feature}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Technical Highlights
    elements.append(Paragraph("Technical Highlights", styles["Heading2"]))
    highlights = [
        "Streamlit Framework: Used for creating interactive web applications.",
        "Database Integration: Interacts with a database through the Student class.",
        "Plotly for Visualizations: Creates interactive and visually appealing charts.",
        "CSS for Custom Styling: Applies a dark theme and improves the app's appearance.",
    ]
    for highlight in highlights:
        elements.append(Paragraph(f"- {highlight}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Strengths
    elements.append(Paragraph("Strengths", styles["Heading2"]))
    strengths = [
        "User-Friendly Interface: Intuitive and easy to use.",
        "Interactive Visualizations: Enhances data exploration and understanding.",
        "Modern Design: Dark theme and custom styling make the app visually appealing.",
        "Comprehensive Features: Combines data management, statistics, and visualization.",
    ]
    for strength in strengths:
        elements.append(Paragraph(f"- {strength}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Suggestions for Further Improvements
    elements.append(
        Paragraph("Suggestions for Further Improvements", styles["Heading2"])
    )
    improvements = [
        "Error Handling: Add error messages for invalid inputs and handle database connection errors.",
        "Performance Optimization: Cache database queries to improve performance for large datasets.",
        "Export Options: Allow users to export the displayed data (e.g., as a CSV file).",
        "Authentication: Add user authentication to restrict access to sensitive data.",
        "Mobile Responsiveness: Optimize the layout for better usability on mobile devices.",
    ]
    for improvement in improvements:
        elements.append(Paragraph(f"- {improvement}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Explanation of Algorithms
    elements.append(Paragraph("Explanation of Algorithms", styles["Heading2"]))
    elements.append(
        Paragraph(
            "The Student Dashboard project uses several algorithms for sorting, statistical calculations, "
            "and data processing. Below is a detailed explanation of the algorithms used:",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Merge Sort
    elements.append(Paragraph("1. Merge Sort", styles["Heading3"]))
    elements.append(
        Paragraph(
            "Purpose: Used to sort grades in ascending order. Merge Sort is a divide-and-conquer algorithm "
            "that splits the list into smaller sublists, sorts them, and merges them back together.",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "Advantages: Stable sorting algorithm with a time complexity of O(n log n).",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Quick Sort
    elements.append(Paragraph("2. Quick Sort", styles["Heading3"]))
    elements.append(
        Paragraph(
            "Purpose: Used to sort names in alphabetical order. Quick Sort selects a pivot element, partitions "
            "the list into elements less than, equal to, and greater than the pivot, and recursively sorts the partitions.",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "Advantages: Efficient for large datasets with an average time complexity of O(n log n).",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Radix Sort
    elements.append(Paragraph("3. Radix Sort", styles["Heading3"]))
    elements.append(
        Paragraph(
            "Purpose: Used to sort performance levels based on a predefined order (e.g., 'A+', 'A', 'B+', etc.). "
            "Radix Sort groups data into buckets based on numeric mappings and concatenates the buckets to produce a sorted list.",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "Advantages: Non-comparative sorting algorithm with a time complexity of O(n).",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Statistical Calculations
    elements.append(Paragraph("4. Statistical Calculations", styles["Heading3"]))
    elements.append(
        Paragraph(
            "The project includes algorithms to calculate mean, median, and mode for grades:",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "- Mean: The average of all grades, calculated in O(n) time.",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "- Median: The middle value in a sorted list, calculated in O(n log n) time due to sorting.",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "- Mode: The most frequently occurring value, calculated in O(n) time.",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Sorting Students
    elements.append(Paragraph("5. Sorting Students", styles["Heading3"]))
    elements.append(
        Paragraph(
            "Purpose: Sorts students by performance and grade. Students are first sorted by performance "
            "(using a predefined order) and then by grade in descending order.",
            styles["BodyText"],
        )
    )
    elements.append(
        Paragraph(
            "Advantages: Custom sorting ensures meaningful organization of student data.",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 12))

    # Add a page break for better layout
    elements.append(PageBreak())

    # Conclusion
    elements.append(Paragraph("Conclusion", styles["Heading2"]))
    elements.append(
        Paragraph(
            "The Student Dashboard is a well-designed and feature-rich application for managing "
            "and visualizing student data. It effectively combines functionality, aesthetics, and "
            "interactivity, making it a valuable tool for educators and administrators. With minor "
            "enhancements, it can become even more robust and user-friendly.",
            styles["BodyText"],
        )
    )

    # Add a page break for better layout
    elements.append(PageBreak())

    # Build the PDF
    pdf.build(elements)
    print(f"PDF report saved to {filepath}")


# Generate the PDF report
create_project_report_pdf(
    "c:\\Users\\saher\\Desktop\\workshop\\algorithm_project\\Student_Dashboard_Report.pdf"
)
