#faça um programa que leia 3 números e mostre o maior e menor dentre eles
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
n3 = int(input('Digite o 3º número:'))

print('-=-'*12)
print('VERIFICANDO MENOR E MAIOR NÚMERO')
print('-=-'*12)

print('-'*25)
if n1 > n2 and n1 > n3:
    print(f'O maior número foi: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número foi: {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior númeor foi: {n3}')

print('-'*25)

if n1 < n2 and n1 < n3:
    print(f'O menor número foi: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número foi: {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número foi: {n3}')

print('-'*25)
