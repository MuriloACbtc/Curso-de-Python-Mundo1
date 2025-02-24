import random
print('Digite o nome dos \033[1;7malunos\033[m e descubra qual é o mais \33[1;7maut\033[m')
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
e = input('Aluno 5: ')
f = input('Aluno 6: ')
lista = [a, b, c, d, e, f]
chute = random.choice(lista)
print('O aluno(a) escolhido(a) foi o(a)', '\033[1;7m', chute, '\033[m')
