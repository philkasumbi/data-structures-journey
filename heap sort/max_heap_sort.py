array = [4,1,2,7,9]

def heapfy_max(array,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    
    if left < n and array[left] > array[largest]:
        largest= left
    
    if right < n and array[right] > array[largest]:
        largest = right
        
        
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapfy_max(array,n,largest)
        
n = len(array)
for i in range(n//2 -1,-1,-1):
    heapfy_max(array,n,i)
    
for i in range(n - 1, 0, -1):
    array[0], array[i] = array[i], array[0]  # Move max to the end
    heapfy_max(array, i, 0)           # Rebuild heap on reduced size

print(array)