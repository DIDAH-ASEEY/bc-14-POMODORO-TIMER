
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
        print "***DEFAULT SETTINGS SET*** "
        

        duration = "01:00:00"
        pomodoro_time = "00:25:00"
        short_break = "00:05:00"
        long_break = "00:15:00"
        sound = True

    elif data == 'set':
        duration  = configurations.set_total_taskTime()
        pomodoro_time = configurations.set_time()
        short_break = configurations.set_short_break()
        long_break = configurations.set_long_break()
        sound = configurations.set_sound()
        


    else:
        print "INVALID INPUT! try again"
        return new(title)
    day = time.time()

    timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y/%m/%d"))

    cycles = cycle(duration, pomodoro_time)

    print "**CONFIGURATIONS SETTINGS**"
    print "TASK TIME:        %s"%duration
    print "POMODORO TIME:    %s"%pomodoro_time
    print "SHORT BREAK TIME: %s"%short_break
    print "LONG BREAK TIME:  %s"%long_break
    print "SOUND : %s " %sound
    print "CYCLES: %s "%cycles
    print "TIMESTAMP:        %s" %timestamp

    database.data_input(title,timestamp,pomodoro_time,cycles,short_break, long_break,sound)

    
        
        
        
        

