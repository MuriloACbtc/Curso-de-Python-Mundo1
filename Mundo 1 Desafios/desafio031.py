d = float(input('Digite a \033[33mdistância\033[m da viagem em Km: '))
if d <= 200:
    print('O preço da viagem é \033[32mR${:.2f}\033[m'.format(d*0.5))
else:
    print('O preço da viagem é \033[32mR${:.2f}\033[m'.format(d*0.45))
