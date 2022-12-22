import random
import time

# characteristics of machine defined
REELS = 3
SYMBOLS = ('SEVEN' , 'bell', 'orange', 'lemon', 'twoja stara', 'PIWSKO')
payline = []


def machine(REELS, SYMBOLS, payline):

    # activating individual reels
    for i in range(1, REELS + 1):
        reel(i, payline, SYMBOLS)

    # printing result of all draws
    print('your payline is: ', '\n')
    print( payline[0], payline[1], payline[2], sep=(', '))
    print(' ')

    # checking if result is wining or losing
    if all_same(payline) == True:
        print('O KURWA WYGRAŁ JEBANY HAHA!!!')
        return True

    elif all_same(payline) == False:
        print('You are a fucking loser xD')
        return False

    else:
        pass


def reel(reel_number, payline, SYMBOLS):

    # cosmetic for user representing rollin of physical reel in a machine
    for i in range(3):
        print("rolling", reel_number)
        time.sleep(0.1)

    # transmission of the draw result to list of results and printing individual result
    payline.append(random.choice(SYMBOLS))
    print(' ')
    print(payline[-1])
    print(' ')


def all_same(payline):
    return all(x == payline[0] for x in payline)
