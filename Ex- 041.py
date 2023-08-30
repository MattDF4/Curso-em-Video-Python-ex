anonascimento = int(input('Em que ano você nasceu?:'))
idade = 2023-anonascimento
print('-='*16)
if idade <= 9:
    print(f'O atleta tem \033[0;34m{idade}\033[m anos. \nEstá na categoria \033[0;34mMIRIM')
elif idade <= 14:
    print(f'O atleta tem \033[0;34m{idade}\033[m anos. \nEstá na categoria \033[0;34mINFANTIL')
elif idade <= 19:
    print(f'O atleta tem \033[0;34m{idade}\033[m anos. \nEstá na categoria \033[0;34mJUNIOR')
elif idade <= 25:
    print(f'O atleta tem \033[0;34m{idade}\033[m anos. \nEstá na categoria \033[0;34mSÊNIOR')
else:
    print(f'O atleta tem \033[0:34m{idade}\33[m anos. \nEstá na categoria \033[0:34mMASTER')
