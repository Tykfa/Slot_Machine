# plik ma za zadanie zebrać mainy wszystkich funkcji i je skoordynować
# Odpala menu główne i na podstawie wyboru gracza odpala main gry lub zamyka program


import menu_main as mn
import game_main as gm


def main():


    a = mn.main_menu()
    if a == 'game':
        gm.game_interface()
    elif a == 'exit':
        print('Goodbye')
        exit()
    else:
        raise NameError('Choice not yet implemented')




if __name__ == '__main__':
    main()
