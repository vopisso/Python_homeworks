import sqlite3


def sql_insert_line_to_schedule():

    line = []
    line.append(input('Enter id: '))
    line.append(input("Enter class number: "))
    line.append(input("Enter lesson number: "))
    line.append(input("Enter starting lesson time: "))
    line.append(input("Enter ending lesson time: "))
    line.append(input("Enter subject: "))
    line = tuple(line)
    con = sqlite3.connect('F:/GB/Courses/Python1/Homeworks/HW8/school_info_system.db')
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO schedule(id, class_number, lesson_number, start_lesson, end_lesson, subject) select * from (VALUES(?, ?, ?, ?, ?, ?)) alias', line)

    con.commit()
    con.close()


def sql_insert_line_to_teachers():

    line = []
    line.append(input('Enter id: '))
    line.append(input("Enter teacher's name: "))
    line.append(input("Enter teacher's phone number: "))
    line.append(input("Enter teacher's subject: "))
    line.append(input("Enter teacher's entering time: "))
    line.append(input("Enter teacher's exiting time: "))
    line = tuple(line)
    con = sqlite3.connect('F:/GB/Courses/Python1/Homeworks/HW8/school_info_system.db')
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO teachers(id, name, phone_num, subject, enter_time, exit_time) select * from (VALUES(?, ?, ?, ?, ?, ?)) alias', line)

    con.commit()
    con.close()


def sql_print_schedule():
    con = sqlite3.connect('F:/GB/Courses/Python1/Homeworks/HW8/school_info_system.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM schedule')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)
    con.close()


def sql_print_teachers():
    con = sqlite3.connect('F:/GB/Courses/Python1/Homeworks/HW8/school_info_system.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM teachers')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)
    con.close()


def print_all_tables():
    con = sqlite3.connect('F:/GB/Courses/Python1/Homeworks/HW8/school_info_system.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())
    con.close()
