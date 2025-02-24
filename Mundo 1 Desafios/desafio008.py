m = float(input("digite o valor em metros: "))
c = m * 100
mm = m * 1000
if 1 == m:
    print(m, 'metro são \033[1;34m{} centímetros\033[m, e \033[1;36m{} milímetros\033[m.'.format(c, mm))
else:
    print(m, 'metros são \033[1;34m{} centímetros\033[m, e \033[1;36m{} milímetros\033[m.'.format(c, mm))