"""
Считывает количество нажатий каждым пальцем
"""

from function import count_finger_load_qwerty, load_hand_left, load_hand_right
from keyboard import keyboard_finger_qwerty_dop
if __name__ == "__main__":
    with open('voina_i_mir.txt', "r", encoding='utf-8') as f:
        text = f.read()

    qwerty_finger_load = count_finger_load_qwerty(text)
    left_qwerty = load_hand_left(qwerty_finger_load)
    right_qwerty = load_hand_right(qwerty_finger_load)
    print('ЙЦУКЕН')
    print('Нагрузка на левую руку в процентах:', left_qwerty, '%')
    print('Нагрузка на правую руку в процентах:', right_qwerty, '%')
    fing = ['левый мизинец', 'левый безымянный', 'левый средний',
            'левый указательный', 'левый большой',
            'правый большой', 'правый указательный',
            'правый средний', 'правый безымянный', 'правый мизинец']
    fing_d_qwerty = dict(zip(fing, qwerty_finger_load))
    print('Количество нажатий каждым пальцем в раскладке ЙЦУКЕН')
    print(fing_d_qwerty)

