import datetime

a = int(input('Digite \033[1;30;46mum ano\033[m, ou \033[30;1;47m0 para o atual\033[m: '))
if a == 0:
    a = datetime.date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} É BISSEXTO!'.format(a))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(a))
