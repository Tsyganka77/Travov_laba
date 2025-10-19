import keyboard
import numpy as np
from keyboard import (keyboard_finger_qwerty,
                      keyboard_finger_qwerty_dop,
                      qwerty_finger_count,
                      key_grid,
                      key_grid_vyzov,
                      valid_keys,
                      valid_keys_vyzov,
                      ignore_chars,
                      key_to_home_finger,
                      keyboard_finger_vyzov,
                      keyboard_finger_vyzov_dop,
                      vyzov_finger_count)

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

    #3. Ищем в кв VYZOV
    if keyboard_layout is keyboard_finger_vyzov:
        for finger_name, characters in keyboard_finger_vyzov_dop.items():
            if character in characters:
                return finger_name, 1


    # 3. Если нигде не нашли — ошибкa
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

SPECIAL_CHARS = {'№', 'ц', 'щ', 'ъ', 'ю', 'э'}

def count_finger_load_vyzov(text):
    """
    Счетки нагрузки на пальцы на кв VYZOV
    """

    # Создаём чистый счётчик
    finger_count = {k: 0 for k in keyboard.vyzov_finger_count}

    for char in text:
        # Основной палец
        finger_name, flag_nado = find_finger(char.lower(), keyboard_finger_vyzov)
        if finger_name in finger_count:
            finger_count[finger_name] += 1

        # Shift
        if char.isupper() or flag_nado == 1:
            finger_count['leftfinger5'] += 1

        # Особые символы → AltGr / альтернативный палец
        if char.lower() in SPECIAL_CHARS:
            finger_count['rightfinger1'] += 1

    layout_2 = list(finger_count.values())
    return layout_2

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
    fing_d_vyzov = dict(zip(fing, layout_2))
    return fing_d_qwerty, fing_d_vyzov

def calculate_penalties(text):
    """
    Подсчитывает штрафы для русского текста на кв QWERTY.
    Штрафы начисляются за перемещение пальца от домашней клавиши.
    """
    penalties = 0
    prev_key = None
    prev_pos = None
    prev_finger = None

    for char in text.lower():
        if char in ignore_chars:
            continue

        if char not in valid_keys:
            continue  # Пропускаем неизвестные символы

        current_key = char
        current_pos = key_grid[char]

        # Определяем, какой палец должен был нажать эту клавишу
        # Если клавиша — из домашней строки, то палец «домашний»
        # Если нет — определяем, с какой домашней клавиши он пришёл
        # каждый символ набирается с ближайшей домашней клавиши
        # если клавиша не из домашней строки — она набирается с ближайшей домашней
        # и это движение засчитывается как штраф.

        # Определим, какой домашний палец отвечает за эту клавишу
        # один и тот же палец работает в одном вертикальном столбце

        col = current_pos[0]
        row = current_pos[1]

        # Сопоставим столбцы с домашними пальцами
        # Левая рука: столбцы 0–3 → пальцы от Ф до А
        # Правая рука: столбцы 4–7 → пальцы от П до Л
        # Столбцы 8–11 — правая рука

        finger_map = {
            # Столбец -> домашняя клавиша
            0: 'ф', 1: 'ы', 2: 'в', 3: 'а', 4: 'п', #левая рука
            5: 'р', 6: 'о', 7: 'л', 8: 'д',  # правая рука
            9: 'ж', 10: 'э', 11: 'э'  # крайние правые — все к правому мизинцу
        }

        home_key_for_current = finger_map[col]  # Ближайшая домашняя клавиша по столбцу
        home_pos = key_grid[home_key_for_current]

        # если текущая клавиша — уже домашняя, то движение = 0
        # иначе — это сдвиг от домашней клавиши к текущей

        if current_key == home_key_for_current:
            # Это домашняя клавиша — движение 0, ничего не добавляем
            # Но нам нужно запомнить её как предыдущую
            if prev_key is not None:
                # Проверим: если предыдущий символ был от другого пальца — переход между пальцами не штрафуется
                pass  # Не считаем штраф за смену пальца

            prev_key = current_key
            prev_pos = current_pos
            prev_finger = key_to_home_finger.get(home_key_for_current)
            continue

        #текущая клавиша НЕ домашняя это движение от домашней клавиши
        dx = abs(current_pos[0] - home_pos[0])
        dy = abs(current_pos[1] - home_pos[1])

        total_shift = dx + dy

        if total_shift == 1:
            # Горизонтально или вертикально на 1 клавишу
            penalties += 1
        elif total_shift >= 2:
            # Диагональ (dx=1, dy=1) или 2 клавиши в одну сторону — оба случая дают 2 штрафа
            penalties += 2

        # Обновляем предыдущее состояние: теперь домашняя клавиша — это та, от которой мы пришли
        prev_key = current_key
        prev_pos = current_pos
        prev_finger = key_to_home_finger.get(home_key_for_current)

    return penalties














def calculate_penalties_vyzov(text):
    """
    Подсчитывает штрафы для русского текста на раскладке ВЫЗОВ.
    Штрафы начисляются за перемещение пальца от домашней клавиши.
    """
    penalties = 0

    for char in text.lower():
        if char in ignore_chars:
            continue
        if char not in valid_keys_vyzov:
            continue

        current_key = char
        current_pos = key_grid_vyzov[char]

        col = current_pos[0]
        row = current_pos[1]

        # Определяем домашнюю клавишу для этого столбца
        # Используем фиксированный список домашних клавиш по столбцам
        home_keys_by_col = ['ю', 'ы', 'э', 'у', 'н', 'д', 'т', 'щ']
        if col < len(home_keys_by_col):
            home_key_for_current = home_keys_by_col[col]
            home_pos = key_grid_vyzov[home_key_for_current]
        else:
            # Если столбец вне диапазона — пропускаем
            continue

        # Если текущая клавиша — домашняя, штраф = 0
        if current_key == home_key_for_current:
            continue

        # Иначе — считаем расстояние
        dx = abs(current_pos[0] - home_pos[0])  # всегда 0, т.к. один столбец
        dy = abs(current_pos[1] - home_pos[1])

        # В нашей модели dx = 0, поэтому штраф зависит только от dy
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

    return penalties
