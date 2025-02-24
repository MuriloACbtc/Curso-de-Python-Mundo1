
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    if n1 > n3:
        print('{} é o maior número'.format(n1))
        if n2 > n3:
            print('{} é o menor número'.format(n3))
        else:
            print(n2, 'é o menor número')
    else:
        print(n3, 'é o maior número')
        if n1 > n2:
            print(n2, 'é o menor número')
        else:
            print('{} é o menor número'.format(n1))
else:
    if n2 > n3:
        print('{} é o maior número'.format(n2))
        if n1 > n3:
            print(n3, 'é o menor número')
        else:
            print('{} é o menor número'.format(n1))
    else:
        print('{} é o maior número'.format(n3))
        if n2 > n1:
            print('{} e o menor número'.format(n1))
        else:
            print(n2, 'é o menor número')
