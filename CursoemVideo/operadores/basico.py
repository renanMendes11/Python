#Ordem de precedencia dos operadores
#1- ()
#2- **
#3- *, /, // e %
#4- + e -

##Operaçoes com numeros
print(5*2+3)
print(5**3)
print(pow(5,3))
print(19//2)
print(19/2)

## Operaçoes com strings
print(5* '-')
print(5* 'Oi ')
print(5* '=')

nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:-^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
d = n1 / n2
print('A divisao vale: {:.2f}'.format(d))