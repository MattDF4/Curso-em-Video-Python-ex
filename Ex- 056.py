# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print('-'*25)
print('          FICHA')
print('-'*25)
print()
c = 0
idadeh = 0
totalidade = 0
homem = ''
mulheres = 0
print('='*35)
for pss in range(1, 5):
    c += 1
    nome = str(input(f'Nome da {c}° pessoa: '))
    idade = int(input('Idade: '))
    totalidade = totalidade + idade
    sexo = str(input('Sexo[F/M]: ')).lower()
    if sexo == 'masculino' or 'm':
        if idade > idadeh:
            idadeh = idade
            homem = nome
    elif sexo == 'feminino' or 'f':
        if idade < 20:
            mulheres += 1
        else:
            print()
    print('='*35)


print()
print('-'*35)
print(f'''
|
|  A \033[4mmédia\033[m de idade do grupo foi de: \033[97m{totalidade/4:.0f}\033[m 
|  O \033[4mhomem mais velho\033[m do grupo foi o \033[97m{homem}\033[m com \033[97m{idadeh}\033[m anos.
|  Foram registradas \033[97m{mulheres}\033[m com \033[4mmenos de 20 anos\033[m.
|
''')
print('-'*35)
