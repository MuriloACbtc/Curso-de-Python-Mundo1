s = int(input('Digite o salário atual em reais: '))
ns = s*1.15
print('O novo salário é \033[1;7m{:.1f} reais\033[m, \033[37m(15% de aumento)\033[m'.format(ns))
