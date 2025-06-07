# solving problems using stack 
"""
----STEPS----
1.traverse the strings character by character
2.if you encounter an opening paranthesis, push it to the stack
3.if you encounter a closing paranthesis, check if it has a corresponding opening paranthesis,
is so pop
"""

chars = "(())(()){}}"

stack = []
# mapping of closing to opening 
pairs = {')':'(',
         '}':'{',
         ']':'['
         }
for char in chars:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        if not stack:
             print("Unbalanced: No matching opening for", char)
             break
        else:
            stack.pop() 
           
else:
    if not stack:
        print("✅ All parentheses are balanced!")
    else:
        print("❌ Unbalanced: Some opening parentheses were not closed:", stack)



