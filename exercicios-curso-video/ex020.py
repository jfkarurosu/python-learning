import random

n1 = input("Primeiro Aluno: ")
n2 = input("Segundo Aluno: ")
n3 = input("Terceiro Aluno: ")
n4 = input("Quarto Aluno: ")
alunos = [n1,n2,n3,n4]
random.shuffle(alunos)
print('A ordem de apresentação sera: ')
print(alunos)
