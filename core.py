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
    if attacker['rage'] > randint(1, 100):
        defender['health'] = defender['health'] - attack * 2
        attacker['rage'] = 0
        return defender['health']
    else:
        defender['health'] = defender['health'] - attack
        attacker['rage'] += 15
        return defender['health']
