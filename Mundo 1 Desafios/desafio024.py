cnormal = input('Digite o \033[1;36;7mnome de uma cidade\033[m: ')
csemespacos = cnormal.strip()
clista = csemespacos.split()
print('A cidade \033[36;1m{}\033[m começa com \033[33m"SANTO"\033[m: {}'.format(csemespacos, 'santo' in clista[0].lower()))