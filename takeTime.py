# takeTime.py
import sys
import os
from time import sleep

def argToTime(t):
    os.system('clear')

    minutes = t - 1
    seconds = 59

    for i in range(seconds):
        os.system('clear')

        if minutes < 10 and seconds < 10:
            print(f'0{minutes}:0{seconds}')
        elif minutes < 10:
            print(f'0{minutes}:{seconds}')
        elif seconds < 0:
            print(f'{minutes}:0{seconds}')
        else:
            print(f'{minutes}:{seconds}')


        seconds -= 1

        if seconds == 0:
            minutes -= 1
            seconds = 59

        elif minutes == 0 and seconds == 0:
            print('END')

            minutes = 0
            seconds = 0

        sleep(1)


time = int(sys.argv[1])

try:
    print(f'Taking {time}')
    sleep(2)
    
    argToTime(time)


except:
    print("No command line arguments passed")
    print("Example: 'python takeTime.py 5'")
    print("The argument must be a integer")
