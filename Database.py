import sqlite3


def create_database():

    conn = sqlite3.connect("bmi_data.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_record(name, age, gender, weight, height, bmi, category):

    conn = sqlite3.connect("bmi_data.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bmi_records
    (name, age, gender, weight, height, bmi, category)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, weight, height, bmi, category))

    conn.commit()
    conn.close()


def get_all_records():

    conn = sqlite3.connect("bmi_data.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bmi_records")

    records = cursor.fetchall()

    conn.close()

    return records

def get_bmi_data():

    conn = sqlite3.connect("bmi_data.db")

    cursor = conn.cursor()

    cursor.execute("SELECT name, bmi FROM bmi_records")

    data = cursor.fetchall()

    conn.close()

    return data