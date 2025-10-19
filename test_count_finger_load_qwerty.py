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

def test_count_finger_load_lowercase():
    text = "ф"
    result = count_finger_load_qwerty(text)
    # leftfinger5 должен быть 1, остальные 0
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected

def test_count_finger_load_uppercase():
    text = "Ф"  # заглавная → требует shift
    result = count_finger_load_qwerty(text)
    # leftfinger5 (для 'ф') + leftfinger5 (shift) → total 2 для leftfinger5?
    # Но в коде shift — отдельный палец: 'leftfinger5' (тот же!)
    # В вашей раскладке shift — это 'leftfinger5', так что:
    assert qwerty_finger_count['leftfinger5'] == 2

def test_count_finger_load_dop_char():
    text = "!"
    result = count_finger_load_qwerty(text)
    # '!' → leftfinger5 (dop), и flag_nado=1 → shift тоже leftfinger5
    assert qwerty_finger_count['leftfinger5'] == 2
