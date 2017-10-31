distancia = float(input('Qual a distancia da viagem(km)? '))
if distancia <= 200:
    passagem = 0.5 * distancia
else:
    passagem = 0.45 * distancia
#pasagem = 0.5 * distancia if distancia <= 200 else 0.45 * distancia

print ('Sua passagem custa: R${}'.format(passagem))