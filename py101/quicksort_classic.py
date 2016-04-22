#numbers = [5,3,7,12,4,5,3,7,12,4,67,45,12,23,78,90,1,2,45]
numbers = [1,2,3,4,5,6,7,8,9,10]
#numbers = [1,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9,10,2,8,4,6,5,3,7,9]

qs_count = 0
swap_count = 0

def quick_sort(target_list, start, end):
    global qs_count

    if(start >= end):
        return
		
    qs_count += 1    
    print('list: {0}'.format(target_list))
    pivot_index = partition(target_list, start, end)
    
    if(start < pivot_index - 1):
        quick_sort(target_list, start, pivot_index-1)

    if(pivot_index < end):
        quick_sort(target_list, pivot_index, end)

def compare(x, y):
    return y - x		
		
def partition(target_list, start, end):

    global swap_count
	
    pivot = target_list[int((start + end) / 2)]
    i = start
    j = end
	
    while(i <= j):
        while(compare(target_list[i], pivot) > 0):
            i += 1
        while(compare(target_list[j], pivot) < 0):
            j -= 1
        
        if(i <= j):
            if(i != j):		
                target_list[i], target_list[j] = target_list[j], target_list[i]
                swap_count += 1			

            i += 1
            j -= 1
            
    return i			
    
def compare(x, y):
    return x - y
    
print('len(numbers): {0}'.format(len(numbers)))  
print(numbers)        
quick_sort(numbers, 0, len(numbers)-1)
print(numbers)	
print('quick_sort count: {0}'.format(qs_count))
print('swap count: {0}'.format(swap_count))
