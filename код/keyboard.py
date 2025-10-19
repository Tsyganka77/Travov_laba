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

keyboard_finger_vyzov = {
    "leftfinger5": ('ю', 'ё', 'в', 'ч', 'ш'),
    "leftfinger4": ('ы', 'и', 'х', '['),
    "leftfinger3": ('э', 'о', 'е', 'й'),
    "leftfinger2": ('Э', 'у', 'а', 'к', '(', 'ь', ',', '_'),
    "leftfinger1": ' ',
    "rightfinger2": ('=', '*', 'ё', '.', '/', '^', 'н', 'р'),
    "rightfinger3": (')', 'д', 'т', 'м'),
    "rightfinger4": ('+', 'я', 'с', 'ф'),
    "rightfinger5": (']', '!', 'щ', 'г', 'ж', 'ц', 'б', 'з', 'п', 'ъ')
}

keyboard_finger_vyzov_dop = {
    "leftfinger5": '%',
    "leftfinger4": '7',
    "leftfinger3": '5',
    "leftfinger2": ('3', '1'),
    "rightfinger2": ('9', '0'),
    "rightfinger3": '2',
    "rightfinger4": '4',
    "rightfinger5": ('6', '8', '#', '@')
}

vyzov_finger_count = {'leftfinger5': 0, 'leftfinger4': 0, 'leftfinger3': 0, 'leftfinger2': 0,
                      'leftfinger1': 0, 'rightfinger1': 0, 'rightfinger2': 0,
                      'rightfinger3': 0, 'rightfinger4': 0, 'rightfinger5': 0}









# --- Добавить в keyboard.py ---

# Домашние клавиши для ВЫЗОВ (по одному на палец, без больших пальцев)
home_keys_vyzov = {'ю', 'ы', 'э', 'у', 'н', 'д', 'т', 'щ'}

# Маппинг: клавиша → домашний палец (для штрафов)
key_to_home_finger_vyzov = {
    'ю': 'left_pinky',
    'ы': 'left_ring',
    'э': 'left_middle',
    'у': 'left_index',
    'н': 'right_index',
    'д': 'right_middle',
    'т': 'right_ring',
    'щ': 'right_pinky'
}

# Сетка клавиш для ВЫЗОВ: (столбец, строка)
# Столбцы: 0=ю, 1=ы, 2=э, 3=у, 4=н, 5=д, 6=т, 7=щ
# Добавим остальные клавиши, распределив их по столбцам согласно keyboard_finger_vyzov

key_grid_vyzov = {}

# Помощник: маппинг пальца → столбец
finger_to_col = {
    'leftfinger5': 0,   # ю
    'leftfinger4': 1,   # ы
    'leftfinger3': 2,   # э
    'leftfinger2': 3,   # у
    'rightfinger2': 4,  # н
    'rightfinger3': 5,  # д
    'rightfinger4': 6,  # т
    'rightfinger5': 7,  # щ
}

# Заполняем сетку
for finger, chars in keyboard_finger_vyzov.items():
    if finger in ('leftfinger1', 'rightfinger1'):
        continue  # большие пальцы — не в сетке
    col = finger_to_col.get(finger)
    if col is None:
        continue
    for char in chars:
        if char == ' ':
            continue
        # Определяем строку: если char в домашних — row=1, иначе 0 или 2
        if char in home_keys_vyzov:
            row = 1
        elif char in ['в', 'и', 'о', 'а', 'р', 'м', 'ь', 'ё', '.', '/', '^', '(', ',', '_', ')']:
            row = 0  # верхний ряд
        else:
            row = 2  # нижний ряд
        key_grid_vyzov[char] = (col, row)

# Все допустимые клавиши для ВЫЗОВ
valid_keys_vyzov = set(key_grid_vyzov.keys())

# Символы, которые игнорируем (как и раньше)
ignore_chars = set(' \t\n\r.,!?;:"\'()[]{}-_+=*/\\|@#$%^&`~')
