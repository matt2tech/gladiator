from core import *
from time import sleep


def start_menu():
    while True:
        sleep(0.1)
        print(
            '\n--------------------------------------------------------------------------'
        )
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print(' ___       _   _   _            __   _   _            _')
        sleep(0.1)
        print(
            '| _ ) __ _| |_| |_| |___   ___ / _| | |_| |_  ___    /_\  __ _ ___ ___'
        )
        sleep(0.1)
        print(
            '| _ \/ _` |  _|  _| / -_) / _ \  _| |  _| \' \/ -_)  / _ \/ _` / -_|_-<'
        )
        sleep(0.1)
        print(
            '|___/\__,_|\__|\__|_\___| \___/_|    \__|_||_\___| /_/ \_\__, \___/__/'
        )
        sleep(0.1)
        print('                                                         |___/')
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print('\n')
        sleep(0.1)
        print(
            '--------------------------------------------------------------------------\n'
        )
        sleep(0.1)
        text = input('{:<37}{:>37}\n>>> '.format('1 - Start Game',
                                                 '2 - Quit Game'))
        if text == '1':
            break

        elif text == '2':
            sleep(0.1)
            print('Quitting game...')
            sleep(2)
            print(
                '\n--------------------------------------------------------------------------\n'
            )
            exit()

        else:
            sleep(0.1)
            print('Invalid choice')
            sleep(2)
            print(
                '\n--------------------------------------------------------------------------'
            )


def credits(player1, player2):
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    print('Developer:')
    sleep(0.5)
    print('Matthew Lipsey\n')
    sleep(0.5)
    print('World Artwork:')
    sleep(0.5)
    print('ASCII Art Archive\n')
    sleep(0.5)
    print('Character Artwork:')
    sleep(0.5)
    print('Unicode\n')
    sleep(0.5)
    print('Testers:')
    sleep(0.5)
    print('Henry Moore')
    sleep(0.5)
    print('Cody van der Poel\n')
    sleep(0.5)
    print('Code:')
    sleep(0.5)
    print('Python\n')
    sleep(0.5)
    print('Text Editor:')
    sleep(0.5)
    print('Visual Studio Code\n')
    sleep(0.5)
    print('Special Thanks:')
    sleep(0.5)
    print('Base Camp Coding Academy')
    sleep(0.5)
    print('Player 1: {}'.format(player1))
    sleep(0.5)
    print('Player 2: {}'.format(player2))
    sleep(0.5)
    print('Terminals and command prompts everywhere')
    sleep(2)
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    sleep(0.1)
    print('\t     ___________')
    sleep(0.1)
    print('\t._____l_______l_____.')
    sleep(0.1)
    print('\t||_____/  |  \_____||')
    sleep(0.1)
    print('\t      /   |   \\')
    sleep(0.1)
    print('\t     /    |    \\')
    sleep(0.1)
    print('\t    /     |     \\')
    sleep(0.1)
    print('\t   /      |      \\')
    sleep(0.1)
    print('\t  /       |       \\')
    sleep(0.1)
    print('\t /        |        \\')
    sleep(0.1)
    print('\t|         |         |')
    sleep(0.1)
    print('\t \        |        /')
    sleep(0.1)
    print('\t   \      |      /')
    sleep(0.1)
    print('\t     \    |    /')
    sleep(0.1)
    print('\t       \  |  /')
    sleep(0.1)
    print('\t         \|/')
    sleep(0.1)
    print('\t          `')
    sleep(0.1)
    print('Thanks for playing Battle of the Ages')
    sleep(2)
    main()


def loading_screen():
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    sleep(0.1)
    print('Loading Battle of the Ages...\n')
    sleep(2)
    print("                  [\\")
    sleep(0.1)
    print("                  |\)                                ____")
    sleep(0.1)
    print("                  |                               __(_   )__")
    sleep(0.1)
    print("                  Y\          ___               _(          )")
    sleep(0.1)
    print("                 T  \       __)  )--.          (     )-----`")
    sleep(0.1)
    print("                J    \   ,-(         )_         `---'")
    sleep(0.1)
    print("               Y/T`-._\ (     (       _)                 __")
    sleep(0.1)
    print("               /[|   ]|  `-(__  ___)-`  |\          ,-(  __)")
    sleep(0.1)
    print("               | |    |      (__)       J'         (     )")
    sleep(0.1)
    print("   _           | |  ] |    _           /;\          `-  '")
    sleep(0.1)
    print("  (,,)        [| |    |    L'         /;  \\")
    sleep(0.1)
    print("             /||.| /\ |   /\         /.,-._\        ___ _")
    sleep(0.1)
    print("            /_|||| || |  /  \        | |{  |       (._.'_)")
    sleep(0.1)
    print("  L/\       | \| | '` |_ _ {|        | | U |   /\\")
    sleep(0.1)
    print(" /v^v\/\   `|  Y | [  '-' '--''-''-\"-'`'   | ,`^v\ /\,`\\")
    sleep(0.1)
    print("/ ,'./  \.` |[   |       [     __   L    ] |      /^v\  \\")
    sleep(0.1)
    print(",'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_")
    sleep(0.1)
    print("--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y")
    sleep(0.1)
    print("   Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-'  _  (^)__  _")
    sleep(0.1)
    print("  Y  YY   ;'~~l  |   L     [|\###U'E'\  \ \Y-` _  (^) _Y  _")
    sleep(0.1)
    print(" Y  Y Y   ;\~~/\{| [      _,'-\`= = '.\_ ,`   (^)(^) (^) (^)")
    sleep(0.1)
    print("     --   ;\~~~/\|  _,.-'`_  `.\_..-'\"  _ . ,_ Y_ Y_ _Y  _Y__")
    sleep(0.1)
    print("    _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^)")
    sleep(0.1)
    print("   (^)  (^)`._~ /  L \  _.Y'`  _  ` --  Y - - -(^) - Y - Y -")
    sleep(0.1)
    print("    Y    Y    `'--..,-'`      (^)   _  -    _   Y ____")
    sleep(0.1)
    print("      --           _    _ --   Y   (^)   _ (^)  ===   ----")
    sleep(0.1)
    print("          __   -  (^)  (^)      --- Y   (^) Y")
    sleep(0.1)
    print("      _            Y    Y                Y             ")
    sleep(0.1)
    print('Initializing...')
    sleep(2)


def get_name():
    name = input('Contestant #1\'s name? ').strip()
    return name


def get_name2():
    sleep(1)
    name = input('Contestant #2\'s name? ').strip()
    return name


def player():
    player = new_gladiator(100, 0, 5, 15, 15)
    return player


def player_turn(player, other_player, name, other_name):
    text = ''
    while True:
        text = input(
            'It is {}\'s move.\n1 - attack\n2 - wait\n3 - heal\n4 - rampage\n5 - evade\n>>> '.
            format(name))
        if text == '1':
            attack(player, other_player, name, other_name)
            break

        elif text == '2':
            player['rage'] = min(player['rage'] + 20, 100)
            print('{} is waiting'.format(name))
            print('(ง-_-)ง')
            break

        elif text == '3':
            heal(player, name)
            break

        elif text == '4':
            rampage(player, other_player, name, other_name)
            break

        elif text == '5':
            evading(player, name)
            break

        else:
            print('Invalid move\n"The crowd is not pleased"')
            print('(-(-_(-_-)_-)-)')
            sleep(1)
            print(
                '\n--------------------------------------------------------------------------\n'
            )


def evading_reset(player):
    player['evasion'] = 15


def battle(first_player, second_player, player1, player2):
    status = ''
    while status != True:
        evading_reset(player1)
        print('{}: {} HP ||| {} Rage\n{}: {} HP ||| {} Rage'.format(
            first_player, player1['health'], player1['rage'], second_player,
            player2['health'], player2['rage']))
        player_turn(player1, player2, first_player, second_player)
        sleep(1)
        print(
            '\n--------------------------------------------------------------------------\n'
        )
        status = is_dead(player2)
        if status == True:
            print('{} has fallen\n{} wins'.format(second_player, first_player))
            print('ᕦ(ˇò_ó)ᕤ (✖╭╮✖ )')
            sleep(2)
            break

        evading_reset(player2)
        print('{}: {} HP ||| {} Rage\n{}: {} HP ||| {} Rage'.format(
            first_player, player1['health'], player1['rage'], second_player,
            player2['health'], player2['rage']))
        player_turn(player2, player1, second_player, first_player)
        sleep(1)
        print(
            '\n--------------------------------------------------------------------------\n'
        )
        status = is_dead(player1)
        if status == True:
            print('{} has fallen\n{} wins'.format(first_player, second_player))
            print('( ✖╭╮✖) ᕦ(ò_óˇ)ᕤ')
            sleep(2)
            break


def battle_announce(player, other_player):
    sleep(2)
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    sleep(0.1)
    print('\t     |\                 /)')
    sleep(0.1)
    print('\t   /\_\\\__           (_//')
    sleep(0.1)
    print('\t  |   `>\-`   _._     //`)')
    sleep(0.1)
    print('\t   \ /` \\\_.-`:::`-._//')
    sleep(0.1)
    print('\t    `   |`    :::    `|')
    sleep(0.1)
    print('\t        |     :::     |')
    sleep(0.1)
    print('\t        |.....:::.....|')
    sleep(0.1)
    print('\t        |:::::::::::::|')
    sleep(0.1)
    print('\t        |     :::     |')
    sleep(0.1)
    print('\t        \     :::     /')
    sleep(0.1)
    print('\t         \    :::    /')
    sleep(0.1)
    print('\t          `-. ::: .-\'')
    sleep(0.1)
    print('\t            //\:/\\\\')
    sleep(0.1)
    print('\t           //  \'  \\\\')
    sleep(0.1)
    print('\t          |/       \\\\\n')
    sleep(2)
    print('WELCOME TO THE BATTLE OF THE AGES\n'.center(50))
    sleep(2)
    print('From zero to hero, the legendary {}\n'.format(player).center(51))
    sleep(2)
    print('From unknown to famous, the all-star {}\n'.format(other_player)
          .center(51))
    sleep(2)
    print('{} vs. {}! Let the battle begin!'.format(player,
                                                    other_player).center(50))
    sleep(1)
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    sleep(2)


def sign_up():
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    sleep(0.1)
    print('\n\t(\ ')
    sleep(0.1)
    print('\t\\\'\\ ')
    sleep(0.1)
    print('\t \\\'\\      __________  ')
    sleep(0.1)
    print('\t / \'|    ()_________)')
    sleep(0.1)
    print('\t \\ \'/    \\  Sign-Up \\')
    sleep(0.1)
    print('\t   \\      \\ ~~~~~~~~ \\')
    sleep(0.1)
    print('\t   ==).    \\__________\\')
    sleep(0.1)
    print('\t  (__)    ()__________)\n')
    sleep(0.5)


def trophy():
    sleep(0.1)
    print('\n\n                                  ___________')
    sleep(0.1)
    print('                             .---\'::\'        `---.')
    sleep(0.1)
    print('                            (::::::\'              )')
    sleep(0.1)
    print('                            |`-----._______.-----\'|')
    sleep(0.1)
    print('                           /￣             ::::::￣\\')
    sleep(0.1)
    print('                          / _               ::::::_ \\')
    sleep(0.1)
    print('                         / /|               ::::::|\\ \\')
    sleep(0.1)
    print('                        | | |               ::::::| | |')
    sleep(0.1)
    print('                        | | |       Champion::::::| | |')
    sleep(0.1)
    print('                         \ \|     of the Arena::::|/ /')
    sleep(0.1)
    print('                          \ ￣               ::::￣ /')
    sleep(0.1)
    print('                           \_              .::::::_/')
    sleep(0.1)
    print('                            |              :::::::|')
    sleep(0.1)
    print('                             \            :::::::/')
    sleep(0.1)
    print('                              `.        .:::::::\'')
    sleep(0.1)
    print('                                `-._  .:::::;-\'')
    sleep(0.1)
    print(
        '____________________________________|  """|"______________________________'
    )
    sleep(0.1)
    print('                                    |  :::|')
    sleep(0.1)
    print('                                    |   ::|')
    sleep(0.1)
    print('                                   /     ::\\ ')
    sleep(0.1)
    print('                              __.-\'      :::`-.__')
    sleep(0.1)
    print('                             (_           ::::::_)')
    sleep(0.1)
    print('                               `"""---------"""\'')
    sleep(0.1)
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    sleep(2)


def main():
    start_menu()

    loading_screen()

    sign_up()

    first_player = get_name()
    second_player = get_name2()
    player1 = player()
    player2 = player()

    battle_announce(first_player, second_player)

    battle(first_player, second_player, player1, player2)

    trophy()

    credits(first_player, second_player)


if __name__ == '__main__':
    main()
