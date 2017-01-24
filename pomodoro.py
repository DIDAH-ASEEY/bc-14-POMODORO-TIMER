#!/usr/bin/python

import sys
import os
import cmd
import datetime
import pygame

from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit

cprint(figlet_format('ANDELA PROJECT', font='starwars'),
       'white', 'on_blue', attrs=['bold'])



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

            print colored('Invalid Command!','red')
            print(e)
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

    mainpage = 'Welcome to pomodoro timer!' \
            + ' (type help for a list of commands.)' + """
Usage:
    pomodoro start <task>
    pomodoro list <date>            eg. 2016:11:09
    pomodoro list_all
    pomodoro delete_all
    pomodoro config <command>       eg. short_break, long_break, sound
    pomodoro (-i | --interactive)
    pomodoro (-h | --help)
    pomodoro exit

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
    prompt = 'enter a command:  '
    file = None
    
