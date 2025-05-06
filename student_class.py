# student_class.py
import pyodbc
import pandas as pd

class Student:
    # Class-level DB connection and cursor (shared)
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=student;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()

    PERFORMANCE_ORDER = {
        "A+": 0, "A": 1, "A-": 2,
        "B+": 3, "B": 4, "B-": 5,
        "C+": 6, "C": 7, "C-": 8,
        "D+": 9, "D": 10, "D-": 11,
        "F": 12
    }

    def __init__(self, name=None, grade=None, performance=None):
        self.name = name
        self.grade = grade
        self.performance = performance

    def insert_to_db(self):
        """
        Instance: insert this student's record into the database.
        """
        if self.name and self.grade and self.performance:
            Student.cursor.execute(
                "INSERT INTO student_table (name, grade, perf) VALUES (?, ?, ?)",
                (self.name, int(self.grade), self.performance)
            )
            Student.conn.commit()
            return True
        return False

    @staticmethod
    def get_all_students():
        """Fetch all students with ID, Name, Grade, Performance."""
        Student.cursor.execute("SELECT id, name, grade, perf FROM student_table")
        rows = Student.cursor.fetchall()
        return [
            {"ID": r[0], "Name": r[1], "Grade": r[2], "Performance": r[3]}
            for r in rows
        ]

    @staticmethod
    def merge_sort_list(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = Student.merge_sort_list(data[:mid])
        right = Student.merge_sort_list(data[mid:])
        return Student._merge_values(left, right)

    @staticmethod
    def _merge_values(left, right):
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged

    @staticmethod
    def quick_sort_list(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return Student.quick_sort_list(left) + middle + Student.quick_sort_list(right)

    @staticmethod
    def radix_sort_performance(data):
        mapped = [(Student.PERFORMANCE_ORDER.get(p, 99), p) for p in data]
        max_key = max(mapped, key=lambda x: x[0])[0] if mapped else 0
        buckets = [[] for _ in range(max_key + 1)]
        for key, p in mapped:
            buckets[key].append(p)
        sorted_list = []
        for bucket in buckets:
            sorted_list.extend(bucket)
        return sorted_list

    @staticmethod
    def get_sorted_grades():
        grades = [s["Grade"] for s in Student.get_all_students()]
        return Student.merge_sort_list(grades)

    @staticmethod
    def get_sorted_names():
        names = [s["Name"] for s in Student.get_all_students()]
        return Student.quick_sort_list(names)

    @staticmethod
    def get_sorted_performance():
        perf = [s["Performance"] for s in Student.get_all_students()]
        return Student.radix_sort_performance(perf)

    @staticmethod
    def calculate_mean(values):
        return sum(values) / len(values) if values else None

    @staticmethod
    def calculate_median(values):
        n = len(values)
        if n == 0:
            return None
        sorted_vals = Student.merge_sort_list(values)
        mid = n // 2
        if n % 2 == 1:
            return sorted_vals[mid]
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2

    @staticmethod
    def calculate_mode(values):
        """Compute mode; returns first most frequent or None if empty."""
        if not values:
            return None
        freq = {}
        for v in values:
            freq[v] = freq.get(v, 0) + 1
        max_count = max(freq.values())
        modes = [v for v, c in freq.items() if c == max_count]
        return modes[0]  # return first mode

    @staticmethod
    def sort_students():
        students = Student.get_all_students()
        order_map = {v: i for i, v in enumerate(Student.get_sorted_performance())}
        students.sort(key=lambda x: (order_map.get(x["Performance"], 99), -x["Grade"]))
        return students