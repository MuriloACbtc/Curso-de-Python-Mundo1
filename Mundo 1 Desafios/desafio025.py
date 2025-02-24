n = input('Digite seu \033[40;32;1mnome\033[m: ')
nnormal = n.strip()
print('O nome \033[40;32;1m{}\033[m tem \033[33m"SILVA"\033[m no nome: {}'.format(nnormal, "silva" in nnormal.lower()))