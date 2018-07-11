from core import *
from time import sleep


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
    print('''\t   |\                     /)
\t /\_\\\__               (_//
\t|   `>\-`     _._       //`)
\t \ /` \\\  _.-`:::`-._  //
\t  `    \|`    :::    `|/
\t        |     :::     |
\t        |.....:::.....|
\t        |:::::::::::::|
\t        |     :::     |
\t        \     :::     /
\t         \    :::    /
\t          `-. ::: .-'
\t           //`:::`\\\\
\t          //   '   \\\\
\t         |/         \\\\
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
                                `-._  .::::::-'
____________________________________|  """|"______________________________
                                    |  :::|
                                    |   ::|
                                   /     ::\               
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `"""---------"""'
''')


if __name__ == '__main__':
    main()
