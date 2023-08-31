# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
c = 0
maiorpeso = 0
menorpeso = 1000
for pers in range(1, 6):
    c += 1
    peso = float(input(f'Quanto a {c}° pessoa pesa?: '))
    print('-'*33)
    if peso > maiorpeso:
        maiorpeso = peso

    if peso < menorpeso:
        menorpeso = peso

print(f'O maior peso digitador foi: \033[31m{maiorpeso}kg\033[m \nO menor peso digitado foi: \033[31m{menorpeso}kg\033[m')
