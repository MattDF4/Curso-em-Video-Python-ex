nome = str(input('Digite seu nome completo:')).strip()
print('='*70)
print(f'Seu nome tem a seguinte quantidade de caracteres: {len(nome)}')
print('='*50)
print(f'Seu nome com todas as letras maiúsculas: \n{nome.upper()}')
print('='*50)
print(f'Seu nome com todas as letras minúsculas: \n{nome.lower()}')
print('='*50)
print(f'Ao todo, desconsiderando os espaços, o nome tem a seguida quantidade de caracteres: \n{len(nome) - nome.count(" ")}')
print('='*50)
print(f'O primeiro nome é: {nome.split()[0]} e tem: {len(nome.split()[0])} letras.')