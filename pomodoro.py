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
import configurations
import add_task
import sound
import database
import timer_display

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
    cprint(figlet_format('POMODORO  *TIMER*', font='epic'),
       'red', attrs=['bold'])

    intro ='WELCOME TO POMODORO TIMER' \
             + """
Usage:
    POMODORO start <task-title>
    POMODORO list <date>            eg. yy/mm/dd
    POMODORO list_all
    POMODORO delete_all
    POMODORO config <command>       eg. short_break, long_break, sound, pomodoro_time
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
        print "CLOSING APPLICATION!....."
        
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
        database.list_day(arg['<date>'])

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_all"""
        database.list_all()

    @docopt_cmd
    def do_config(self, args):
        """Usage: config <cmmand>"""
        if args['<command>'] == 'short_break':
            database.set_shortBreak_db()
        elif args['<command>'] == 'long_break':
            database.set_longBreak_db()
        elif args['<command>'] == 'sound':
            database.set_sound_db()
        elif args['<command>'] == 'pomodoro_time':
            database.set_pomodoro_db()
        
               

    @docopt_cmd
    def do_delete_all(self,arg):
        """Usage: delete_all"""
        database.delete_list()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        # print (__doc__)
        MyInteractive().cmdloop()
    except KeyboardInterrupt:
        print "\n"

    
