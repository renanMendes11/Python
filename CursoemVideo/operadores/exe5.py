#Ler um numero e mostre a sua tabuada
n1 = int(input('Digite um numero: '))
i = 1
print('Tabuada')
while(i <= 10):
    print('\n {}x{}= {}'.format(i,n1,n1*i))
    i = i + 1
