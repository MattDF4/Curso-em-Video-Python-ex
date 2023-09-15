# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos
primeiro = int(input('Diga o primeiro termo: '))
razãoo = int(input('Diga a Razão da PA: '))
termo = primeiro
contador = 1
total = 10
while contador <= 10:
    print(end=f' -> {termo}')
    termo += razãoo
    contador += 1

print('')
print('-='*25)


resposta = str(input('Deseja mostrar mais termos? [S/N]: ')).upper().strip()[0]
contador = 1
razão = 0

while resposta == 'S':
        escolha = int(input('Quantos termos deseja adicionar?: '))
        total += escolha
        print('-'*20)
        segundaescolha = str(input('Deseja mudar a razão? [S/N]: ')).upper().strip()[0]
        if segundaescolha == 'S':
            razão = int(input('Qual será a nova razão: '))
            while contador <= escolha:
                print(end=f' -> {(termo + razão) - razãoo}')
                termo += razão
                contador += 1
        elif segundaescolha == 'N':
            razão = razãoo
            while contador <= escolha:
                print(end=f' -> {termo}')
                termo += razão
                contador += 1
        contador = 1
        print('')
        print('-=' * 25)
        print('')
        resposta = str(input('Deseja mostrar mais termos? [S/N]: ')).upper().strip()[0]
print('')
print('FIM do programa.')
print(f'Foram mostrados ao todo \033[4m{total}\033[m termos.')