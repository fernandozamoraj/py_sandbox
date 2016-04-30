number = 0
step = 2520

for i in range(1,99999999):

    number += step
    tempSum = 0
    for j in range(20, 9, -1):
        if( number % j == 0):
            tempSum += 1

    if tempSum == 10:
        print number
        break
    

       
