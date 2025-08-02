import sqlite3
import os


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    ''')

    cursor.execute('''
    CREATE TABLE Courses (
        id INTEGER PRIMARY KEY,
        course_name VARCHAR NOT NULL,
        instructor TEXT,
        credits INTEGER)
    ''')


def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]

    courses = [
        (1, 'Python Programming', "Dr. Anderson", 3),
        (2, 'Web Development', "Prof. Wilson", 4),
        (3, 'Data Science', "Dr. Taylor", 3),
        (4, 'Mobile Apps', "Prof. Garcia", 2),
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)
    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Sample data inserted successfully")


def basic_sql_operations(cursor):
    # Select All
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()

    for row in records:
        print(row)


def sql_update_insert_delete_operations(conn, cursor):
    # 1) Insert
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com', 'Miami')")
    conn.commit()

    # 2) Update
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    # 3) Delete
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()


def aggregate_functions(cursor):
    # 1) Count
    print("***** Count *****")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 2) Average
    print("***** Average *****")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])


def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_insert_delete_operations(conn, cursor)
        aggregate_functions(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
