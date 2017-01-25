import sys
import os
import timer_display
import datetime
import time

def cycle(duration, pomodoro_time):
    total_time = timer_display.seconds(duration)
    task_time = timer_display.seconds(pomodoro_time)

    
    if total_time < task_time:
        num_cycles = 1

    else:
        num_cycles = total_time/task_time

    return num_cycles
