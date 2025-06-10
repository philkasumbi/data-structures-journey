
# def bubble_sort(arr):
#     n = len(arr)
    
#     swapped = True
    
#     while swapped:
#        swapped = False
#        for i in range (n-1):
#            if arr[i] > arr[i+1]:
#                arr[i],arr[i+1] = arr[i+1],arr[i]
               
#                swapped = True 
#     return arr


# my_list = [7, 3, 5, 1, 8, 2, 4, 6]
# print(f"The original list: {my_list}")

# sorted_list = bubble_sort(my_list)
# print(f"The sorted list is {sorted_list}")
    

def bubble_sort(arr):
    n  = len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
               arr[j],arr[j+1] = arr[j+1],arr[j]
               
    return arr

my_list = [7, 3, 5, 1, 8, 2, 4, 6]

print(bubble_sort(my_list))
