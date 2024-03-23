# takeTime.py
import sys
import os
from time import sleep
import pyfiglet
from argToTime import argToTime

time = int(sys.argv[1])

try:
    print(pyfiglet.figlet_format(f'Taking  {time}'))
    sleep(5)
    
    argToTime(time)


except:
    print("No command line arguments passed")
    print("Example: 'python takeTime.py 5'")
    print("The argument must be a integer")
