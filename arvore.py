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
    
    def tree_search(self, x, k):
        if(x==None or x.key == k):
            return x
        if(k < x.key):
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right , k)

    def tree_minimum(self, x):
        while(x.left!= None):
            x = x.left
        return x

    def tree_successor(self, x):
        if x.right != None:
            return self.tree_minimum(x.right)
        y = x.p
        while (y!= None and x==y.right):
            x = y
            y = y.p 
        return y

minhaQueridaArvore = Tree()
minhaRaizinha = Node(41)
minhaQueridaArvore.root =  minhaRaizinha
minhaQueridaArvore.insert(Node(55))
minhaQueridaArvore.insert(Node(32))
minhaQueridaArvore.insert(Node(65))
minhaQueridaArvore.insert(Node(24))
print('fim')

noRetorno = minhaQueridaArvore.tree_search(minhaRaizinha,888)
if(noRetorno!=None):
    print('chave retornada: {}'.format(noRetorno.key))
else:
    print('No não eontrado')

noMinimo = minhaQueridaArvore.tree_minimum(minhaRaizinha)
print('Nó mínimo = {}'.format(noMinimo.key))

sucessor = minhaQueridaArvore.tree_successor(minhaRaizinha)
print('Sucessor raiz = {}'.format(sucessor.key))