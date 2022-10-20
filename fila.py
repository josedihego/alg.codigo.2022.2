MAX = 20

class MyQueue:
    def __init__(self):
        self.tail = 0
        self.head = 0
        self.Q  = [None] * MAX
    
    def enqueue(self,x):
        self.Q[self.tail] = x
        if self.tail == (len(self.Q)-1):
            self.tail = 0
        else:
            self.tail =  self.tail + 1
    
    def dequeue(self):
        x = self.Q[self.head]
        if self.head == (len(self.Q) -1):
            self.head = 0
        else:
            self.head =  self.head + 1
        return x

fila = MyQueue()
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(8)
fila.enqueue(30)
fila.dequeue()
fila.dequeue()
fila.enqueue(18)
fila.enqueue(99)
print('fim')