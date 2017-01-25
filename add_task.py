
import timer_display
import datetime
import time
import database
import configurations


def cycle(duration, pomodoro_time):
    total_time = timer_display.seconds(duration)
    task_time = timer_display.seconds(pomodoro_time)

    
    if total_time < task_time:
        num_cycles = 1

    else:
        num_cycles = total_time/task_time

    return num_cycles
def new(title):
    print " **POMODORO TIME CONFIGURATION** "
    print
    data = (raw_input("ENTER 'set' TO CONFIGURE THE TIME OR PRESS <ENTER> TO PROCEED WITH DEFAULT SETTINGS => ")).lower()

    if data == '':
        print "**DEFAULT SETTINGS SET** "
        print "TASK TIME:        01:00:00"
        print "POMODORO TIME:    00:15:00"
        print "SHORT BREAK TIME: 00:05:00"
        print "LONG BREAK TIME:  00:08:00"
        print "SOUND : True"

        duration = "00:45:00"
        pomodoro_time = "00:15:00"
        short_break = "00:05:00"
        long_break = "00:08:00"
        sound = True

    elif data == 'set':
        duration  = configurations.set_total_taskTime()
        pomodoro_time = configurations.set_time()
        short_break = configurations.set_short_break()
        long_break = configurations.set_long_break()
        sound = configurations.set_sound()
        print "**CONFIGURATIONS SET**"
        print "TASK TIME:        %s"%duration
        print "POMODORO TIME:    %s"%pomodoro_time
        print "SHORT BREAK TIME: %s"%short_break
        print "LONG BREAK TIME:  %s"%long_break
        print "SOUND : %s "%sound


    else:
        print "INVALID INPUT! try again"
        return new(title)

    day = str(datetime.         
        
        
        
        

