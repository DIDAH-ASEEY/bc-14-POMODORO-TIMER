import sys
import sqlite3
import configurations

def create_table():
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()

    print "succesfully connected"

    conn.execute('''CREATE TABLE POMODORO_TIMER
       (ID INT PRIMARY KEY     NOT NULL,
       TASK_TITTLE     TEXT    NOT NULL,
       TIMESTAMP       TEXT    NOT NULL,
       CYCLES          INT,
       SHORT_BREAK     TEXT,
       LONG_BREAK      TEXT,
       TOTAL_DURATION  TEXT,
       SOUND           INT);''')

    print "table created successfully"

create_table()

    



