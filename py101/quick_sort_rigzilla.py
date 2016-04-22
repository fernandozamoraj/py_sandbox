quicksort_count = 0

def partitioning(lt, start, end):
    '''
    selects a pivot, puts all members lesser than the pivot to the left,
    and all members greater than the pivot to the right
    '''
    
    global quicksort_count
    quicksort_count += 1
    
    #pick end of the list as pivot
    pivot = lt[end]
    #initiate an iterator
    pIndex = start
    #iterate through list
    for i in range(start, end):
    	#if the member, we're looking at is lesser than or equal to the pivot
        if lt[i] <= pivot:
        	#-> swap it with the iterator
            lt[i], lt[pIndex] = lt[pIndex], lt[i]
            #raise iterator by one
            pIndex += 1

    #swap pivot with the index where the iterator has stoppped, to put it in the middle
    lt[pIndex], lt[end] = lt[end], lt[pIndex]
    #return the middle
    return pIndex


def quicksort(lt, start, end):
    
    '''
    recursive function that calls partinioning to sort a list
    of ints from lowest to greatest member
    '''

    
    #if list has more than two members and members are valid
    if start < end:
        
    	#partition list and get middle
        pIndex = partitioning(lt, start, end)
        #recursive call on first half of partinioned list
        quicksort(lt, start, pIndex-1)
        #recursive call on second half of partinioned list
        quicksort(lt, pIndex+1, end)
        #return lt

#usage:
#example list
lt = [5,2,7,0,3,6,1,4]
#print before sorting
print (lt)
#sort example lsit
quicksort(lt, 0, len(lt)-1)
#print sorted list
print (lt)

print('count: {0}'.format(quicksort_count))