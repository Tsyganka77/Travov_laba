"""Main script to analyze text on multiple keyboard layouts."""

from function import (
    count_finger_load_qwerty,
    count_finger_load_vyzov,
    count_finger_load_dictor,
    load_hand_left,
    load_hand_right,
    calculate_penalties_qwerty,
    calculate_penalties_vyzov,
    calculate_penalties_dictor,
)

if __name__ == "__main__":
    with open("voina_i_mir.txt", "r", encoding="utf-8") as f:
        text = f.read()

    qwerty_load = count_finger_load_qwerty(text)
    vyzov_load = count_finger_load_vyzov(text)
    dictor_load = count_finger_load_dictor(text)

    left_qwerty = load_hand_left(qwerty_load)
    right_qwerty = load_hand_right(qwerty_load)
    left_vyzov = load_hand_left(vyzov_load)
    right_vyzov = load_hand_right(vyzov_load)
    left_dictor = load_hand_left(dictor_load)
    right_dictor = load_hand_right(dictor_load)

    penalties_qwerty = calculate_penalties_qwerty(text)
    penalties_vyzov = calculate_penalties_vyzov(text)
    penalties_dictor = calculate_penalties_dictor(text)

    fingers = [
        "левый мизинец", "левый безымянный", "левый средний",
        "левый указательный", "левый большой",
        "правый большой", "правый указательный",
        "правый средний", "правый безымянный", "правый мизинец"
    ]

    print("=" * 68)
    print("ЙЦУКЕН")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_qwerty}%")
    print(f"Нагрузка на правую руку: {right_qwerty}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, qwerty_load)))
    print("Штрафы:", penalties_qwerty)

    print("=" * 68)
    print("ВЫЗОВ")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_vyzov}%")
    print(f"Нагрузка на правую руку: {right_vyzov}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, vyzov_load)))
    print("Штрафы:", penalties_vyzov)

    print("=" * 68)
    print("DICTOR")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_dictor}%")
    print(f"Нагрузка на правую руку: {right_dictor}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, dictor_load)))
    print("Штрафы:", penalties_dictor)
    print("=" * 68)
