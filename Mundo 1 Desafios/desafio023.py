n = int(input('Digite um \033[31;4mnúmero inteiro\033[m: '))
unidade = n % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print('''O número \033[1;31m{}\033[m tem
 unidade: {}
 dezena: {}
 centena: {}
 milhar: {}
 '''.format(n, unidade, dezena, centena, milhar))
