def binary_search(arr,target):
    n = len(arr)
    
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid -1
            
    return f"item {target} not found"

arr =  [1, 3, 5, 8, 13, 21, 34]

print(binary_search(arr,21))
            