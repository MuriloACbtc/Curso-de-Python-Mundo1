import math
an = float(input('Digite um \033[37;1mângulo\033[m: '))
a = math.radians(an)
sen = math.sin(a)
cos = math.cos(a)
tg = math.tan(a)
cores = {
    'amarelo' : '\033[33m',
    'nada' : '\033[m',
    'azul' : '\033[34m',
    'vermelho' : '\033[31m'
}
print('O', cores['vermelho'], 'seno', cores['nada'], 'do \33[1;37mângulo {}°\33[m é {:.3f}, o'.format(an, sen),
      cores['azul'], 'cosseno', cores['nada'], 'do \33[1;37mângulo {}°\033[m é {:.3f}, e a'.format(an, cos),
                                               cores['amarelo'], 'tangente', cores['nada'], 'é {:.3f}'.format(tg))