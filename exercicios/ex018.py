#digite o ângulo e calcule sen, cos, tan
from math import sin, cos, tan , radians
a = float(input('Digite o ângulo: '))
ang = radians(a)
print('-'*20)
print('O seno de {:.2f} é {:.2f};\nO cosseno {:.2f};\nE a tangente {:.2f}'.format(ang,sin(ang),cos(ang), tan(ang)))
print('-'*20)
