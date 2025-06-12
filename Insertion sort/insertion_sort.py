def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements that are greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key in the correct position
        arr[j + 1] = key
    
    return arr


arr = [30, 40, 29, 17, 13, 79]
print(insertion_sort(arr))
