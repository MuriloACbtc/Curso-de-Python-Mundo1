n = int(input('Digite um \033[37;1;7mnúmero inteiro\033[m: '))
if n % 2 == 0:
    print('O número {} é \033[1mPAR\033[m!'.format(n))
else:
    print('O número {} é \033[1mÍMPAR\033[m!'.format(n))
