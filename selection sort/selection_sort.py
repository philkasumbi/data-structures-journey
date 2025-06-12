def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        smallest_element = i
        for k in range(i+1,n):
            if arr[k] < arr[smallest_element]:
                smallest_element = k
            
        arr[i],arr[smallest_element] = arr[smallest_element],arr[i] 
    return arr

arr = [5,1,2,7,0,4]

print(selection_sort(arr))