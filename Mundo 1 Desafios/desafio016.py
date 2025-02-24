import math
n = float(input('Digite um número: '))
nint = math.trunc(n)
print(12*"XoX")
print('O número \033[1;33m{}\033[m, tem a parte inteira \033[1;34m{}\033[m'.format(n, nint))
