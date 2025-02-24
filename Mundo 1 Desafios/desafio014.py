tc = float(input('Digite a temperatura em Celsius: '))
tf = (9*tc) / 5 + 32
print('A temperatura de \033[34m{}°C\033[m corresponde a \033[31m{}°F\033[m'.format(tc, tf))