print('\033[1;4;33m=-\033[m'*20)
r1 = float(input('Digite o tamanho da \033[1;37mprimeira reta\033[m: '))
r2 = float(input('Digite o tamanho da \033[1;37msegunda reta\033[m: '))
r3 = float(input('Digite o tamanho da \033[1;37mterceira reta\033[m: '))
print('\033[1;4;33m=-\033[m'*20)
if (r1+r2) > r3 and (r2+r3) > r1 and (r1+r3) > r2:
    print('As retas que medem {}, {} e {} \033[1;35mpodem formar um triângulo\033[m'.format(r1, r2, r3))

else:
    print('As retas que medem {}, {} e {} \033[1;36mnão podem formar um triângulo\033[m'.format(r1, r2, r3))


