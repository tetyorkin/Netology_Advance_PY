import datetime as dt

import psycopg2 as pg

conn = pg.connect(dbname='netology_db', user='netology_user', password='123456')
cur = conn.cursor()
student_1 = {'name': 'Маша', 'gpa': 4, 'birth': dt.datetime(2005, 7, 14)}
student_2 = {'name': 'Smith', 'gpa': 5, 'birth': dt.datetime(2004, 3, 4)}
student_3 = {'name': 'Bond', 'gpa': 3, 'birth': dt.datetime(2004, 6, 30)}

list_student = [
    {'name': 'Маша_2', 'gpa': 4, 'birth': dt.datetime(2005, 8, 10)},
    {'name': 'Даша', 'gpa': 4.7, 'birth': dt.datetime(2004, 6, 16)},
    {'name': 'Глаша', 'gpa': 4.8, 'birth': dt.datetime(2002, 6, 25)},
    {'name': 'Наташа', 'gpa': 4.1, 'birth': dt.datetime(2001, 3, 8)},
    {'name': 'Саша', 'gpa': 5, 'birth': dt.datetime(2004, 9, 1)}
]


# Функция добавяет список студентов в таблицу Student и записывает их на id курса
def add_students(course_id, students):
    cur.execute("""
            INSERT INTO Course
            VALUES (default, %s);
    """, (course_id))
    conn.commit()
    for student in students:
        name = student['name']
        gpa = student['gpa']
        birth = student['birth']
        cur.execute("""
                INSERT INTO Student(name, gpa, birth)
                values(%s, %s, %s);
        """, (name, gpa, birth))
        conn.commit()

        cur.execute("""
                SELECT id
                FROM Student
                WHERE name=%s;
        """, (name,))
        fetch = cur.fetchall()

        cur.execute("""
                INSERT INTO Course_name
                VALUES (default, %s, %s);
        """, (fetch[0], course_id))

        conn.commit()



# Функция возвращает именя студентов учащихся на конкретном id курса
def get_students(course_id):
    cur.execute("""
                SELECT name 
                FROM Student
                INNER JOIN Course_name
                ON student.id=course_name.student_id
                WHERE course_name.course_id=%s;
            """, course_id)
    print(cur.fetchall())


# Функция возвращает имя студента по его id
def get_student(student_id):
    cur.execute("""
            SELECT name 
            FROM Student
            WHERE id=%s;
        """, student_id)
    print(cur.fetchall())


# Функция создания студента, аргументом отправляем заранее сформированный словарь
def add_student(student):
    name = student['name']
    gpa = student['gpa']
    birth = student['birth']
    cur.execute("""
        INSERT INTO Student(name, gpa, birth)
        values(%s, %s, %s);
    """, (name, gpa, birth))
    conn.commit()


# Функция создания таблиц Student и Course
def create_db():
    cur.execute("""
        CREATE TABLE if not exists Student(
        id serial PRIMARY KEY not null,
        name varchar(100) not null,
        gpa numeric(10,2),
        birth timestamp with time zone 
        );
        CREATE TABLE if not exists Course(
        id serial PRIMARY KEY not null,
        name varchar(100) not null
        );        
        CREATE TABLE if not exists Course_name(
        id serial PRIMARY KEY not null,
        student_id INTEGER REFERENCES student(id),
        course_id INTEGER REFERENCES course(id)
        );
    """)
    conn.commit()


# Функция очистки от таблиц
def delete_db():
    cur.execute("""
         DROP TABLE Course_name;
         DROP TABLE Student;
         DROP TABLE Course;
     """)
    conn.commit()


if __name__ == '__main__':
    create_db()
    add_student(student_1)
    add_student(student_2)
    get_student('1')
    get_student('2')
    add_students('1', list_student)
    get_students('1')
