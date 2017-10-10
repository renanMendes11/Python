#Desafio 4
##Faça um progama que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas informações possiveis sobre ela.
algo = input('Digite algo: ')
print('É string ?', algo.isalpha())
print('É número?', int(algo).isnumeric)
print('Todas as letras maiusculas?', algo.isupper())
