import slump_matte
from random import randint

tal1 = randint(1,5)
tal2 = randint(6, 10)

def valet():
    raknesatten = {
            'plus': slump_matte.plus(tal1,tal2),
            'minus': slump_matte.minus(tal1, tal2),
            'gånger': slump_matte.multiplikation(tal1, tal2),
            'delat': slump_matte.division(tal1, tal2)
            }

    tecken = {
            'plus': '+',
            'minus': '-',
            'gånger': '*',
            'delat': '/'
            }

    räknevalet = input('välj ett räknesätt:> ')
    print(f"{tal1} {tecken.get(räknevalet)} {tal2} blir {raknesatten.get(räknevalet)}")

    
def samman_rakning():
     print(tal1, tal2)
#     summering = input('vad blir det tillsammans? :> ')
#     if summering == slump_matte.plus(tal1, tal2):
#         print('korrekt')
 
samman_rakning()
valet()
