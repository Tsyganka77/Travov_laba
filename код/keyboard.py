keyboard_finger_qwerty = {
    "leftfinger5": ('ё', '1', 'й', 'ф', 'я'),
    "leftfinger4": ('2', 'ц', 'ы', 'ч'),
    "leftfinger3": ('3', 'у', 'в', 'с'),
    "leftfinger2": ('4', 'к', 'а', 'м', '5', 'е', 'п', 'и'),
    "leftfinger1": (' '),
    "rightfinger2": ('6', 'н', 'р', 'т', '7', 'г', 'о', 'ь'),
    "rightfinger3": ('8', 'ш', 'л', 'б'),
    "rightfinger4": ('9', 'щ', 'д', 'ю'),
    "rightfinger5": ('0', '-', '=', 'з', 'ж', '.', 'х', 'э', 'ъ')
}

keyboard_finger_qwerty_dop = {
    "leftfinger5": ('!'),
    "leftfinger4": ('"'),
    "leftfinger3": ('№'),
    "leftfinger2": (';', '%'),
    "rightfinger2": (':', '?'),
    "rightfinger3": ('*'),
    "rightfinger4": ('('),
    "rightfinger5": (')', '_', '+', '/', ',')
}

qwerty_finger_count = {'leftfinger5': 0, 'leftfinger4': 0, 'leftfinger3': 0, 'leftfinger2': 0,
                       'leftfinger1': 0, 'rightfinger1': 0, 'rightfinger2': 0,
                       'rightfinger3': 0, 'rightfinger4': 0, 'rightfinger5': 0}

# Домашняя строка — только эти 8 клавиш
home_keys = {'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'}

# Какой палец отвечает за какую клавишу (домашняя строка)
key_to_home_finger = {
    'ф': 'left_pinky',
    'ы': 'left_ring',
    'в': 'left_middle',
    'а': 'left_index',
    'п': 'left_index',
    'р': 'right_index',
    'о': 'right_index',
    'л': 'right_middle',
    'д': 'right_ring',
    'ж': 'right_pinky',
    'э': 'right_pinky'
}

# Координаты клавиш на виртуальной сетке (столбец, строка)
key_grid = {
    # Верхняя строка (row 0)
    'й': (0, 0), 'ц': (1, 0), 'у': (2, 0), 'к': (3, 0), 'е': (4, 0), 'н': (5, 0),
    'г': (6, 0), 'ш': (7, 0), 'щ': (8, 0), 'з': (9, 0), 'х': (10, 0), 'ъ': (11, 0),

    # Домашняя строка (row 1)
    'ф': (0, 1), 'ы': (1, 1), 'в': (2, 1), 'а': (3, 1), 'п': (4, 1),
    'р': (5, 1), 'о': (6, 1), 'л': (7, 1), 'д':(8, 1), 'ж':(9, 1), 'э':(10, 1),

    # Нижняя строка (row 2)
    'я': (0, 2), 'ч': (1, 2), 'с': (2, 2), 'м': (3, 2), 'и': (4, 2), 'т': (5, 2),
    'д': (6, 2), 'ж': (7, 2), 'б': (8, 2), 'ю': (9, 2), '.': (10, 2), ',': (11, 2)
}

# Все клавиши, которые мы можем обрабатывать
valid_keys = set(key_grid.keys())

# Символы, которые не влияют на штрафы
ignore_chars = set(' \t\n\r.,!?;:"\'()[]{}-_+=*/\\|@#$%^&`~')

