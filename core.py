from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator1 = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return gladiator1


def attack(attacker, defender):
    attack = randint(attacker['damage_low'], attacker['damage_high'])
    if attacker['rage'] >= randint(1, 100):
        defender['health'] = max(defender['health'] - attack * 2, 0)
        attacker['rage'] = 0
        #testing function
        #return defender['health']
    else:
        defender['health'] = max(defender['health'] - attack, 0)
        attacker['rage'] += 15
        #testing function
        #return defender['health']


def heal(gladiator):
    if gladiator['rage'] >= 20:
        gladiator['health'] = min(gladiator['health'] + 10, 100)
        gladiator['rage'] -= 20
        #testing function
        #return gladiator['health']
    else:
        print('Insufficient rage')
        #testing function
        #return 'Insufficient rage'


def is_dead(gladiator):
    gladiator['health'] == 0
    #testing function
    #if gladiator['health'] == 0:
    #    return True
    #else:
    #    return False
