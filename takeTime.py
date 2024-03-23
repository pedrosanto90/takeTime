# takeTime.py
import sys
import os
from time import sleep

try:
    time = int(sys.argv[1])
    print(f'Taking {time}')
    sleep(2)

    for i in range(time):
        os.system('clear')

        actualTime = time - i
        print(actualTime)
        sleep(1)

except:
    print("No command line arguments passed")
    print("Example: 'python takeTime.py 5'")
    print("The argument must be a integer")
