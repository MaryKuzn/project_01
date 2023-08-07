### Задача 4.1.
## В базе данных teacher создайте таблицу Students
#import sqlite3
#connection = sqlite3.connect("teacher.db")
#cursor = connection.cursor()
#query = """Create table Students (Student_Id Integer Not Null,
#Student_Name Text Not Null,
#School_Id Integer Not Null Primary key)""" 
#cursor.execute(query)
#connection.commit()
#connection.close()

#connection = sqlite3.connect("teacher.db")
#cursor = connection.cursor()
#query = """Insert into Students (Student_Id,Student_Name,School_Id) 
#Values (201, 'Иван', 1), (202, 'Петр', 2), (203, 'Анастасия', 3), (204, 'Игорь', 4)"""
#cursor.execute(query)
#connection.commit()
#connection.close()


###Решение с помощью 2 функций:
import sqlite3

def get_connection():
  connection = sqlite3.connect("teacher.db")
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * from School WHERE School_Id = ?"
    cursor.execute(sql_query,(school_id,))
    info = cursor.fetchone()
    close_connection(connection)
    return info[1]
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных", error) 

def stud_info(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * from Students WHERE Student_Id = ?"
    cursor.execute(sql_query,(student_id,))
    name = cursor.fetchall()
    close_connection(connection)
    print("Информация o школе и студентах")
    for row in name:
      print("ID Студента:", row[0])
      print("Имя студента:", row[1])
      print("ID школы:", row[2])
      print("Название школы:", school_name(row[2]))
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных", error)  
stud_info(203)

###Решение с помощью join:

import sqlite3

def get_connection():
  connection = sqlite3.connect("teacher.db")
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def join_stud(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * from Students JOIN School ON Students.School_Id = School.School_Id WHERE Students.Student_Id = ?"
    cursor.execute(sql_query,(student_id,))
    list = cursor.fetchall()
    close_connection(connection)
    print("Информация o школе и студентах")
    for row in list:
      print("ID Студента:", row[0])
      print("Имя студента:", row[1])
      print("ID школы:", row[2])
      print("Название школы:", row[4])
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных", error)  
join_stud(203)    
