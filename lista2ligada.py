
class MyList:
    def __init__(self):
        self.head = None
    
    def insert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev =  None

class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next =  None

lista = MyList()
lista.insert(Node(7))
lista.insert(Node(10))
lista.insert(Node(13))
lista.insert(Node(18))
print('fim')