import slump_matte
from random import randint

points = 0
errors = 0

a = randint(6, 10)
b = randint(1, 5)

def valet():

    global points, errors

    raknesatten = {
            'plus': slump_matte.plus(a, b),
            'minus': slump_matte.minus(a, b),
            'gånger': slump_matte.multiplikation(a, b),
            'delat': slump_matte.division(a, b)
            }

    tecken = {
            'plus': '+',
            'minus': '-',
            'gånger': '*',
            'delat': '/'
            }

    while points < 3:
        arithemtic = input('välj räknesätt:> ')
        print(f'vad blir {a} {tecken.get(arithemtic)} {b} ?')
        raknesatt = raknesatten.get(arithemtic)
        if raknesatt == 'delat':
            gissning = float(input('summa? '))
        else:
            gissning = int(input('summa? '))

        if raknesatt == gissning:
            print('rätt')
            points += 1
            print(points)
        else:
            print('fel')
            errors += 1
            print(errors)
            print(raknesatt, 'raknesatt2') 
    
valet()
