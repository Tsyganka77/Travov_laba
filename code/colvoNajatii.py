"""Main script to analyze text on multiple keyboard layouts."""

from function import (
    count_finger_load_qwerty,
    count_finger_load_vyzov,
    count_finger_load_dictor,
    count_finger_load_ant,
    count_finger_load_rusphone,
    count_finger_load_skoropis,
    count_finger_load_zubachew,
    load_hand_left,
    load_hand_right,
    calculate_penalties_qwerty,
    calculate_penalties_vyzov,
    calculate_penalties_dictor,
    calculate_penalties_ant,
    calculate_penalties_rusphone,
    calculate_penalties_skoropis,
    calculate_penalties_zubachew,
)

if __name__ == "__main__":
    with open("voina_i_mir.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # QWERTY
    qwerty_load = count_finger_load_qwerty(text)
    left_qwerty = load_hand_left(qwerty_load)
    right_qwerty = load_hand_right(qwerty_load)
    penalties_qwerty = calculate_penalties_qwerty(text)

    # VYZOV
    vyzov_load = count_finger_load_vyzov(text)
    left_vyzov = load_hand_left(vyzov_load)
    right_vyzov = load_hand_right(vyzov_load)
    penalties_vyzov = calculate_penalties_vyzov(text)

    # DICTOR
    dictor_load = count_finger_load_dictor(text)
    left_dictor = load_hand_left(dictor_load)
    right_dictor = load_hand_right(dictor_load)
    penalties_dictor = calculate_penalties_dictor(text)

    # ANT
    ant_load = count_finger_load_ant(text)
    left_ant = load_hand_left(ant_load)
    right_ant = load_hand_right(ant_load)
    penalties_ant = calculate_penalties_ant(text)

    # RUSPHONE
    rusphone_load = count_finger_load_rusphone(text)
    left_rusphone = load_hand_left(rusphone_load)
    right_rusphone = load_hand_right(rusphone_load)
    penalties_rusphone = calculate_penalties_rusphone(text)

    # SKOROPIS
    skoropis_load = count_finger_load_skoropis(text)
    left_skoropis = load_hand_left(skoropis_load)
    right_skoropis = load_hand_right(skoropis_load)
    penalties_skoropis = calculate_penalties_skoropis(text)

    # ZUBACHEW
    zubachew_load = count_finger_load_zubachew(text)
    left_zubachew = load_hand_left(zubachew_load)
    right_zubachew = load_hand_right(zubachew_load)
    penalties_zubachew = calculate_penalties_zubachew(text)

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
    print("ANT")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_ant}%")
    print(f"Нагрузка на правую руку: {right_ant}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, ant_load)))
    print("Штрафы:", penalties_ant)

    print("=" * 68)
    print("RUSPHONE")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_rusphone}%")
    print(f"Нагрузка на правую руку: {right_rusphone}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, rusphone_load)))
    print("Штрафы:", penalties_rusphone)

    print("=" * 68)
    print("SKOROPIS")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_skoropis}%")
    print(f"Нагрузка на правую руку: {right_skoropis}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, skoropis_load)))
    print("Штрафы:", penalties_skoropis)

    print("=" * 68)
    print("ZUBACHEW")
    print("=" * 68)
    print(f"Нагрузка на левую руку: {left_zubachew}%")
    print(f"Нагрузка на правую руку: {right_zubachew}%")
    print("Количество нажатий каждым пальцем:")
    print(dict(zip(fingers, zubachew_load)))
    print("Штрафы:", penalties_zubachew)
    print("=" * 68)
