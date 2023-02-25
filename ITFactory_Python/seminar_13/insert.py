import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

cursor.execute("INSERT INTO Students (name, email, age) VALUES ('adam', 'adam@g.com', 28)")
cursor.execute("INSERT INTO Students (name, email, age) VALUES ('eva', 'eva@g.com', 22)")

cursor.execute("SELECT * FROM Students")
pprint(cursor.fetchall())

grades_values = [
	("WEB DEV", 8, 1),
	("WEB DEV", 7, 2),
	("DB DEV", 10, 1),
	("DB DEV", 8, 1),
	("DB DEV", 6, 2),
	("Front End", 8, 2),
	("Front End", 10, 1),
	("Front End", 5, 1),
]
SQL_query = "INSERT INTO Grades (topic, grade, student_id) VALUES (?,?,?)"
cursor.executemany(SQL_query, grades_values)

cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())

con.commit()