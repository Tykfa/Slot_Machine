import login_screen as ls

def main_menu():

    # program options presentation
    print(' ', 'Welcome to slot machine main menu.',
    '----------------------------------',
    '1. Add credits',
    '2. Withdraw credits',
    '3. Start game',
    '3. Log out',
    '----------------------------------', sep = '\n')

    # user inputs the choice
    menu_choice = int(input())

    if menu_choice == 1: # user_operations method that adds credits to user account
        print(1)

    elif menu_choice == 2: # user_operations method that enables credits withdrawal
        print(2)

    elif menu_choice == 3: # running slot_machine_insides
        print(3)

    elif menu_choice == 4: # returning to loging screen
        print(4)

    else: # forcing correct choice for menu
        print('Please, choose number from 1 to 4.')
        main_menu()


main_menu()