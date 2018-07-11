from random import randint


def new_gladiator(health, rage, damage_low, damage_high, evasion):
    gladiator1 = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high,
        'evasion': 15
    }
    return gladiator1


def attack(attacker, defender, player, other_player):
    attack = randint(attacker['damage_low'], attacker['damage_high'])
    accuracy = randint(1, 100)
    if accuracy > defender['evasion']:
        if attacker['rage'] >= randint(1, 100):
            print('{} rages, slings the controller and hits {} in the head'.
                  format(player, other_player))
            print('( -_-)つ -=≡~B(҂T-T)')
            defender['health'] = max(defender['health'] - attack * 2, 0)
            attacker['rage'] = 0
            #testing function
            #return defender['health']
        else:
            defender['health'] = max(defender['health'] - attack, 0)
            attacker['rage'] = min(attacker['rage'] + 10, 100)
            print('{} hit {}'.format(player, other_player))
            print('( ಠ_ಠ)⊃o-|===>(ಠ╭╮ಠ )')
            #testing function
            #return defender['health']
    else:
        print('{} missed'.format(player))
        print('( ÒДÓ)⊃o-|===> ε=ε=ε=┌( ^-^)ﾉ')


def heal(gladiator, name):
    if gladiator['rage'] > 0:
        gladiator['health'] = min(
            gladiator['health'] + int(gladiator['rage'] * 0.75), 100)
        gladiator['rage'] -= gladiator['rage']
        print('{} drunk a potion'.format(name))
        print('(* .*)=[HP^]')
        #testing function
        #return gladiator['health']
    else:
        print(
            '{} attempted to drink a potion but couldn\'t stomach it\n"Rage required"'.
            format(name))
        print('(°Д°)')
        #testing function
        #return 'Insufficient rage'


def rampage(attacker, defender, player, other_player):
    if attacker['rage'] == 100:
        accuracy = randint(1, 100)
        if accuracy > defender['evasion'] + 35:
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


def evading(gladiator, name):
    if gladiator['rage'] > 0:
        gladiator['evasion'] = min(
            gladiator['evasion'] + gladiator['rage'] / 3, 100)
        gladiator['rage'] = 0
        print('{} is evading'.format(name))
        print('ε=ε=ε=┌( o-o)ﾉ')

    else:
        print('{} attempted to evade but tripped over a pebble'.format(name))
        print('.︵ /(.□ . \）')
