import sqlite3

conn = sqlite3.connect("bmi_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM bmi_records")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()