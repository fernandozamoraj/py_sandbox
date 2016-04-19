
numbers = [3,1,9,7,8,2,5,6,4,0,11,15,13, 14,21,3]

def get_pivot(mynumbers):
	return  (mynumbers[0]+mynumbers[-1])/2
	
	
def get_left(mynumbers, pivot):
       
    left = []
    
    pivot_nums = []
    for i in range(len(mynumbers)):
        if(mynumbers[i] < pivot):
            left.append(mynumbers[i])
        if(mynumbers[i] == pivot):
            pivot_nums.append(mynumbers[i])        

    #append pivot last        
    for i in pivot_nums:
        left.append(i)            
    return left			

def get_right(mynumbers, pivot):
    right = []
  
    for i in range(len(mynumbers)):
        if(mynumbers[i] > pivot):
            right.append(mynumbers[i])
    
    return right
	
def quick_sort(mynumbers):

    if(len(mynumbers) <= 1):
        return mynumbers;

    proceed = False
    
    #check to see if all numbers are the same
    #for example 3,3,3,3, etc
    if(len(mynumbers) > 1):
        target = mynumbers[0]
        for n in mynumbers:
            if(n != target):
                proceed = True
                break
    
    if(proceed == False):
        return mynumbers
        
    pivot = get_pivot(mynumbers)
    print(pivot)
	
    left_partition = get_left(mynumbers, pivot)
    righ_partition = get_right(mynumbers, pivot)
	
    left_partition = quick_sort(left_partition)
    righ_partition = quick_sort(righ_partition)
	
    for r in righ_partition:
        left_partition.append(r)
	
    print('joined: {0}'.format(left_partition))
    input()
    
    return left_partition
	
numbers = quick_sort(numbers)
	
print(numbers)	
	


	

	
	
	