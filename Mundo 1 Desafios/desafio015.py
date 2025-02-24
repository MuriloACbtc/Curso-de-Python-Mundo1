d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))

print('O total a pagar é de \033[32mR${:.2f}\033[m'.format((d*60)+(km*0.15)))

#ou
drs = d * 60
kmrs = km * 0.15
total = drs + kmrs
print('O total a pagar é de \033[1;4;7mR${:.2f}\033[m'.format(total))