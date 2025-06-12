def quick_sort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    pivot = arr[-1]
    
    left = []
    right = []
    
    for item in arr[:-1]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
                
    left = quick_sort(left)
    right =quick_sort(right)
        
    return left + [pivot] + right
        
       
arr = [12,30,50,47,70,59]
print(quick_sort(arr))   