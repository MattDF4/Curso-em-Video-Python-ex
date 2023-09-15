#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:0 – 1 – 1 – 2 – 3 – 5 – 8
n = int(input('Quantos números da sequência de Fibonacci você deseja ver?: '))
c = 3
p = 0
s = 1
print(end=f'{p}-{s}')
while c <= n:
    c += 1
    seq = p + s
    p = s
    s = seq
    print(end=f'-{seq}')
