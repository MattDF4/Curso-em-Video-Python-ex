#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
v = int(input('Diga um valor [999 para PARAR!]: '))
c = 1
soma = v
print('-'*15)
while v != 999:
    v = int(input('Diga outro valor: '))
    print('-'*15)
    if v == 999:
        break
    c += 1
    soma += v
print(f'Foram digitados \033[4m{c}\033[m números. \nA soma entre eles resulta em: \033[4m{soma}\033[m')
