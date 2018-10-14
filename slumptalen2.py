from random import randint

print("""Välkommen! Spela så länge du vill.
Om du vill avsluta så trycker du "Ctrl + C\n""")

c = 0

try:
    
    def slump_matte(choise):
        global c

        a = randint(6, 10)
        b = randint(1, 5)
        
        
        def plus():
            summa = a + b
            return summa

        def minus():
            summa = a - b
            return summa

        def gånger():
            summa = a * b
            return summa

        def delat():
            summa = a / b
            return summa


        val = {'plus': plus(),
               'minus': minus(),
               'gånger': gånger(),
               'delat': delat(),
               }
        
        tecken = {'plus': '+',
               'minus': '-',
               'gånger': '*',
               'delat': '/',
               }

#        choise = input('Välj ett räknesätt! ')
        utfall = val.get(choise)
        symbol = tecken.get(choise)
        
        print(f"Vad blir {a} {symbol} {b}?\n")
        svar = int(input('Det blir: '))
        if svar == utfall:
            print(f'Ja. {utfall} är rätt svar.\n') 
            c += 1
        else:
            print(f"Nej, det var inte rätt. Det ska vara {utfall}, Försök igen!\n")
        print(f"Du har totalt: {c} poäng.\n")
            
        while c < 3:
            slump_matte(choise)

except:
    print("Good bye!")
