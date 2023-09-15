#Faça um programa que leia um número qualquer e mostre o seu fatorial.
fatorial = int(input('Escolha um número para ver seu fatorial: '))
contador = fatorial
multi = 1
print(end=f'O fatorial de {fatorial}! = ')
while contador > 0:
    print(end=f'{contador}')
    print(end=' x ' if contador > 1 else ' = ')
    multi = multi * contador
    contador -= 1
print(multi)
