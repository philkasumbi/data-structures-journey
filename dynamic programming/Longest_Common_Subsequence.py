text1 = "abcde"
text2 = "ace"

i = 0
j = 0
result = []

while i < len(text1) and j < len(text2):
    if text1[i] == text2[j]:
        result.append(text1[i])
        j += 1
    i += 1
    
    
    
print(f"The matching letters in order:"," ".join(result))
print(f"The length of the matching is strings is, {len(result)}")