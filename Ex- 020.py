from random import shuffle
n1 = str(input('Digite o 1º nome:'))
n2 = str(input('Digite o 2º nome:'))
n3 = str(input('Digite o 3º nome:'))
n4 = str(input('Digite o 4º nome:'))
n5 = str(input('Digite o 5º nome:'))
n6 = str(input('Digite o 6º nome:'))
opc = [n1,n2,n3,n4,n5,n6]
shuffle(opc)
print('='*30)
print(f'Dentro das opções, a ordem de apresentação será: \n {opc}')
