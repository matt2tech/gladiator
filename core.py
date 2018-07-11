from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator1 = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return gladiator1


def attack(attacker, defender, player, other_player):
    attack = randint(attacker['damage_low'], attacker['damage_high'])
    accuracy = randint(1, 100)
    if accuracy > 15:
        if attacker['rage'] >= randint(1, 100):
            print('{} rages, slings the controller and hits {} in the head'.
                  format(player, other_player))
            print('( -_-)つ --===B(҂T-T)')
            defender['health'] = max(defender['health'] - attack * 2, 0)
            attacker['rage'] = 0
            #testing function
            #return defender['health']
        else:
            defender['health'] = max(defender['health'] - attack, 0)
            attacker['rage'] = min(attacker['rage'] + 10, 100)
            print('( ಠ_ಠ)⊃o-|===>(ಠ╭╮ಠ )')
            #testing function
            #return defender['health']
    else:
        print('{} missed'.format(player))
        print('!!!( O.O)⊃o-|===> ε=ε=ε=┌( ^-^)ﾉ')


def heal(gladiator):
    if gladiator['rage'] > 0:
        gladiator['health'] = min(
            gladiator['health'] + int(gladiator['rage'] * 0.75), 100)
        gladiator['rage'] -= gladiator['rage']
        print('(* .*)=[HP^]')
        #testing function
        #return gladiator['health']
    else:
        print(
            'Not angry enough to down those disgusting health potions\n"Rage required"'
        )
        print('¯\_(o-o)_/¯')
        #testing function
        #return 'Insufficient rage'


def rampage(attacker, defender, player, other_player):
    if attacker['rage'] == 100:
        accuracy = randint(1, 100)
        if accuracy > 50:
            defender['health'] = max(defender['health'] - 50, 0)
            attacker['rage'] = 0
            print(
                '{} unleashed built-up rage, went on a rampaged and severely injured {}'.
                format(player, other_player))
            print("（╯°□ °）╯︵( .o.)")

        else:
            attacker['rage'] = 0
            print(
                '{} attempted to go on a rampage but tripped and faceplanted'.
                format(player))
            print('(#;-;)')
    else:
        print(
            '{} attempted to go on a rampage but wasn\'t angry enough\n"requires 100 Rage"'.
            format(player))
        print('¯\_(o-o)_/¯')


def is_dead(gladiator):
    return gladiator['health'] == 0
