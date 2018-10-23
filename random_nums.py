from random import randint

attempts = 0
points = 0
misses = 0

try:
    
    def random_math(choise):
        
        global points
        global misses
        global attempts

        a = randint(6, 100)
        b = randint(1, 5)
        
        def plus():
            summa = a + b
            return summa
    
        def minus():
            summa = a - b
            return summa
    
        def multiply():
            summa = a * b
            return summa
    
    
        choise_of_math = {
               'plus': plus(),
               'minus': minus(),
               'multiply': multiply(),
               }
    
        
        sign = {'plus': '+',
               'minus': '-',
               'multiply': '*',
               }
    
        turn_out = choise_of_math.get(choise)
        symbol = sign.get(choise)
        
        print(f"how much is {a} {symbol} {b}?")
    
        answer = int(input('It will be.... '))
        if answer == turn_out:
            print(f'Yes! {turn_out} is correct.\n') 
            points += 1
        else:
            print(f"No. I am sorry {answer} is not correct.") 
            print(f"It is {turn_out}")
            misses += 1

        attempts += 1
        print(f"You have now: {points} points.\n")

        if attempts < 5:
            random_math(choise)
        else:
            print(f'You have {points} out of {attempts} attempts\n')
            if misses <= attempts / 5:
                print('Well done!\n')

            elif misses >= attempts / 3:
                print('I think you can do better.')

            attempts = 0
            points = 0
            misses = 0


except:
    print("  Good bye!")
    points = 0

