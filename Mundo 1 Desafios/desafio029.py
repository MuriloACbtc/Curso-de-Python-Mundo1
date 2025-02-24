v = float(input('Digite a velocidade do seu carro em km/h: '))
if v > 80:
    print('Você foi MULTADO! \nSeu carro estava com uma velocidade acima de 80km/h')
    print('Como você estava a {:.0f}km/h, sua multa ficou em R${}'.format(v, (v-80)*7))
else:
    print('PARABÉNS! Você respeitou o limete de velocidade de 80km/h')
print('Dirija com segurança!')
