# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
print('''
------------------
|    CADASTRO    |
------------------''')
c = 1
i = h = mm = 0
while True:
    idade = int(input(f'Diga a idade da {c}° pessoa: '))
    if idade >= 18:
        i += 1
    sexo = str(input('Diga seu sexo [M/F]: ')).lower().strip()[0]
    if sexo == 'm':
        h += 1
    elif sexo == 'f' and idade < 20:
        mm += 1

    while sexo not in 'm' 'f':
        sexo = str(input('Resposta inválida, tente novamente: ')).lower().strip()[0]
        print('---')
        if sexo == 'm':
            h += 1
        elif sexo == 'f' and idade < 20:
            mm += 1
    print('-'*40)
    r = str(input('Deseja cadastrar mais pessoas? [S/N]: ')).lower().strip()[0]
    print('-'*40 )
    c += 1
    if r not in 'sn':
        while r not in 'sn':
            r = str(input('Resposta inválida, tente novamente: ')).lower().strip()[0]
            print('---')
    if r == 'n':
        print('='*20)
        print('FIM DO PROGRAMA')
        print('=' *20)
        break
print(f'''Foram cadastrados:
{i} maiores de idade (+18)
---
{h} homens. 
---
{mm} mulheres com menos de 20 anos.''')
