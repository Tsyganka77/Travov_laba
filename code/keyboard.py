"""Keyboard layout definitions and key grids."""

# ====================== QWERTY (ЙЦУКЕН) ======================

KEYBOARD_FINGER_QWERTY = {
    "leftfinger5": ("ё", "1", "й", "ф", "я"),
    "leftfinger4": ("2", "ц", "ы", "ч"),
    "leftfinger3": ("3", "у", "в", "с"),
    "leftfinger2": ("4", "к", "а", "м", "5", "е", "п", "и"),
    "leftfinger1": (" ",),
    "rightfinger2": ("6", "н", "р", "т", "7", "г", "о", "ь"),
    "rightfinger3": ("8", "ш", "л", "б"),
    "rightfinger4": ("9", "щ", "д", "ю"),
    "rightfinger5": ("0", "-", "=", "з", "ж", ".", "х", "э", "ъ"),
}

KEYBOARD_FINGER_QWERTY_DOP = {
    "leftfinger5": ("!",),
    "leftfinger4": ('"',),
    "leftfinger3": ("№",),
    "leftfinger2": (";", "%"),
    "rightfiber2": (":", "?"),
    "rightfinger3": ("*",),
    "rightfinger4": ("(",),
    "rightfinger5": (")", "_", "+", "/", ","),
}

QWERTY_FINGER_COUNT = {
    "leftfinger5": 0,
    "leftfinger4": 0,
    "leftfinger3": 0,
    "leftfinger2": 0,
    "leftfinger1": 0,
    "rightfinger1": 0,
    "rightfinger2": 0,
    "rightfinger3": 0,
    "rightfinger4": 0,
    "rightfinger5": 0,
}

HOME_KEYS_QWERTY = {"ф", "ы", "в", "а", "о", "л", "д", "ж"}

KEY_GRID_QWERTY = {
    # Row 0 — top
    "й": (0, 0), "ц": (1, 0), "у": (2, 0), "к": (3, 0), "е": (4, 0), "н": (5, 0),
    "г": (6, 0), "ш": (7, 0), "щ": (8, 0), "з": (9, 0), "х": (10, 0), "ъ": (11, 0),
    "п": (4, 0), "р": (5, 0),

    # Row 1 — home
    "ф": (0, 1), "ы": (1, 1), "в": (2, 1), "а": (3, 1),
    "о": (6, 1), "л": (7, 1), "д": (8, 1), "ж": (9, 1),

    # Row 2 — bottom
    "я": (0, 2), "ч": (1, 2), "с": (2, 2), "м": (3, 2), "и": (4, 2), "т": (5, 2),
    "ь": (6, 2), "б": (7, 2), "ю": (8, 2), ".": (9, 2), ",": (10, 2),
}

VALID_KEYS_QWERTY = set(KEY_GRID_QWERTY.keys()) | {" "}


# ====================== VYZOV ======================

KEYBOARD_FINGER_VYZOV = {
    "leftfinger5": ("ч", "ш", "щ", "ъ", "х"),
    "leftfinger4": ("и", "ы", "ь", "э"),
    "leftfinger3": ("е", "у", "ю", "я"),
    "leftfinger2": ("а", "к", "м", "с"),
    "leftfinger1": (" ",),
    "rightfinger2": ("н", "т", "г", "ф"),
    "rightfinger3": ("д", "в", "п"),
    "rightfinger4": ("л", "р", "о"),
    "rightfinger5": ("б", "ж", "з", "й", "ц"),
}

KEYBOARD_FINGER_VYZOV_DOP = {
    "leftfinger5": ("%", "Q", "W"),
    "leftfinger4": ("7", "S", "D"),
    "leftfinger3": ("5", "E", "R"),
    "leftfinger2": ("3", "1", "A"),
    "rightfinger2": ("9", "0", "T", "Y"),
    "rightfinger3": ("2", "F", "G"),
    "rightfinger4": ("4", "H", "J"),
    "rightfinger5": ("6", "8", "#", "Z", "X"),
}

VYZOV_FINGER_COUNT = {
    "leftfinger5": 0,
    "leftfinger4": 0,
    "leftfinger3": 0,
    "leftfinger2": 0,
    "leftfinger1": 0,
    "rightfinger1": 0,
    "rightfinger2": 0,
    "rightfinger3": 0,
    "rightfinger4": 0,
    "rightfinger5": 0,
}

HOME_KEYS_VYZOV = {"ч", "и", "е", "а", "н", "т", "с", "б"}
HOME_ROW_VYZOV = ["ч", "и", "е", "а", "н", "т", "с", "б"]

FINGER_TO_COL_VYZOV = {
    "leftfinger5": 0,
    "leftfinger4": 1,
    "leftfinger3": 2,
    "leftfinger2": 3,
    "rightfinger2": 4,
    "rightfinger3": 5,
    "rightfinger4": 6,
    "rightfinger5": 7,
}

KEY_GRID_VYZOV = {}
for finger, chars in KEYBOARD_FINGER_VYZOV.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_VYZOV.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        if ch == " ":
            continue
        row = 1 if ch in HOME_KEYS_VYZOV else 2
        KEY_GRID_VYZOV[ch] = (col, row)

for finger, chars in KEYBOARD_FINGER_VYZOV_DOP.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_VYZOV.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        KEY_GRID_VYZOV[ch] = (col, 0)

VALID_KEYS_VYZOV = set(KEY_GRID_VYZOV.keys()) | {" "}


# ====================== DICTOR ======================

KEYBOARD_FINGER_DICTOR = {
    "leftfinger5": ("у", "й", "ф", "я"),
    "leftfinger4": ("и", "ы", "ч", "э"),
    "leftfinger3": ("е", "в", "с", "ь"),
    "leftfinger2": ("а", "к", "м", "п"),
    "leftfinger1": (" ",),
    "rightfinger2": ("т", "н", "р", "о"),
    "rightfinger3": ("с", "ш", "л", "б"),
    "rightfinger4": ("р", "щ", "д", "ю"),
    "rightfinger5": ("й", "з", "ж", "х", "ъ"),
}

KEYBOARD_FINGER_DICTOR_DOP = {
    "leftfinger5": ("%", "Q", "W"),
    "leftfinger4": ("7", "S", "D"),
    "leftfinger3": ("5", "E", "R"),
    "leftfinger2": ("3", "1", "A"),
    "rightfinger2": ("9", "0", "T", "Y"),
    "rightfinger3": ("2", "F", "G"),
    "rightfinger4": ("4", "H", "J"),
    "rightfinger5": ("6", "8", "#", "Z", "X"),
}

DICTOR_FINGER_COUNT = {
    "leftfinger5": 0,
    "leftfinger4": 0,
    "leftfinger3": 0,
    "leftfinger2": 0,
    "leftfinger1": 0,
    "rightfinger1": 0,
    "rightfinger2": 0,
    "rightfinger3": 0,
    "rightfinger4": 0,
    "rightfinger5": 0,
}

HOME_KEYS_DICTOR = {"у", "и", "е", "а", "т", "с", "р", "й"}
HOME_ROW_DICTOR = ["у", "и", "е", "а", "т", "с", "р", "й"]

FINGER_TO_COL_DICTOR = {
    "leftfinger5": 0,
    "leftfinger4": 1,
    "leftfinger3": 2,
    "leftfinger2": 3,
    "rightfinger2": 4,
    "rightfinger3": 5,
    "rightfinger4": 6,
    "rightfinger5": 7,
}

KEY_GRID_DICTOR = {}
for finger, chars in KEYBOARD_FINGER_DICTOR.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_DICTOR.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        if ch == " ":
            continue
        row = 1 if ch in HOME_KEYS_DICTOR else 2
        KEY_GRID_DICTOR[ch] = (col, row)

for finger, chars in KEYBOARD_FINGER_DICTOR_DOP.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_DICTOR.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        KEY_GRID_DICTOR[ch] = (col, 0)

VALID_KEYS_DICTOR = set(KEY_GRID_DICTOR.keys()) | {" "}


# ====================== ANT ======================

KEYBOARD_FINGER_ANT = {
    "leftfinger5": ("ф", "ш", "э", "ё"),
    "leftfinger4": ("ы", "ь", "ю", "б"),
    "leftfinger3": ("а", "е", "и", "о"),
    "leftfinger2": ("я", "р", "т", "ы"),  # Уточнить: "ы" уже в leftfinger4? → возможно опечатка
    "leftfinger1": (" ",),
    "rightfinger2": ("у", "л", "д", "ж"),
    "rightfinger3": ("й", "к", "з", "х"),
    "rightfinger4": ("ц", "щ", "ч", "п"),
    "rightfinger5": ("м", "г", "в", "н"),
}

KEYBOARD_FINGER_ANT_DOP = {
    "leftfinger5": ("E", "1", "!"),
    "leftfinger4": ("2", "@"),
    "leftfinger3": ("3", "№"),
    "leftfinger2": ("4", "$"),
    "rightfinger2": ("5", "%"),
    "rightfinger3": ("6", "^"),
    "rightfinger4": ("7", "&"),
    "rightfinger5": ("8", "*", "9", "(", "0", ")", "-", "_", "+", "=", "|", "\\", "/", "?", ">", "<"),
}

ANT_FINGER_COUNT = {
    "leftfinger5": 0,
    "leftfinger4": 0,
    "leftfinger3": 0,
    "leftfinger2": 0,
    "leftfinger1": 0,
    "rightfinger1": 0,
    "rightfinger2": 0,
    "rightfinger3": 0,
    "rightfinger4": 0,
    "rightfinger5": 0,
}

HOME_KEYS_ANT = {"а", "е", "и", "о", "у", "л", "д", "ж"}  # Центральные клавиши основного ряда

FINGER_TO_COL_ANT = {
    "leftfinger5": 0,
    "leftfinger4": 1,
    "leftfinger3": 2,
    "leftfinger2": 3,
    "rightfinger2": 4,
    "rightfinger3": 5,
    "rightfinger4": 6,
    "rightfinger5": 7,
}

KEY_GRID_ANT = {}
for finger, chars in KEYBOARD_FINGER_ANT.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_ANT.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        if ch == " ":
            continue
        row = 1 if ch in HOME_KEYS_ANT else 2
        KEY_GRID_ANT[ch] = (col, row)

for finger, chars in KEYBOARD_FINGER_ANT_DOP.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_ANT.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        KEY_GRID_ANT[ch] = (col, 0)  # Доп символы — верхний ряд

VALID_KEYS_ANT = set(KEY_GRID_ANT.keys()) | {" "}


# ====================== RUSPHONE ======================

KEYBOARD_FINGER_RUSPHONE = {
    "leftfinger5": ("ю", "э", "я", "а"),
    "leftfinger4": ("б", "ь", "з", "с"),
    "leftfinger3": ("е", "р", "д", "ц"),
    "leftfinger2": ("т", "ф", "г", "х"),
    "leftfinger1": (" ",),
    "rightfinger2": ("у", "й", "к", "л"),
    "rightfinger3": ("и", "о", "п", "ш"),
    "rightfinger4": ("щ", "ч", "ж", "м"),
    "rightfinger5": ("н", "в", "ы", "ё"),
}

KEYBOARD_FINGER_RUSPHONE_DOP = {
    "leftfinger5": ("Ю", "1", "!"),
    "leftfinger4": ("2", "@"),
    "leftfinger3": ("3", "№"),
    "leftfinger2": ("4", "$"),
    "rightfinger2": ("5", "%"),
    "rightfinger3": ("6", "^"),
    "rightfinger4": ("7", "&"),
    "rightfinger5": ("8", "*", "9", "(", "0", ")", "-", "_", "+", "=", "|", "\\", "/", "?", ">", "<"),
}

RUSPHONE_FINGER_COUNT = {
    "leftfinger5": 0,
    "leftfinger4": 0,
    "leftfinger3": 0,
    "leftfinger2": 0,
    "leftfinger1": 0,
    "rightfinger1": 0,
    "rightfinger2": 0,
    "rightfinger3": 0,
    "rightfinger4": 0,
    "rightfinger5": 0,
}

HOME_KEYS_RUSPHONE = {"е", "р", "д", "ц", "у", "й", "к", "л"}  # Центральные клавиши основного ряда

FINGER_TO_COL_RUSPHONE = {
    "leftfinger5": 0,
    "leftfinger4": 1,
    "leftfinger3": 2,
    "leftfinger2": 3,
    "rightfinger2": 4,
    "rightfinger3": 5,
    "rightfinger4": 6,
    "rightfinger5": 7,
}

KEY_GRID_RUSPHONE = {}
for finger, chars in KEYBOARD_FINGER_RUSPHONE.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_RUSPHONE.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        if ch == " ":
            continue
        row = 1 if ch in HOME_KEYS_RUSPHONE else 2
        KEY_GRID_RUSPHONE[ch] = (col, row)

for finger, chars in KEYBOARD_FINGER_RUSPHONE_DOP.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_RUSPHONE.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        KEY_GRID_RUSPHONE[ch] = (col, 0)  # Доп символы — верхний ряд

VALID_KEYS_RUSPHONE = set(KEY_GRID_RUSPHONE.keys()) | {" "}


# ====================== SKOROPIS ======================

KEYBOARD_FINGER_SKOROPIS = {
    "leftfinger5": ("ф", "э", "ц", "у"),
    "leftfinger4": ("ь", "я", "и", "е"),
    "leftfinger3": ("з", "в", "о", "а"),
    "leftfinger2": ("с", "д", "л", "т"),
    "leftfinger1": (" ",),
    "rightfinger2": ("к", "п", "ш", "р"),
    "rightfinger3": ("г", "ж", "щ", "й"),
    "rightfinger4": ("ч", "х", "б", "м"),
    "rightfinger5": ("н", "ы", "ё", "ю"),
}

KEYBOARD_FINGER_SKOROPIS_DOP = {
    "leftfinger5": ("*", "1", "!"),
    "leftfinger4": ("2", "@"),
    "leftfinger3": ("3", "№"),
    "leftfinger2": ("4", "$"),
    "rightfinger2": ("5", "%"),
    "rightfinger3": ("6", "^"),
    "rightfinger4": ("7", "&"),
    "rightfinger5": ("8", "*", "9", "(", "0", ")", "-", "_", "+", "=", "|", "\\", "/", "?", ">", "<"),
}

SKOROPIS_FINGER_COUNT = {
    "leftfinger5": 0,
    "leftfinger4": 0,
    "leftfinger3": 0,
    "leftfinger2": 0,
    "leftfinger1": 0,
    "rightfinger1": 0,
    "rightfinger2": 0,
    "rightfinger3": 0,
    "rightfinger4": 0,
    "rightfinger5": 0,
}

HOME_KEYS_SKOROPIS = {"ь", "я", "и", "е", "к", "п", "ш", "р"}  # Центральные клавиши основного ряда

FINGER_TO_COL_SKOROPIS = {
    "leftfinger5": 0,
    "leftfinger4": 1,
    "leftfinger3": 2,
    "leftfinger2": 3,
    "rightfinger2": 4,
    "rightfinger3": 5,
    "rightfinger4": 6,
    "rightfinger5": 7,
}

KEY_GRID_SKOROPIS = {}
for finger, chars in KEYBOARD_FINGER_SKOROPIS.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_SKOROPIS.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        if ch == " ":
            continue
        row = 1 if ch in HOME_KEYS_SKOROPIS else 2
        KEY_GRID_SKOROPIS[ch] = (col, row)

for finger, chars in KEYBOARD_FINGER_SKOROPIS_DOP.items():
    if finger in ("leftfinger1", "rightfinger1"):
        continue
    col = FINGER_TO_COL_SKOROPIS.get(finger)
    if col is None:
        continue
    for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
        KEY_GRID_SKOROPIS[ch] = (col, 0)  # Доп символы — верхний ряд

VALID_KEYS_SKOROPIS = set(KEY_GRID_SKOROPIS.keys()) | {" "}


# ====================== ZUBACHEW ======================

# Идентична Ant — создаём копию для единообразия
KEYBOARD_FINGER_ZUBACHEW = KEYBOARD_FINGER_ANT.copy()
KEYBOARD_FINGER_ZUBACHEW_DOP = KEYBOARD_FINGER_ANT_DOP.copy()
ZUBACHEW_FINGER_COUNT = {k: 0 for k in ANT_FINGER_COUNT}
HOME_KEYS_ZUBACHEW = HOME_KEYS_ANT.copy()
FINGER_TO_COL_ZUBACHEW = FINGER_TO_COL_ANT.copy()
KEY_GRID_ZUBACHEW = KEY_GRID_ANT.copy()
VALID_KEYS_ZUBACHEW = VALID_KEYS_ANT.copy()

IGNORE_CHARS = set(" \t\n\r.,!?;:\"'()[]{}-_+=*/\\|@#$%^&`~")
