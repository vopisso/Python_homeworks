import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('F:/GB/Courses/Python1/Homeworks/HW8/school_info_system.db')

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        'create table if not exists teachers(id integer PRIMARY KEY, name text, phone_num text, subject text, enter_time text, exit_time text)')

    con.commit()


con = sql_connection()
sql_table(con)