primeiron = float(input('Diga o primeiro número:'))
segundon = float(input('Diga o segundo número:'))
print('-='*14)
if primeiron > segundon:
    print(f'O MAIOR número digitado foi o \033[0;34mPRIMEIRO! ({primeiron})')
elif segundon > primeiron:
    print(f'O MAIOR número digitado foi o \033[0;34mSEGUNDO! ({segundon})')
else:
    print('Os números são \033[0;33miguais.')
