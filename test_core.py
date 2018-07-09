from core import *


def test_new_gladiator():
    assert new_gladiator(100, 0, 5, 15) == {
        'health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }

    assert new_gladiator(50, 90, 5, 15) == {
        'health': 50,
        'rage': 90,
        'damage_low': 5,
        'damage_high': 15
    }


def test_attack():
    assert attack({
        'health': 100,
        'rage': 0,
        'damage_low': 10,
        'damage_high': 10
    }, {
        'health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }) == 90

    assert attack({
        'health': 100,
        'rage': 100,
        'damage_low': 10,
        'damage_high': 10
    }, {
        'health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }) == 80


def test_heal():
    assert heal({
        'health': 79,
        'rage': 30,
        'damage_low': 5,
        'damage_high': 15
    }) == 89

    assert heal({
        'health': 100,
        'rage': 30,
        'damage_low': 5,
        'damage_high': 15
    }) == 100

    assert heal({
        'health': 79,
        'rage': 15,
        'damage_low': 5,
        'damage_high': 15
    }) == 'Insufficient rage'


def test_is_dead():
    assert is_dead({
        'health': 0,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }) == True

    assert is_dead({
        'health': 1,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }) == False
