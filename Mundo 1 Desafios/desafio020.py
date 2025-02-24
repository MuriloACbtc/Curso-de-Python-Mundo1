from random import shuffle
print('\033[7mDigite\033[m o \033[1mnome dos alunos\033[m')
a = str(input('Digite o nome do aluno 1: '))
b = str(input('Digite o nome do aluno 2: '))
c = str(input('Digite o nome do aluno 3: '))
d = str(input('Digite o nem do aluno 4: '))
lista = [a, b, c, d]
shuffle(lista)
print('\033[1;7m', lista, '\033[m')
