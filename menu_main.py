
def main_menu():

    # program options presentation
    MENU_TEXT = open('main_menu_text', 'r')
    print(MENU_TEXT.read())
    MENU_TEXT.close()

    # user inputs the choice
    menu_choice = 1 #int(input())

    if menu_choice == 1: # user_operations method that adds credits to user account
        return 'game'

    elif menu_choice == 2: # user_operations method that enables credits withdrawal
        print('add')

    elif menu_choice == 3: # running slot_machine_insides
        print('withdraw')

    elif menu_choice == 4: # returning to loging screen
        return 'exit'

    else: # forcing correct choice for menu
        print('Please, choose number from 1 to 4.')
        main_menu()


# main_menu()