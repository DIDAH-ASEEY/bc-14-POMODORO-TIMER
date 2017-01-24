import sys
import sqlite3
import configurations

def create_table():
    conn = sqlite3.connect('pomodoro_timer.db')
    c = conn.cursor()



