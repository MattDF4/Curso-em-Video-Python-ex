#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
vim = int(input('Diga o valor: '))
vin = vim
nv = 1
r = str(input('Deseja digitar mais valores? [S/N]')).upper().strip()[0]
vn = vim
maior = vim
menor = vn
print('-'*20)
if r == 'S':
    while r == 'S':
        v = int(input('Diga o valor: '))
        nv += 1
        if v > vim:
            vim = v
            maior = v
        elif v < vin:
            vin = v
            menor = v
        vn += v
        r = str(input('Deseja digitar mais valores? [S/N]: ')).upper().strip()[0]
        print('-'*20)
print('')
print(f'A média dos valores digitados foi de: {vn/nv}')
print(f'O maior valor digitado foi: {maior} e o menor valor foi: {menor}')
print('FIM DO PROGRAMA.')
