array = [10,3,6,9,10,10,3,5,8,60,30,4,3,5]

count_dict = {}

duplicates = []

for num in array: 
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1
        
for key in count_dict:
    if count_dict[key] > 1:
        duplicates.append(key)
        
print("duplicates", duplicates)

for n in duplicates:
    print(f"{n} appeared {count_dict[n]} times")
