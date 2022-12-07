
def h(nome):
    soma = 0
    for l in nome:
        soma = soma + ord(l)
    print(soma)
    return soma%26

res_hash1 = h('Esdras')
res_hash2 = h('Vinícius')
res_hash3 = h('Diego')
print(res_hash1)
print(res_hash2)
print(res_hash3)