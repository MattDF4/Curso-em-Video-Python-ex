# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#Bônus = Diga qual a menor e maior idade e à quem elas pertencem
from datetime import date
candidatos = int(0)
maiores = int(0)
menores = int(0)
anteriormaior = int(0)
anteriormenor = int(1000)
anoagora = date.today().year
print('=' * 35)
for c in range(1, 3):
    candidatos += 1
    nome = str(input(f'Qual o nome do  {candidatos}° participante?: '))
    ano = int(input('Em que ano o nasceu?: '))
    idade = anoagora - ano
    if anteriormenor > idade:
        anteriormenor = idade

    print('-' * 35)
    if idade > anteriormaior:
        anteriormaior = idade
    else:
        print()

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(
    f'Foram ao total; \033[32m{maiores} maiores\033[m de idade e \033[31m{menores} menores\033[m de idade contabilizados.')
print(f'O candidato mais velho tem {anteriormaior} anos e o mais novo tem {anteriormenor}')
