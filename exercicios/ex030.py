# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número inteiro qualquer: '))
r = n % 2 #resto da divisão desse número é
#todo número par vai ter resultado zero. Porque o resto da divisão de qualquer número par é zero. ímpar é um
# print ('O resultado foi {}.'.format(r))
if r == 0 :
    print('O número {} é par.'.format(n))
else :
    print('O número {} é ímpar.'.format(n))
