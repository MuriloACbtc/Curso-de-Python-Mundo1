n = input('Digite seu \033[40;7;1mnome completo\033[m: ')
nn = n.strip()
separado = nn.split()
print('O nome \033[40;7;1m{}\033[m, tem o {}primeiro nome{} sendo {} e o {}último nome{} sendo {}'.format(nn, '\033[35m', '\033[m', separado[0], '\033[36m', '\033[m', separado[-1]))
#ou poderia o último ser: separado[len(separado)-1]
