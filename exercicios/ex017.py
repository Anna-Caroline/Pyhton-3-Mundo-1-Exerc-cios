# Ler catetos e calcular a hipotenusa
'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = (co**2+ca**2)**(1/2)
print ('A hipotenusa irá medir {:.2f}'.format(hi))'''
'''import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = math.hypot(co,ca)
print ('A hipotenusa irá medir {:.2f}'.format(hi)) '''

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = hypot(co,ca)
print ('A hipotenusa irá medir {:.2f}'.format(hi))


