import random
import time


def machine():
    reels = 3
    symbols = ('SEVEN', 'bell', 'orange', 'lemon', 'twoja stara', 'sun', 'moon', 'phone', 'dog', 'cat', 'PIWSKO')
    payline = []

    for i in range(1, reels + 1):
        reel(i, payline, symbols)
    print('your payline is: ', '\n', payline[0], payline[1], payline[2])
    print(' ')

    if all_same(payline) == True:
        print('O KURWA WYGRAŁ JEBANY HAHA!!!')
        return True

    elif all_same(payline) == False:
        print('You are a fucking loser xD')
        return False

    else:
        pass


def reel(reel_number, payline, symbols):
    for i in range(3):
        print("rolling", reel_number)
        time.sleep(0.5)
    payline.append(random.choice(symbols))
    print(' ')
    print(payline[-1])
    print(' ')


def all_same(payline):
    return all(x == payline[0] for x in payline)
