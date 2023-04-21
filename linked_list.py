class LinkedList:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next
    
    def __repr__(self) -> str:
        return f"{self.data}->"

if __name__ =='__main__':
    print("linked list")
    a = LinkedList(1)
    b = LinkedList(2)
    c = LinkedList(3)
    d = LinkedList(4)
    e = LinkedList(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    i = LinkedList(0,a)

    while i.next != None:
        print(i)
        i = a