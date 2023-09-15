#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.
print('''
=============================
LEITURA DE PREÇOS E PRODUTOS 
=============================''')
nome = str(input('Diga o nome do produto: '))
preco = float(input('Diga o preço do prduto: R$'))
mil = 0
nmb = nome
pmb = preco
if preco > 1000:
    mil += 1
total = preco
while True:
    print('-'*25)
    resp = str(input('Deseja cadastrar outro produto? [S/N]: ')).lower().strip()[0]
    print('-'*25)
    if resp == 's':
        nome = str(input('Diga o nome do produto: ')).strip()
        preco = float(input('Diga o preço do produto: R$'))
        if preco < pmb:
            pmb = preco
            nmb = nome
        if preco > 1000:
            mil += 1
        total += preco
    elif resp == 'n':
        break
    elif resp not in 'sn':
        while resp not in 'sn':
            resp = str(input('Respota inválida, tente novamente: ')).lower().strip()[0]
print('-'*10)
print(f'O valor total da compra foi: R${total:.2f}')
print(f'Foram registrados \033[97;4m{mil}\033[m produtos custando R$1000.00 ou mias.')
print(f'O produto mais barato foi o(a): \033[97;4m{nmb}\033[m, custando \033[4mR${pmb}\033[m')
print('FIM DO PROGRAMA')
print('-'*10)