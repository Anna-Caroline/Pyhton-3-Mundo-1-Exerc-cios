#Sorteio de alunos
'''import random
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a1,a2,a3,a4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))'''
from random import choice
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a1,a2,a3,a4]
print('O aluno escolhido foi {}'.format(choice(lista)))
