
def reverse(items):
    reverseList = []
	
    itemSize = len(items)
	
    i = itemSize
	
    for i in range(itemSize, 0, -1):
	    
        reverseList.append(items[i-1])
		
    return reverseList


reversed = reverse([1, 2, 3, 4,])

print reversed

	    
