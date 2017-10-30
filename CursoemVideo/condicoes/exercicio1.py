from random import *

print('-----Vou pensar em um número de 0 a 5, tente advinhar!-----')
num = randint(0,5)
numuser = int(input('Qual o número que pensei ? '))
print('Processando....')
print('Voce ganhou!' if numuser == num else 'Voce perdeu!')