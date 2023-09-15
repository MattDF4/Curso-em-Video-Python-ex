# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = 0
c = 1
print('''
-----------------------------
       DIGITE NÚMEROS
  [Digite 999 para parar]
-----------------------------''')
v = int(input('Digite um valor: '))
print('-'*15)
while v != 999:
    v = int(input('Digite outro valor: '))
    if v == 999:
        break
    c += 1
    soma += v
    print('-'*15)
print('')
print(f'Foram digitados cerca de: \033[4m{c} números.\033[m')
print(f'A soma desses números resulta em: \033[4m{soma}\033[m')
