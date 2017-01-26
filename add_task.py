import timer_display
import datetime
import time
import database
import configurations
import alarm


def cycle(duration, pomodoro_time):
    total_time = timer_display.seconds(duration)
    task_time = timer_display.seconds(pomodoro_time)

    if total_time < task_time:
        num_cycles = 1

    else:
        num_cycles = total_time / task_time

    return num_cycles


def new(title):
    print " **POMODORO TIME CONFIGURATION** "
    print
    data = (raw_input(
        "ENTER 'set' TO CONFIGURE THE TIME OR PRESS <ENTER> TO PROCEED WITH DEFAULT SETTINGS => ")).lower()

    if data == '':
        print "***DEFAULT SETTINGS SET*** "

        duration = "01:00:00"
        pomodoro_time = "00:25:00"
        short_break = "00:05:00"
        long_break = "00:15:00"
        sound = True

    elif data == 'set':
        duration = configurations.set_total_taskTime()
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
    print "TASK TIME:        %s" % duration
    print "POMODORO TIME:    %s" % pomodoro_time
    print "SHORT BREAK TIME: %s" % short_break
    print "LONG BREAK TIME:  %s" % long_break
    print "SOUND : %s " % sound
    print "CYCLES: %s " % cycles
    print "TIMESTAMP:        %s" % timestamp

    database.data_input(title, timestamp, pomodoro_time,
                        (cycles + 1), short_break, long_break, sound)

    num = 0
    break_point = ''
    display = timer_display.display_box(pomodoro_time, title)
    SB_display = timer_display.display_box(short_break, "SHORT BREAK")
    LB_display = timer_display.display_box(long_break, "LONG BREAK")

    while cycles > num:
        count = 3
        while count > 0 and cycles > num:
            num += 1
            status = display
            if sound == True:
                alarm.end_sound()
            SB_display
            alarm.end_sound()
            count -= 1
            num += 1
        display
        if sound == True:
            alarm.end_sound()
        LB_display
        alarm.end_sound()

        num += 1
        count -= 1
