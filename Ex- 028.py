from random import randint
numero = int(randint(0,5))
resposta = int(input('Tente advinhar o númeor que o computar escolheu entre 0 e 5:'))
if resposta == numero:
    print(f'Que sorte! Você acertou o número escolhido pelo computador ({numero}) com seu chute; {resposta}')
else:
    print(f'Sem tanta sorte, o computador escolheu: {numero} enquanto você escolheu: {resposta}.')
