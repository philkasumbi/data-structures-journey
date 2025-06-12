def merge_sort(arr):
    n = len(arr)
    
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        right_half = arr[mid:]
        left_half = arr[:mid]
        
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        
        final_arr = []
        
        i = 0
        j = 0
        
        while i < len(left_half) and j <len(right_half):
            if left_half[i] < right_half[j]:
                final_arr.append(left_half[i])
                i += 1
            else:
                final_arr.append(right_half[i])
                j += 1
        # add leftovers to the list
        
        while i < len(left_half):
            final_arr.append(left_half[i])
            i += 1
        while j < len(right_half):
            final_arr.append(right_half[j])
            j += 1
            
    return final_arr

arr = [1,5,8,9,4,7,0,3,5,8]

print(merge_sort(arr))        