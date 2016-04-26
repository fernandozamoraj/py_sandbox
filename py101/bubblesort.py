mylist = [1,5,8,23,5,8,7,1]
swap_c = 0

for i in range(0, len(mylist)):
    for j in range(0, len(mylist)-i-1):
        swap_c += 1
        if(mylist[j] > mylist[j+1]):
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                #swap_c += 1
                
              
print(mylist)              
print('swap count: {0}'.format(swap_c))