import sys
import sqlite3
import configurations
from prettytable import PrettyTable as table




def create_table():
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()

    print "succesfully connected"

    conn.execute('''CREATE TABLE pomodoro 
       (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
       TASK_TITTLE     TEXT    NOT NULL,
       TIMESTAMP       TEXT    NOT NULL,
       
       SHORT_BREAK     TEXT,
       LONG_BREAK      TEXT,
       POMODORO_TIME   TEXT,
       CYCLES          INT,
       SOUND           INT )''')

    conn.commit()                               #commits the current transaction to enable visibilit of changes to other database connections
    c.close()


def data_input(task_title, timestamp, pomodoro_time, cycles,SB,LB,sound):
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()

    c.execute(" INSERT INTO pomodoro (TASK_TITTLE, TIMESTAMP , SHORT_BREAK, LONG_BREAK,POMODORO_TIME,CYCLES, SOUND ) VALUES(?,?,?,?,?,?,?)",
              (task_title, timestamp, SB, LB, pomodoro_time, cycles,sound))
    
    conn.commit()
    
    c.close()


def delete_list():
    conn = sqlite3.connect('pomodoro_timer.db')

    c = conn.cursor()
    c.execute("DELETE from pomodoro")

    print "TOTAL NUMBER OF ROWS DELETED => %s" %conn.total_changes
    print

    conn.commit()
    c.close()


def list_all():
    
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM pomodoro''')

    data = c.fetchall()

    print "LIST OF ALL TASKS"

    tasks_list = table(['ID','TASK TITLE', 'DATE','POMODORO TIME','CYCLES'])
    

    for row in data:
        id = str(row[0])
        title = str(row[1])
        date = str(row[2])
        time = str(row[3])
        cycles = str(row[6])

        tasks_list.add_row([id,title, date, time,cycles])

    print tasks_list
    c.close()

def list_day(timestamp):
    
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Pomodoro WHERE TIMESTAMP = ?;", (timestamp,))

    data = c.fetchall()

    print "LIST OF TASKS"

    tasks_list = table(['ID','TASK TITLE', 'DATE','POMODORO TIME','CYCLES'])
    

    for row in data:
        id = str(row[0])
        title = str(row[1])
        date = str(row[2])
        time = str(row[3])
        cycles = str(row[6])

        tasks_list.add_row([id,title, date, time,cycles])

    print tasks_list
    c.close()



def set_shortBreak_db():
    
    list_all()
    print
    print "SHORT BREAK SETTINGS"
    task_id = input("ENTER THE TASK ID FOR TASK TO EDIT => ")
    
    time = configurations.set_short_break()

    conn = sqlite3.connect("pomodoro_timer.db")
    c = conn.cursor()
    c.execute("UPDATE pomodoro SET SHORT_BREAK = '%s' WHERE ID = '%s' " %(time, task_id))
    conn.commit()
    c.close()

              


def set_longBreak_db():
    list_all()
    print
    print "LONG BREAK SETTINGS"
    task_id = input('ENTER THE TASK ID FOR TASK TO EDIT => ')
    time = configurations.set_long_break()

    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()
    c.execute("UPDATE pomodoro SET LONG_BREAK = '%s' WHERE ID ='%s' " %(time,task_id))
    conn.commit()
    c.close()


def set_sound_db():
    list_all()
    print
    print "SOUND SETTINGS"
    task_id = input("ENTER THE TASK ID FOR TASK TO EDIT => ")

    sound = configurations.set_sound()
    conn = sqlite3.connect("pomodoro_timer.db")
    c = conn.cursor()
    c.execute("UPDATE pomodoro SET SOUND='%s' WHERE ID='%s' " %(sound,task_id))
    conn.commit()
    c.close()    

def set_pomodoro_db():
    list_all()
    print
    print "CYCLE TIME SETTINGS"
    task_id = input("ENTER THE TASK ID FOR TASK TO EDIT => ")

    sound = configurations.set_time()
    conn = sqlite3.connect("pomodoro_timer.db")
    c = conn.cursor()
    c.execute("UPDATE pomodoro SET POMODORO_TIME='%s' WHERE ID='%s' " %(sound,task_id))
    conn.commit()
    c.close()

    

    


        
        
        
        
        
        

    
    

    
    



    
