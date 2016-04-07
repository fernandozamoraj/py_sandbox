from random import randint
import time

while(True):
    line = ''
    for i in range(0, 70):
        line = line +  chr(randint(65,127))
    time.sleep(1)
    print(line)

    