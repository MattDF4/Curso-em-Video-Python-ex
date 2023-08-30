cidade = str(input('Digite o nome de uma cidade:')).strip().capitalize()
print('='*40)
print(f'A palavra "Santo" está no primeiro nome?[T/F]: {"Santo" in cidade.split()[0]}')
