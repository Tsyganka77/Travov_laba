import pytest
from function import (
    find_finger,
    count_finger_load_qwerty,
    load_hand_left,
    load_hand_right,
    clicks,
    calculate_penalties,
    keyboard_finger_qwerty,
    keyboard_finger_qwerty_dop,
    qwerty_finger_count,
    key_grid,
    valid_keys,
    ignore_chars,
    key_to_home_finger
)

# Сброс глобального состояния перед каждым тестом
@pytest.fixture(autouse=True)
def reset_finger_count():
    for key in qwerty_finger_count:
        qwerty_finger_count[key] = 0

def test_find_finger_main_layout():
    finger, flag = find_finger('ф', keyboard_finger_qwerty)
    assert finger == 'leftfinger5'
    assert flag == 0

def test_find_finger_dop_layout():
    finger, flag = find_finger('!', keyboard_finger_qwerty)
    assert finger == 'leftfinger5'
    assert flag == 1

def test_find_finger_invalid_char():
    result, flag = find_finger('月', keyboard_finger_qwerty)
    assert result == "Invalid character: 月"
    assert flag == 0

def test_find_finger_non_qwerty_no_dop():
    fake_layout = {"leftfinger5": "abc"}
    result, flag = find_finger('!', fake_layout)
    assert result == "Invalid character: !"
    assert flag == 0
