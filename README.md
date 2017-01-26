# **POMODORO TIMER**
The pomodoro timer is an application that implements the  **_[Pomodoro](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=0ahUKEwiR5NnEpODRAhXLKMAKHQ2nBLQQFgghMAE&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPomodoro_Technique&usg=AFQjCNEcNK-woTV-MpzRR0ilVXA1DnbXxQ&sig2=YF0JzoKcwKKC1LaDWNQsvg)_** technique.
A time management method that uses a timer to break down tasks into intervals "_pomodoros_", usually set at 25 mins each,
separated by short breaks and a long break after a specified number of cycles.

The pomodoro time allows the user to set different times for pomodoros and also assign different values to the short breaks time and the long break time.

# **Getting Started**
The program has been fully developed using **Python** and some of its libraries, while the database implementation uses **SQLITE3**
* Python 2.7
* SQLITE3
* Sublime Text 2

## **Prerequisites**
Below are some of the basic requirements to run the program:
* Python should be installed in your computer, if not do so here _[Python Download](https://tutorial.djangogirls.org/en/python_installation/)_
* Git should be installed in your computer, if not do so here, _[Git Download](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjxsYyak8zRAhWsI8AKHR9YDL4QFggfMAA&url=https%3A%2F%2Fgit-scm.com%2Fdownloads&usg=AFQjCNHZLDrEFiZHXrz1JGq57NFHFrcfkA&sig2=4ht1GzU2s-G7fLM3fuDxYA)_
* A stable internet connection is recommended
* SQLITE3 should be installed, if not, do so on _[SQLITE3](github.com/sqlitebrowser/sqlitebrowser/releases)_
## **Installation**
Follow the following steps to succesfully _**install**_ the program:

1. Run your _Git Bash_ program and enter **`$ cd Desktop`** to place your directory in into desktop folder.
2. Type **`$ git clone https://github.com/DIDAH-ASEEY/bc-14-POMODORO-TIMER`** to clone the repository to your desktop folder.
3. open command prompt and enter **`$ pip install -r requirements.txt`** to install the required packages to run the program.
4. Enter **`$ cd desktop\bc-14-POMODORO-TIMER`** . 
5. Finally enter **`$ python pomodoro.py`** to run the program.

**_NB: This installation steps assumes a windows operating system_**

## The Pomodoro Timer Program
The program displays a list of commands on the interface.

* The user can  _start_ a new task by typing `start <task-title>

 ![start](https://cloud.githubusercontent.com/assets/25131942/22341962/e0091770-e403-11e6-9784-7d16f8f2ce9d.PNG)
 
* The user can _print_ a list of all the task by typing `list_all`

 ![list](https://cloud.githubusercontent.com/assets/25131942/22341939/d5a46c80-e403-11e6-883c-815355e6b851.PNG)
 
* The user can configure the _pomodoros_ of previously done tasks

 ![pomodoro](https://cloud.githubusercontent.com/assets/25131942/22341949/db02ce1a-e403-11e6-9db1-925dfd892ca3.PNG)
 
* The user can configure the _short break_ time of previous tasks

 short](https://cloud.githubusercontent.com/assets/25131942/22341952/dd21886c-e403-11e6-9d43-cd342879231b.PNG)

* The user can configure the _long break_ time of previous tasks

 ![long](https://cloud.githubusercontent.com/assets/25131942/22341943/d825bae0-e403-11e6-8210-9eb0539d6b5f.PNG)
 
* A _sound_ is played at the beginning and end of every pomodoro

* A countdown _display_ pops up when the timer is set

 ![timer](https://cloud.githubusercontent.com/assets/25131942/22342202/97097ec4-e404-11e6-9578-46bcca5a7fbd.PNG)
 







