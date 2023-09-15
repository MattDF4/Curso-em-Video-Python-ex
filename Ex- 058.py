#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
tentativas = 1
sorteio = int(randint(1, 11))
palpite = int(input('Tente advinhar o número, entre 1 e 10, que o computador escolheu:'))
while palpite != sorteio:
    tentativas += 1
    sorteio = int(randint(1, 11))
    print('-'*5)
    palpite = int(input('Errou! Tente novemente:'))
print('-'*5)
print(f'Parabéns! Você acertou após \033[97m{tentativas} tentativas!\033[m \nOs números foram: {sorteio} e {palpite}')
