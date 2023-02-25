import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

SQL_query = "SELECT * FROM Students as s JOIN Grades g ON s.id=g.student_id WHERE s.name=?"
cursor.execute(SQL_query, ('eva',))


pprint(cursor.fetchall())

# numele, topicul si nota pentru studentul adam
print(60 * "*")

SQL_query = "SELECT s.name, g.topic, g.grade FROM Students as s JOIN Grades g ON s.id=g.student_id WHERE s.name=?"
cursor.execute(SQL_query, ('adam',))


pprint(cursor.fetchall())
print(60 * "*")