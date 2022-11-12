
def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

print(fatorial(100))

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def __eq__(self, outro: object):
        if outro is Funcionario and self.salario == outro.salario:
            return True
        else:
            return False
    def __gt__(self, outro:object):
        if outro is Funcionario and self.salario > outro.salario:
            return True
        else:
            return False