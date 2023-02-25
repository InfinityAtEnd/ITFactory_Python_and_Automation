import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

cursor.executescript("""
	CREATE TABLE if not exists Students  (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		email TEXT,
		age INTEGER CHECK(age > 18) 
		);
	CREATE TABLE if not exists Grades (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		topic TEXT,
		grade INTEGER NOT NULL CHECK(grade > 0 and grade <= 10),
		student_id INTEGER NOT NULL,
		FOREIGN KEY (student_id) REFERENCES Students(id)		
	);
	""")

cursor.execute("SELECT * FROM Students")
pprint(cursor.fetchall())