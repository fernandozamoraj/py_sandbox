quick_sort_count = 0

def partition(targetlist, start, end):

    pivot = targetlist[end]
    partition_index = start
	
    for i in range(start, end):
        if(targetlist[i] <= pivot):
            temp = targetlist[i]
            targetlist[i] = targetlist[partition_index]
            targetlist[partition_index] = temp
            partition_index += 1 			
    
    temp = targetlist[end]
    targetlist[end] = targetlist[partition_index]
    targetlist[partition_index] = temp
	
    return partition_index
    
	
	
def quick_sort(targetlist, start, end):
    global quick_sort_count
    
    print(targetlist)
    quick_sort_count += 1
    if(start < end):
        pivot_index = partition(targetlist, start, end)
        quick_sort(targetlist, start, pivot_index-1)
        quick_sort(targetlist, pivot_index+1, end)
		
		
numbers = [30, 10, 11, 45, 1, 50, 10, 11, 45, 1, 50, 10, 11, 45, 1, 50, 10, 11, 45, 1, 50, 10, 11, 45, 1, 50, 10, 11, 45, 1, 50]

print(numbers)
quick_sort(numbers, 0, len(numbers)-1)
print(numbers)
print('count: {0}'.format(quick_sort_count))    
