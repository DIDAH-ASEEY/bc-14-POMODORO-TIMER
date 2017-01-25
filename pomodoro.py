#!/usr/bin/python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    pomodoro start <task-title>
    pomodoro list <date>
    pomodoro list_all
    pomodoro config short_break | long_break | sound
    pomodoro clear
    pomodoro (-i | --interactive)
    pomodoro (-h | --help | --version)
    pomodoro exit

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

Note:
    use interactive for best perfomance
"""

import sys
import os
import cmd
import datetime
import pygame

from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print ('Invalid Command!','red')
            print (e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class MyInteractive(cmd.Cmd):
    cprint(figlet_format('POMODORO TIMER', font='starwars'),
       'white', 'on_blue', attrs=['bold'])

    mainpage = 'WELCOME TO POMODORO TIMER' \
             + """
Usage:
    POMODORO start <task-title>
    POMODORO list <date>            eg. 2016:11:09
    POMODORO list_all
    POMODORO delete_all
    POMODORO config <command>       eg. short_break, long_break, sound
    POMODORO (-i | --interactive)
    POMODORO (-h | --help)
    POMODORO exit

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
    prompt = 'Enter a command: POMODORO  '
    file = None
    

    def do_exit(self, arg):
        """Usage: exit"""
        print "CLOSSING APPLICATION!....."
        
        exit()

    @docopt_cmd
    def do_start(self, arg):
        """Usage: start <task-title>"""
        try:
            add_task.new(arg['<task-title>'])
        except KeyboardInterrupt:
            pygame.quit()
            print ('\nTASK ACCOMPLISHED')

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list <date>"""
        list_day(arg['<date>'])

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_all"""
        configurations.list_all()

    
