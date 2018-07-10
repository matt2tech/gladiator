from core import *


def get_name():
    name = input('First player\'s name? ').strip().capitalize()
    return name


def get_name2():
    name = input('Second player\'s name? ').strip().capitalize()
    return name


def player():
    player = new_gladiator(100, 0, 5, 15)
    return player


def player_turn(player, other_player, name):
    text = ''
    while text != '4':
        text = input(
            'It is {}\'s move.\n1 - attack\n2 - pass\n3 - heal\n4- quit\n>>> '.
            format(name))
        if text == '1':
            attack(player, other_player)
            print(other_player['health'])
            break

        elif text == '2':
            break

        elif text == '3':
            break

        elif text == '4':
            return True

        else:
            print('Invalid move')
            print(
                '\n---------------------------------------------------------------\n'
            )


def battle(first_player, second_player, player1, player2):
    status = ''
    while status != True:
        status = is_dead(player1)
        print('{}: {} HP ||| {} Rage\n{}: {} HP ||| {} Rage'.format(
            first_player, player1['health'], player1['rage'], second_player,
            player2['health'], player2['rage']))
        player_turn(player1, player2, first_player)
        print(
            '\n---------------------------------------------------------------\n'
        )
        status = is_dead(player2)

        print('{}: {} HP ||| {} Rage\n{}: {} HP ||| {} Rage'.format(
            first_player, player1['health'], player1['rage'], second_player,
            player2['health'], player2['rage']))
        player_turn(player2, player1, second_player)
        print(
            '\n---------------------------------------------------------------\n'
        )


def main():

    first_player = get_name()
    second_player = get_name2()
    player1 = player()
    player2 = player()

    battle(first_player, second_player, player1, player2)


if __name__ == '__main__':
    main()
