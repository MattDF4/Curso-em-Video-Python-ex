from random import choice
n1 = str(input('Nome do 1º aluno:'))
n2 = str(input('Nome do 2º aluno:'))
n3 = str(input('Nome do 3º aluno:'))
n4 = str(input('Nome do 4º aluno:'))
print('='*30)
n5 = str(input('Nome do 5° aluno:'))
n6 = str(input('Nome do 6º aluno:'))
n7 = str(input('Nome do 7° aluno:'))
n8 = str(input('Nome do 8° aluno:'))
turma1a = [n1,n2,n3,n4]
turma1b = [n5,n6,n7,n8]
escolhido1a = choice(turma1a)
escolhido1b = choice(turma1b)
print('='*30)
print(f'O aluno escolhido da turma 1a ({turma1a})foi: |{escolhido1a}|')
print(f'o aluno escolhido da turma 1b ({turma1b})foi: |{escolhido1b})')

 