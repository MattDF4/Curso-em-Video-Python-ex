print('='*20)
print('10 PARTES DE UMA PA')
print('='*20)

pt = int(input('Diga o primeiro termo:'))
st = int(input('Diga o segundo termo:'))
razao = pt + (10 - 1) * st
for cc in range(pt, razao+1, st):
    print(cc, end=' → ')
print('FIM')
#→
