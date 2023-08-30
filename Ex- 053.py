frase = str(input('Digite uma palavra ou frase: ')).strip().split()
ffinal = ''.join(frase).lower()
novo = ''
for c in range(len(ffinal)-1, -1, -1):
    novo = novo + ffinal[c]
print(f'A palavra ao contrário fica: {novo}')

if novo == ffinal:
    print(f'A palavra/Frase "{ffinal}", \033[32mÉ\033[m um palindromo.')
else:
    print(f'A palavra/Frase "{ffinal}", \033[31mNão\033[m é um palindromo.')