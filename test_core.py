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
