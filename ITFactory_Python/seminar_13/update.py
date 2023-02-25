import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

SQL_query = "UPDATE Grades SET grade=? WHERE student_id=? AND topic=? AND grade=?"
cursor.execute(SQL_query,(2, 1, "DB DEV", 10))
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())
con.commit()