import pyodbc

# إنشاء الاتصال بقاعدة البيانات
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=student;'
    'Trusted_Connection=yes;'
)

cursor = connection.cursor()

# إدخال بيانات جديدة في الجدول
cursor.execute('''DELETE FROM student_table;''')
# cursor.execute('DELETE FROM student_table WHERE name = ?', ('saher',))

connection.commit()

# استرجاع وعرض جميع البيانات من الجدول
cursor.execute('''SELECT grade FROM student_table''')
print("All records in student_table:")
grades = cursor.fetchall()
print(grades)

# إغلاق الاتصال
connection.close()


