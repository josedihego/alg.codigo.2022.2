MAX = 10

class Pilha:
    def __init__(self):
        self.top = 0
        self.S = [None] * MAX
    
    def esta_vazia(self):
        return self.top == 0

    def esta_cheia(self):
        return self.top == len(self.S)

    def push(self,  elemento):
        if not self.esta_cheia():
            self.S[self.top] = elemento
            self.top =  self.top +1
        else:
            print('Pilha cheia')
    def pop(self):
        if not self.esta_vazia():
            self.top = self.top -1 
            return self.S[self.top+1]
        else:
            print('Pilha vazia')
    def print_pilha(self):
        print('--T---')
        pos = self.top
        if self.esta_cheia(): pos = self.top-1
        for i in range(pos-1, -1, -1):
            print(self.S[i])
        print('--B---')

pilha =  Pilha()
pilha.push('Leo')
pilha.push('João')
pilha.push('Vini M')
pilha.push('Cabral')
pilha.push('Esdras')
pilha.push('Daniel')
pilha.pop()
pilha.pop()
pilha.print_pilha()
