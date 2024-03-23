import os
import pyfiglet
from time import sleep


def argToTime(t):
    os.system('clear')

    minutes = t - 1
    seconds = 59

    for i in range(seconds):
        os.system('clear')

        if minutes < 10 and seconds < 10:
            currentTime = pyfiglet.figlet_format(f'0{minutes} : 0{seconds}')
            print(currentTime)
        elif minutes < 10:
            currentTime = pyfiglet.figlet_format(f'0{minutes} : {seconds}')
            print(currentTime)
        elif seconds < 0:
            currentTime = pyfiglet.figlet_format(f'{minutes} : 0{seconds}')
            print(currentTime)
        else:
            currentTime = pyfiglet.figlet_format(f'{minutes} : {seconds}')
            print(currentTime)

        seconds -= 1

        if seconds == 1:
            minutes -= 1
            seconds = 59

        sleep(1)

    os.system('clear')

    print(pyfiglet.figlet_format('END'))
    print(pyfiglet.figlet_format('Time To Go Back To Work'))
