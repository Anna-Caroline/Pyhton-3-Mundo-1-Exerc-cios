# Primeira e última ocorrência de um string
# Faça um programa q leia uma frase e mostre quantas vezes aparece a letra A, em que posição ela aparece pela primeira vez, e em que posição ela aparece pela última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
# r.find procura pela direita
