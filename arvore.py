class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x!=None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root =  z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z


minhaQueridaArvore = Tree()
minhaRaizinha = Node(41)
minhaQueridaArvore.root =  minhaRaizinha
minhaQueridaArvore.insert(Node(55))
minhaQueridaArvore.insert(Node(32))
minhaQueridaArvore.insert(Node(65))
minhaQueridaArvore.insert(Node(24))
print('fim')


