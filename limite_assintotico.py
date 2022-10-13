n_0 = 0.1
c_1 = 0.1
c_2 = 20

achou = False
while(not achou):
    print('n_0 : {} c_1: {}  c_2 : {}'.format(n_0, c_1, c_2))
    if( c_1 <= (0.5 - (3.0/n_0)) and  (0.5 - (3.0/n_0)) <=c_2):
        achou = True
    else:
        n_0 = n_0 + 0.1
        c_1 =  c_1 + 0.1
        c_2 = c_2 + 0.2
print('n_0 : {} c_1: {}  c_2 : {}'.format(n_0, c_1, c_2))
