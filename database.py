import sys
import sqlite3
import configurations

def create_table():
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()

    print "succesfully connected"

    conn.execute('''CREATE TABLE POMODORO_TIMER IF NOT EXISTS
       (ID INT PRIMARY KEY     NOT NULL,
       TASK_TITTLE     TEXT    NOT NULL,
       TIMESTAMP       TEXT    NOT NULL,
       
       SHORT_BREAK     TEXT,
       LONG_BREAK      TEXT,
       POMODORO_TIME   TEXT,
       CYCLES          INT,
       SOUND           INT);''')

    conn.commit()                               #commits the current transaction to enable visibilit of changes to other database connections
    c.close()


def data_input(task_title, timestamp, pomodoro_time, cycles,SB,LB,sound):
    conn = sqlite.connect('database.db')
    c = conn.cursor()

    c.execute(" INSERT INTO POMODORO_TIMER (TASK_TITTLE, TIMESTAMP , SHORT_BREAK, LONG_BREAK,POMODORO_TIME,CYCLES, SOUND ) VALUES(?,?,?,?,?,?,?)",
              (tast_tittle, time_stamp, SB, LB, pomodoro_time, cycles,sound))
    
    conn.commit()
    
    c.close()


def delete_list():
    conn = sqlite3.connect('database.db')

    c = conn.cursor()
    c.execute("DELETE from POMODORO_TIMER")

    print "Total Number of rows deleted => %s" %conn.total_changes

    conn.commit()
    c.close()


    



    
