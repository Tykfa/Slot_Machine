import slot_machine_insides as smi
import calculations as calc
import menu as mn


def main():

    mn.main_menu()


    # user inserts credits to be bet
    # bet = int(input('insert amount of credits to enter the game: '))
    bet = 5

    # result of the draw
    result = smi.machine(smi.reels, smi.symbols, smi.payline)


    # activating the calculation based on result
    if  result == True:
        print(calc.winning(bet, calc.multiplier))

    elif result == False:
        print(calc.losing(bet))

    else:
        pass


if __name__ == '__main__':
    main()
