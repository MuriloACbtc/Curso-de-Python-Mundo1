largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura * altura
tinta = área/2
print('A área da parede é \033[33;1m{} m²\033[m, e será necessário \033[33;1m{} litro(s) de tinta\033[m'.format(área, tinta))