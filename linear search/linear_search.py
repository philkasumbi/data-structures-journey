def linear_search(arr,n):
    l = len(arr)
    
    for i in range(l):
        if arr[i] == n:
            return i
        
    return f"sorry!! item {n} not found"

arr = [23,36,48,89,59,3,8,9,1]

print(linear_search(arr,10))