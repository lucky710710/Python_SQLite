# Import the SQLite library 
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('course_enrollment.db')

# Create a cursor object to interact with database
cursor = connection.cursor()

# Create the 'course_enrollment' table
cursor.execute('''CREATE TABLE IF NOT EXISTS course_enrollment (
                    EnrollmentID INTEGER PRIMARY KEY,
                    StudentName TEXT NOT NULL,
                    CourseName TEXT NOT NULL,
                    Progress TEXT,
                    Status TEXT)''')

# Insert a single record
cursor.execute("INSERT INTO course_enrollment (StudentName, CourseName, Progress, Status) VALUES ('Lalith Kumar', 'Artificial Intelligence', '75%', 'In Progress')")

# Insert multiple records using parameterized queries
students_data = [
    ('Yashwanth Kuntla', 'Data Science', '100%', 'Completed'),
    ('Kranti Jaddu', 'Machine Learning 201', '50%', 'In Progress'),
    ('Raj Tharun', 'Web Development', '100%', 'Completed')
]

# Insert each record into the table
for student in students_data:
    cursor.execute("INSERT INTO course_enrollment (StudentName, CourseName, Progress, Status) VALUES (?, ?, ?, ?)", student)

# Query the database
cursor.execute("SELECT * FROM course_enrollment")
rows = cursor.fetchall()

# Print the records from the course_enrollment table
print("Records in the 'course_enrollment' table:")
for row in rows:
    print(row)

# Querying a table that doesn't exist
try:
    cursor.execute("SELECT * FROM database")  # Non-existing table
except sqlite3.OperationalError as e:
    print(f"\nAn error occurred: {e}")    

# Commit the changes to database
connection.commit()

# Close the connection
connection.close()