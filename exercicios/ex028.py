# Jogo de adivinhação
from random import randint
from time import sleep
computador = randint(0,5) # O computador pensa em um número
# print ('Pensei no número {}.'.format(computador))
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador :
    print ('Parabéns! Você conseguiu me vencer!')
else:
    print('Você errou, eu pensei no número {}.'.format(computador))




'''n = int(input('Vou pensar em um número entre zero e cinco. Tente adivinhar: '))
if n == 0 :
    print ('Parabéns! Você adivinhou!')
else :
    print ('Você errou, eu pensei no 0.')'''