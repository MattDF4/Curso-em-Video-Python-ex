#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
resposta = str(input('Diga qual o seu sexo [M/F]: ')).upper().strip()[0]
while resposta not in 'FM':
    resposta = str(input('Respota inválida. Tente novamente: ')).upper().strip()[0]
print(f'Sexo \033[4m{resposta}\033[m registrado com sucesso.')
