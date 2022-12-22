# ma przyjmowć informacje że zostaje odpalona gra
# pobiera od użytkownika ile stawia
# użytkownik ciągnie wajchę - odpala sie mechanizm gry
# mechanizm zwraca inf o wygranej/przegranej do przelicznika
# przelicznik zwraca rezultat gry


import slot_machine_insides as smi
import calculations as calc


def game_interface():

    # printing game menu
    MENU_TEXT = open('game_menu_text', 'r')
    print(MENU_TEXT.read())
    MENU_TEXT.close()

    menu_choice = int(input())
    if menu_choice == 1:
        # user inserts credits to be bet

        bet = input('insert amount of credits to enter the game: ')
        input('Pull the lever')

        # result of the draw
        result = smi.machine(smi.REELS, smi.SYMBOLS, smi.payline)

        # activating the calculation based on result
        if result == True:
            print(calc.add_credits(bet, calc.MULTIPLIER))
            input('Press any button to  continue...')

        elif result == False:
            print(bet, 'lost')
            input('Press any button to  continue...')

        else:
            pass

        game_interface()


    elif menu_choice == 2:
        print('Goodbye')
        exit()

    else:
        raise NameError('Wrong choice')
