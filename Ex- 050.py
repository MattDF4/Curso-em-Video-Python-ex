s = int(0)
for c in range(1, 7):
    valor = int(input(f'Digite o {c}º número:'))
    if valor % 2 == 0:
        s = s + valor
print(f'A soma dos números pares resulta em: {s}')
