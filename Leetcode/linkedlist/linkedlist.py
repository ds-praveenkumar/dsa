# Linked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return f"data : {self.data}"
    
def show_list( head ):
    currentNode = head
    while currentNode:
        print(currentNode.data, end='->')
        currentNode = currentNode.next
    print('null')
        
def show_list_prev( head ):
    currentNode = head
    while currentNode:
        print(currentNode.data, end='->')
        currentNode = currentNode.prev
    print('null')

class DoublyList:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
        self.prev = None
        
    def __repr__(self) -> str:
        return f"data {self.data}"

        
if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    currentNode = a
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    
    while currentNode :
        print(currentNode)
        currentNode = currentNode.next 
        
    a = DoublyList(1)
    b = DoublyList(2)
    c = DoublyList(3)
    d = DoublyList(4)
    
    startNode = a
    
    a.next = b
    b.prev = a
    
    b.next = c 
    c.prev = b
    
    c.next = d
    d.prev = c
    
    show_list(startNode)
    show_list_prev(d)
