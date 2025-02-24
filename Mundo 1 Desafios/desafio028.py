import random
import time
n = random.randint(1,5)
print('\033[34m--=\033[31m--=\033[m'*12)
print('Tente acertar um \033[33mnúmero inteiro\033[m que o computador imaginou de \033[36m1 até 5\033[m')
print('\033[31m=--\033[34m=--\033[m'*12)
n1 = int(input('Digite o número: '))
print('\033[35mProcessando...\033[m')
time.sleep(2)
if n1 == n:
    print('Parabéns você \033[32macertou\033[m!')
else:
    print('Que pena, você \033[31merrou\033[m! \nO número era \033[1;32m{}\033[m!'.format(n))
