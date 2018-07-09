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
    crit_chance = randint(attack['rage'], 100)
    if crit_chance == 100:
        defender['health'] = defender['health'] - attack * 2
        attacker['rage'] = 0
    else:
        defender['health'] = defender['health'] - attack
        attacker['rage'] += 15
