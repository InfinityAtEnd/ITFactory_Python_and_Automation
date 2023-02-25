import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

print(60 * "*")

# :topic and :id - are beeing taken from a dictionary
SQL_query = "DELETE FROM Grades WHERE topic=:topic AND student_id=:id"
values = {
	'id': 1,
	'topic': 'DB DEV'
}
cursor.execute(SQL_query, values)
pprint(cursor.fetchall())
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())
con.commit()