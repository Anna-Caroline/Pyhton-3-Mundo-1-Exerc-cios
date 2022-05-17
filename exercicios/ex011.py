#Pintando a parede
# Cada litro de tinta pinta uma área de 2m²
n1 = float(input('Digite a largura da parede: '))
n2 = float(input('Digite a altura da parede: '))
area = n1 * n2
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(n1,n2,area))
tinta = area / 2
print('Para pintar essa parede, serão necessários {}l de tinta.'.format(tinta))

