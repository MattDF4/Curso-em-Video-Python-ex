from _datetime import date
ano = int(input('Diga um ano qualquer:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissesxto.')
