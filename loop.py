
lista_med = ['azitromicina', 'tilenol', 'paracetamol', 'pomada']

print('Opção 1')

med_buscado = input('Informe o medicamento buscado: ')
for m in lista_med:
    if m == med_buscado:
        print('Medicamento encontrado')
        break
    print('Medicamento visitado : {}'.format(m))

print('Opção 2')
for m in lista_med:
    if m == med_buscado:
        print('Medicamento encontrado')
    print('Medicamento visitado : {}'.format(m))