f = str(input('Digite \033[41;30muma\033[m \033[31mfrase\033[m: ')).strip()
na = f.lower().count('a')
primeiroa = f.lower().find('a')
ultimoa = f.lower().rfind('a')
print('''A frase tem \033[31m{} letra(s) "a"\033[m,
 aparecendo pela \033[33mprimeira vez\033[m na posição {},
 e na \033[33múltima vez\033[m na posição {}'''.format(na, primeiroa + 1, ultimoa + 1))