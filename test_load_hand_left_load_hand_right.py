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

def test_load_hand_left():
    # Левая рука: пальцы 0–4 → leftfinger5,4,3,2,1
    data = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]  # только левая
    assert load_hand_left(data) == 100

def test_load_hand_right():
    # Правая рука: пальцы 5–9 → но в вашем списке индексы 5–9
    # Однако в qwerty_finger_count у вас 10 пальцев: индексы 0–9
    # Правая рука: rightfinger1–5 → индексы 5–9
    data = [0, 0, 0, 0, 0, 5, 5, 5, 5, 5]  # только правая
    assert load_hand_right(data) == 100

