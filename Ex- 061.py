#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Escolha o primeiro termo: '))
razao = int(input('Qual a razão?: '))
term = primeiro
contador = 1
while contador <= 10:
    print(end=f' -> {term} ')
    term += razao
    contador += 1
