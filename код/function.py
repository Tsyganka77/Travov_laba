import keyboard
import numpy as np
from keyboard import (keyboard_finger_qwerty,
                      keyboard_finger_qwerty_dop,
                      qwerty_finger_count)

def find_finger(character, keyboard_layout):
    # 1. Ищем в основной раскладке
    for finger_name, characters in keyboard_layout.items():
        if character in characters:
            return finger_name, 0  # flag = 0 — основная раскладка

    # 2. Если не нашли — ищем во вспомогательной (только для QWERTY)
    if keyboard_layout is keyboard_finger_qwerty:
        for finger_name, characters in keyboard_finger_qwerty_dop.items():
            if character in characters:
                return finger_name, 1  # flag = 1 — доп. раскладка

    # 3. Если нигде не нашли — ошибка
    return "Invalid character: {}".format(character), 0

def count_finger_load_qwerty(text):
    """
        Подсчитывает нагрузку на пальцы, использованные при наборе текста
        на клавиатурной раскладке ЙЦУКЕН.
    """
    for character in text:
        finger_name, flag_nado = \
            find_finger(character.lower(), keyboard_finger_qwerty)
        if finger_name in keyboard.qwerty_finger_count:
            keyboard.qwerty_finger_count[finger_name] += 1
            if character.isupper() or flag_nado == 1:
                shift_finger = 'leftfinger5'
                keyboard.qwerty_finger_count[shift_finger] += 1

    layout_1 = list(qwerty_finger_count.values())
    return layout_1


def load_hand_left(list):
    """
        Вычисляет процент нагрузки
        на левую руку на основе значений из переданного списка.
    """
    start_index = 0
    end_index = 5
    start_index_1 = 0
    end_index_1 = 9
    partial_sum = sum(list[start_index:end_index])
    general_sum = sum(list[start_index_1:end_index_1])
    procent = int((partial_sum * 100) / general_sum)
    return procent


def load_hand_right(list):
    """
        Вычисляет процент нагрузки
        на правую руку на основе значений из переданного списка.
    """
    start_index = 5
    end_index = 9
    start_index_1 = 0
    end_index_1 = 9
    partial_sum = sum(list[start_index:end_index])
    general_sum = sum(list[start_index_1:end_index_1])
    procent = int((partial_sum * 100) / general_sum)
    return procent

def clicks(layout_1, layout_2, layout_3, layout_4):
    """
        Выводит количество нажатий на каждый палец
    """
    fing = ['левый мизинец', 'левый безымянный', 'левый средний',
            'левый указательный', 'левый большой',
            'правый большой', 'правый указательный', 'правый средний',
            'правый безымянный', 'правый мизинец']
    fing_d_qwerty = dict(zip(fing, layout_1))
    return fing_d_qwerty


