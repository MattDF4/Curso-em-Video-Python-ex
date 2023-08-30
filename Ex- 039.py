anonasce = int(input('Em que ano você nasceu?:'))
genero = str(input('Você é do sexo MASCULINO ou FEMININO?:')).strip().capitalize()
idade = 2023-anonasce
print('-='*15)
print(f'Quem nasceu em {anonasce} terá \033[0;31m{idade}\033[m anos ao fim do ano.(2023)')
print('-'*6)
if genero == 'Masculino' and idade == 18:
    print(f'Por ter 18 anos o seu alistamento deve ser feito \033[0;31messe ano\033[m!')
    print(f'Seu alistamento será em; {2023-(idade-18)}')
elif genero == 'Masculino' and idade < 18:
    print(f'Faltam \033[0;31m{18-idade}\033[m anos para você poder se alistar.')
    print(f'Você poderá se alistar em; \033[0;31m{anonasce+18}')
elif genero == 'Masculino' and idade > 18:
    print(f'O seu alistamente deveria ter sido feito há \033[0;31m{idade-18}\033[m anos.')
    print(f'Seu alistamento foi em; \033[0;31m{2023-(idade-18)}')
else:
    print('Você \033[0;31mNÃO\033[m precisa fazer alistamenot militar obrigatório.')
