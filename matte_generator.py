import slumpgenerator

matte = 0

def addition():

    global matte 

    while matte < 3:
        a = slumpgenerator.tal_1()
        b = slumpgenerator.tal_2()
        print(f'how much is {a} + {b}?')
        svar = int(input(':> '))
        if svar == a + b:
            matte += 1
            print(f'Correct. You have {matte} points')

        elif svar != a + b:
            print(f'Not correct! You have still have {matte} points')

    subtraction()

def subtraction():

    global matte 
    
    print(f'Ta daaa! You have {matte} points from previous room.')

addition()

