class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
def is_BST(node,min,max):
    if node is None:
        return True
    if node.value <= min or node.value >= max:
        return False
    
    left = is_BST(node.left,min,node.value)
    right = is_BST(node.right,node.value,max)
    
    return left and right
   


root = Node(10)
root.left = Node(5)
root.right = Node(15)


print(is_BST(root,float('-inf'),float('+inf'))) #This prints true-its a valid BST

# lets break it a bit 
root = Node(10)
root.left = Node(13)
root.right = Node(15)

print(is_BST(root,float('-inf'),float('+inf'))) #prints false- its not valid

