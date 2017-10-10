#Ler preço de um produto e mostre seu valor com 5% de desconto
n1 = float(input('Digite o preço do produto R$: '))
d = n1 - (0.05 * n1)
print('Esse prouto com 5% de desconto fica: R${}'.format(d))
