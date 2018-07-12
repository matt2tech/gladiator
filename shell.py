from core import *
from time import sleep


def credits(player1, player2):
    text = input('1 - Roll credits\n2 - Replay\n')
    if text == '1':
        sleep(1)
        print(
            '\n--------------------------------------------------------------------------\n'
        )
        print('Developer:')
        sleep(1)
        print('Matthew Lipsey\n')
        sleep(1)
        print('World Artwork:')
        sleep(1)
        print('ASCII Art Archive\n')
        sleep(1)
        print('Character Artwork:')
        sleep(1)
        print('Unicode\n')
        sleep(1)
        print('Testers:')
        sleep(1)
        print('Henry Moore')
        sleep(1)
        print('Cody van der Poel\n')
        sleep(1)
        print('Code:')
        sleep(1)
        print('Python\n')
        sleep(1)
        print('Text Editor:')
        sleep(1)
        print('Visual Studio Code\n')
        sleep(1)
        print('Special Thanks:')
        sleep(1)
        print('Base Camp Coding Academy')
        sleep(1)
        print('Player 1: {}'.format(player1))
        sleep(1)
        print('Player 2: {}'.format(player2))
        sleep(1)
        print('Computer terminals and command prompts everywhere\n')
        print(
            '\n--------------------------------------------------------------------------\n'
        )
        sleep(2)
        print('\t     ___________')
        sleep(1)
        print('\t._____l_______l_____.')
        sleep(1)
        print('\t||_____/  |  \_____||')
        sleep(1)
        print('\t      /   |   \\')
        sleep(1)
        print('\t     /    |    \\')
        sleep(1)
        print('\t    /     |     \\')
        sleep(1)
        print('\t   /      |      \\')
        sleep(1)
        print('\t  /       |       \\')
        sleep(1)
        print('\t /        |        \\')
        sleep(1)
        print('\t|         |         |')
        sleep(1)
        print('\t \        |        /')
        sleep(1)
        print('\t   \      |      /')
        sleep(1)
        print('\t     \    |    /')
        sleep(1)
        print('\t       \  |  /')
        sleep(1)
        print('\t         \|/')
        sleep(1)
        print('\t          `')
        sleep(1)
        print('Thanks for playing Battle of the Ages')
        sleep(1)


def loading_screen():
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    print('Loading Battle of the Ages...\n')
    sleep(2)
    print("                  [\\")
    sleep(1)
    print("                  |\)                                ____")
    sleep(1)
    print("                  |                               __(_   )__")
    print("                  Y\          ___               _(          )")
    sleep(2)
    print("                 T  \       __)  )--.          (     )-----`")
    print("                J    \   ,-(         )_         `---'")
    print("               Y/T`-._\ (     (       _)                 __")
    print("               /[|   ]|  `-(__  ___)-`  |\          ,-(  __)")
    print("               | |    |      (__)       J'         (     )")
    print("   _           | |  ] |    _           /;\          `-  '")
    print("  (,,)        [| |    |    L'         /;  \\")
    sleep(3)
    print("             /||.| /\ |   /\         /.,-._\        ___ _")
    print("            /_|||| || |  /  \        | |{  |       (._.'_)")
    print("  L/\       | \| | '` |_ _ {|        | | U |   /\\")
    sleep(1)
    print(" /v^v\/\   `|  Y | [  '-' '--''-''-\"-'`'   | ,`^v\ /\,`\\")
    print("/ ,'./  \.` |[   |       [     __   L    ] |      /^v\  \\")
    print(",'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_")
    sleep(2)
    print("--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y")
    print("   Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-'  _  (^)__  _")
    print("  Y  YY   ;'~~l  |   L     [|\###U'E'\  \ \Y-` _  (^) _Y  _")
    print(" Y  Y Y   ;\~~/\{| [      _,'-\`= = '.\_ ,`   (^)(^) (^) (^)")
    sleep(1)
    print("     --   ;\~~~/\|  _,.-'`_  `.\_..-'\"  _ . ,_ Y_ Y_ _Y  _Y__")
    print("    _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^)")
    print("   (^)  (^)`._~ /  L \  _.Y'`  _  ` --  Y - - -(^) - Y - Y -")
    sleep(1)
    print("    Y    Y    `'--..,-'`      (^)   _  -    _   Y ____")
    print("      --           _    _ --   Y   (^)   _ (^)  ===   ----")
    print("          __   -  (^)  (^)      --- Y   (^) Y")
    sleep(2)
    print("      _            Y    Y                Y             ")


def get_name():
    name = input('Contestant #1\'s name? ').strip()
    return name


def get_name2():
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
            break


def battle_announce(player, other_player):
    sleep(2)
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    print('''\t     |\                 /)
\t   /\_\\\__           (_//
\t  |   `>\-`   _._     //`)
\t   \ /` \\\_.-`:::`-._//
\t    `   |`    :::    `|
\t        |     :::     |
\t        |.....:::.....|
\t        |:::::::::::::|
\t        |     :::     |
\t        \     :::     /
\t         \    :::    /
\t          `-. ::: .-'
\t            //\:/\\\\
\t           //  '  \\\\
\t          |/       \\\\
''')
    print('WELCOME TO THE BATTLE OF THE AGES\n'.center(50))
    sleep(2)
    print('From zero to hero, the legendary {}\n'.format(player).center(51))
    sleep(2)
    print('From unknown to famous, the all-star {}\n'.format(other_player)
          .center(51))
    sleep(2)
    print('{} vs. {}! Let the battle begin!'.format(player,
                                                    other_player).center(50))
    sleep(2)
    print(
        '\n--------------------------------------------------------------------------\n'
    )


def main():
    loading_screen()
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    print('''\n\t(\ 
\t\\'\ 
\t \\'\      __________  
\t / '|    ()_________)
\t \ '/    \  Sign-Up \\
\t   \      \ ~~~~~~~~ \\
\t   ==).    \__________\\
\t  (__)    ()__________)\n''')
    first_player = get_name()
    second_player = get_name2()
    player1 = player()
    player2 = player()

    battle_announce(first_player, second_player)

    battle(first_player, second_player, player1, player2)

    sleep(2)
    print('''\n\n                                  ___________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                           /￣             ::::::￣\\
                          / _               ::::::_ \\
                         / /|               ::::::|\\ \\
                        | | |               ::::::| | |
                        | | |       Champion::::::| | |
                         \ \|     of the Arena::::|/ /
                          \ ￣               ::::￣ /
                           \_              .::::::_/
                            |              :::::::|
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .:::::;-'
____________________________________|  """|"______________________________
                                    |  :::|
                                    |   ::|
                                   /     ::\               
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `"""---------"""'
''')
    print(
        '\n--------------------------------------------------------------------------\n'
    )
    credits(first_player, second_player)


if __name__ == '__main__':
    main()
