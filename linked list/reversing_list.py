class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node: {self.value}"
      
Node1  = Node(10)
Node2  = Node(20)
Node3  = Node(30)
Node4  = Node(40)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

head = Node1
  
prev = None
current = head

while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node 
    
    if current:
        print(current.value)

# set the new head
head = prev


print("\nReversed Linked List:")
current = head
while current:
    print(current.value)
    current = current.next