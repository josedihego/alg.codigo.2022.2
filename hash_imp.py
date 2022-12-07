import math

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

class HashTable:

    def __init__(self, m):
        self.T = [0] * m
        for i in range(m):
            self.T[i] = MyList()
        self.m = m
    
    def h(self, k):
        A = (math.sqrt(5) -1 )/2
        return math.floor((k * A % 1) * self.m)
    
    def insert(self,new_e):
        p = self.h(new_e)
        print('posição {} do {}'.format(p,new_e))
        self.T[p].insert(Node(new_e))

table = HashTable(10)
table.insert(14)
table.insert(15)
table.insert(10)
table.insert(19)
table.insert(0)
table.insert(1)
table.insert(2)
print('fim')



         






