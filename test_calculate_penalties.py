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

def test_calculate_penalties_empty():
    assert calculate_penalties("") == 0
    assert calculate_penalties("   ") == 0

def test_calculate_penalties_home_row():
    # Все символы из домашнего ряда → штраф = 0
    text = "фывапролджэ"
    assert calculate_penalties(text) == 0

def test_calculate_penalties_one_shift_vertical():
    # 'й' → (0,0), домашняя 'ф' → (0,1) → dy=1 → штраф=1
    assert calculate_penalties("й") == 1

def test_calculate_penalties_lower_row():
    # 'я' → (0,2), домашняя 'ф' → (0,1) → dy=1 → штраф=1
    assert calculate_penalties("я") == 1
