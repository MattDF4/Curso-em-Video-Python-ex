lado1 = float(input('Medida do lado 1:'))
lado2 = float(input('Medida do lado 2:'))
lado3 = float(input('Medida do lado 3:'))
print('-='*12)
if lado1 < lado3 + lado2 and lado2 < lado3 + lado1 and lado3 < lado2 + lado1:
    print('\033[32mPODEMOS\033[m ter um triângulo com essas medidas!')
    if lado1 == lado2 == lado3:
        print('O seu \033[37mTRIÂNGULO\033[m é \033[30;107mEQUILÁTERO!\033[m')
    elif lado1 == lado2 or lado3 == lado2 or lado3 == lado1:
        print('O seu \033[37mTRIÂNGULO\033[m é \033[30;107mISÓSCELES!\033[m')
    elif lado1 != lado2 != lado3 != lado1:
        print('O seu \033[0;37mTRIÂNGULO\033[m é \033[30;107mESCALENO!\033[m')
else:
    print('\033[31mNÃO\033[m foi possível formar um triângulo.')
