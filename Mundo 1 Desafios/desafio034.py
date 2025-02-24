s = float(input('Digite o seu \033[30;43msalário\033[m em R$: '))
if s > 1250:
    print('O aumento será de 10%, e o novo salário será de \033[32mR${:.2f}\033[m'.format(s*1.1))
else:
    print('O aumento será de 15%, e o novo salário será de \033[32mR${:.2f}\033[m'.format(s*1.15))