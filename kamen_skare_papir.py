import random

try:
    igrac_1 = int(input('Krećemo s igrom! Za kamen izaberi 1, za škare 2, a za papir 3! Za izlaz pritisni x! '))
except:
    print('Vidimo se drugi put!')
igrac_2 = random.randint([1,3])

while igrac_1 != 'x':
    try:
        if igrac_1 == 1 and igrac_2 == 2:
            print('Koji si ti luzer...')
            igrac_1 = int(input('Ako želiš nastaviti za kamen izaberi 1, za škare 2, a za papir 3... Za izlaz pritisni x!'))
        elif igrac_1 == 2 and igrac_2 == 3:
            print('Koji si ti luzer...')
            igrac_1 = int(input('Ako želiš nastaviti za kamen izaberi 1, za škare 2, a za papir 3... Za izlaz pritisni x!'))
        elif igrac_1 == 3 and igrac_2 == 1:
            print('Koji si ti luzer...')
            igrac_1 = int(input('Ako želiš nastaviti za kamen izaberi 1, za škare 2, a za papir 3... Za izlaz pritisni x!'))
        else:
            print('Nice job!')
    except:
        print('Do sljedećeg susreta!')


