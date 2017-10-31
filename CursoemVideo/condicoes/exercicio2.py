vel = float(input('Qual a velicidade do seu carro ? '))
if vel > 80:
    multa = (vel - 80) * 7.00
    print ('MULTADO! Voce excedeu o limite de velocidade com {}km/h'.format(vel))
    print ('Voce pagará uma multa de {}'.format(multa))
else:
    print ('Dirija com segurança!')