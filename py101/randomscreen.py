from random import randint
import time
import pdb


def do_random_screen():
    result = 1
    while(True):
        result += 1
        line = ''
        for i in range(0, 70):
           line = line +  chr(randint(65,127))
        time.sleep(1)
        print(line)
        if(result == 30):
            break;
        pdb.set_trace()
            
    return result

if(__name__=='__main__'):
    x = do_random_screen()
    print(x) 
        
    

_
