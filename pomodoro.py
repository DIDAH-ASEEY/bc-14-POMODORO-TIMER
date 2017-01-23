import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('ANDELA PROJECT', font='starwars'),
       'white', 'on_blue', attrs=['bold'])
cprint(figlet_format('POMODORO',font ='starwars'),'white', 'on_blue',attrs=['bold'])

cprint(figlet_format('TIMER', font = 'starwars'),'white','on_blue',attrs=['bold'])
