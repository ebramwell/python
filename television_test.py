import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert not tv.is_on
    assert tv.channel == 1

def test_turn_on():
    tv = Television()
    tv.turn_on()
    assert tv.is_on

def test_turn_off():
    tv = Television()
    tv.turn_on()
    tv.turn_off()
    assert not tv.is_on

def test_change_channel():
    tv = Television()
    tv.turn_on()
    tv.set_channel(5)
    assert tv.channel == 5

def test_invalid_channel():
    tv = Television()
    tv.turn_on()
    with pytest.raises(ValueError):
        tv.set_channel(999)
