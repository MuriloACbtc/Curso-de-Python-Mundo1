nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
média = (nota1 + nota2) / 2
print('A \033[1mmédia\033[m do aluno é \033[1;33m{:.2f}\033[m, \ne teve as notas \033[1;37m{}\033[m e \033[1;37m{}\033[m.'.format(média, nota1, nota2))

