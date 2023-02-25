import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM Students")
# pprint(cursor.fetchall())
print(60 * "*")
pprint(cursor.fetchone())
pprint(cursor.fetchone())
pprint(cursor.fetchone())
print(60 * "*")

cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchmany(3))
pprint(cursor.fetchone())
print(60 * "*")

cursor.execute("SELECT topic, grade FROM Grades")
pprint(cursor.fetchall())


print(60 * "*")
cursor.execute("SELECT * FROM Grades WHERE topic=?", ('DB DEV',))
pprint(cursor.fetchall())


print(60 * "*")
# numele si emailul tuturor studentilor cu varsta mai mica decat 26
cursor.execute("SELECT name, email FROM Students WHERE age<26")
pprint(cursor.fetchall())


print(60 * "*")