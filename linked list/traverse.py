class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"nodes 1:{self.value}"
      

Node1  = Node(10)
Node2  = Node(20)
Node3  = Node(30)
Node4  = Node(40)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

head = Node1

current = head

while current is not None:
    print(current.value)
    current = current.next


