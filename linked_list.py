class Node:
    def __init__(self,data= None):
        self.data  = data
        self.next = None
    
    def __repr__(self) -> str:
        return f"{self.data}->"

class LinkedList:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next
    
    def __repr__(self) -> str:
        return f"{self.head}->"

if __name__ =='__main__':
    print("linked list")
    a = Node()
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    i = LinkedList(a)

    print( a )
    print( i )
    