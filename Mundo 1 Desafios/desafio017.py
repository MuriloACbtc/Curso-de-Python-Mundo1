from math import sqrt

print('Em um triângulo retângulo')
co = float(input('Digite o \033[34mcateto oposto: \033[m'))
ca = float(input('Digite o \033[31mcateto adjacente: \033[m'))
hip = sqrt(co ** 2 + ca ** 2)
#ou hip = (co ** 2 + ca ** 2) ** (1/2)
#ou poderia ter importado math como um todo e usado "pow" ao invés de "**"
print('A \033[33mhipotenusa\033[m do triângulo é \033[33m', hip, '\033[m')

