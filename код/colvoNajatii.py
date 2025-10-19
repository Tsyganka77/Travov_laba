"""
Считывает количество нажатий
"""

from function import (count_finger_load_qwerty, count_finger_load_vyzov,
                      load_hand_left, load_hand_right, calculate_penalties,
                      calculate_penalties_vyzov)
from keyboard import (keyboard_finger_qwerty_dop, keyboard_finger_vyzov,
                      keyboard_finger_vyzov_dop)
if __name__ == "__main__":
    with open('voina_i_mir.txt', "r", encoding='utf-8') as f:
        text = f.read()

    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)
    left_qwerty = load_hand_left(qwerty_finger_load)
    right_qwerty = load_hand_right(qwerty_finger_load)
    left_vyzov = load_hand_left(vyzov_finger_load)
    right_vyzov = load_hand_right(vyzov_finger_load)
    penalties = calculate_penalties(text)
    penalties_vyzov = calculate_penalties_vyzov(text)
    print('====================================================================')
    print('ЙЦУКЕН')
    print('====================================================================')
    print('Нагрузка на левую руку в процентах:', left_qwerty, '%')
    print('Нагрузка на правую руку в процентах:', right_qwerty, '%')
    print('====================================================================')
    fing = ['левый мизинец', 'левый безымянный', 'левый средний',
            'левый указательный', 'левый большой',
            'правый большой', 'правый указательный',
            'правый средний', 'правый безымянный', 'правый мизинец']
    fing_d_qwerty = dict(zip(fing, qwerty_finger_load))
    print('Количество нажатий каждым пальцем в раскладке ЙЦУКЕН')
    print(fing_d_qwerty)
    print('===================================================================')
    print('Количество штрафов: ', penalties)
    print('===================================================================')
    print('===================================================================')
    print('ВЫЗОВ')
    print('===================================================================')
    print('Нагрузка на левую руку в процентах:', left_vyzov, '%')
    print('Нагрузка на правую руку в процентах:', right_vyzov, '%')
    print('===================================================================')
    find_d_vyzov = dict(zip(fing, vyzov_finger_load))
    print('Количество нажатий каждым пальцем в раскладке ВЫЗОВ')
    print(find_d_vyzov)
    print('===================================================================')
    print('Количество штрафов:', penalties_vyzov)
