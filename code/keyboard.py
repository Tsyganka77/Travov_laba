KEYBOARD_QWERTY = {
    "leftfinger5": ("ё", "1", "!", "й", "ф", "я", "Й", "Ф", "Я"),
    "leftfinger4": ("2", "\"", "ц", "ы", "ч", "Ц", "Ы", "Ч"),
    "leftfinger3": ("3", "№", "у", "в", "с", "У", "В", "С"),
    "leftfinger2": ("4", ";", "5", "%", "к", "а", "м", "е", "п", "и", "К", "А", "М", "Е", "П", "И"),
    "leftfinger1": (),
    "rightfinger2": ("6", ":", "7", "?", "н", "р", "т", "г", "о", "ь", "Н", "Р", "Т", "Г", "О", "Ь"),
    "rightfinger3": ("8", "*", "ш", "л", "б", "Ш", "Л", "Б"),
    "rightfinger4": ("9", "(", "щ", "д", "ю", "Щ", "Д", "Ю"),
    "rightfinger5": ("0", ")", "-", "_", "=", "+", "з", "ж", ".", ",", "х", "э", "ъ", "З", "Ж", "Х", "Э", "Ъ", "/", "\\", "[", "]", "{", "}", "`", "~"),
}

KEY_GRID_QWERTY = {
    "ё": (0, 0), "1": (0, 0), "!": (0, 0),
    "2": (1, 0), "\"": (1, 0),
    "3": (2, 0), "№": (2, 0),
    "4": (3, 0), ";": (3, 0),
    "5": (4, 0), "%": (4, 0),
    "6": (5, 0), ":": (5, 0),
    "7": (6, 0), "?": (6, 0),
    "8": (7, 0), "*": (7, 0),
    "9": (8, 0), "(": (8, 0),
    "0": (9, 0), ")": (9, 0),
    "-": (10, 0), "_": (10, 0),
    "=": (11, 0), "+": (11, 0),
    "й": (0, 0), "Й": (0, 0),
    "ц": (1, 0), "Ц": (1, 0),
    "у": (2, 0), "У": (2, 0),
    "к": (3, 0), "К": (3, 0),
    "е": (4, 0), "Е": (4, 0),
    "н": (5, 0), "Н": (5, 0),
    "г": (6, 0), "Г": (6, 0),
    "ш": (7, 0), "Ш": (7, 0),
    "щ": (8, 0), "Щ": (8, 0),
    "з": (9, 0), "З": (9, 0),
    "х": (10, 0), "Х": (10, 0),
    "ъ": (11, 0), "Ъ": (11, 0),
    "ф": (0, 1), "Ф": (0, 1),
    "ы": (1, 1), "Ы": (1, 1),
    "в": (2, 1), "В": (2, 1),
    "а": (3, 1), "А": (3, 1),
    "о": (6, 1), "О": (6, 1),
    "л": (7, 1), "Л": (7, 1),
    "д": (8, 1), "Д": (8, 1),
    "ж": (9, 1), "Ж": (9, 1),
    "я": (0, 2), "Я": (0, 2),
    "ч": (1, 2), "Ч": (1, 2),
    "с": (2, 2), "С": (2, 2),
    "м": (3, 2), "М": (3, 2),
    "и": (4, 2), "И": (4, 2),
    "т": (5, 2), "Т": (5, 2),
    "ь": (6, 2), "Ь": (6, 2),
    "б": (7, 2), "Б": (7, 2),
    "ю": (8, 2), "Ю": (8, 2),
    ".": (9, 2), ",": (10, 2),
    "э": (11, 2), "Э": (11, 2),
    "/": (10, 2), "\\": (11, 2),
    "[": (12, 0), "]": (12, 0),
    "{": (12, 0), "}": (12, 0),
    "`": (13, 0), "~": (13, 0),
}

HOME_KEYS_QWERTY = {"ф", "ы", "в", "а", "о", "л", "д", "ж", "Ф", "Ы", "В", "А", "О", "Л", "Д", "Ж"}

KEYBOARD_VYZOV = {
    "leftfinger5": ("ч", "ш", "щ", "ъ", "х", "Ч", "Ш", "Щ", "Ъ", "Х", "1", "!", "q", "Q"),
    "leftfinger4": ("и", "ы", "ь", "э", "И", "Ы", "Ь", "Э", "2", "@", "w", "W"),
    "leftfinger3": ("е", "у", "ю", "я", "Е", "У", "Ю", "Я", "3", "#", "e", "E"),
    "leftfinger2": ("а", "к", "м", "с", "А", "К", "М", "С", "4", "$", "r", "R"),
    "leftfinger1": (),
    "rightfinger2": ("н", "т", "г", "ф", "Н", "Т", "Г", "Ф", "5", "%", "t", "T"),
    "rightfinger3": ("д", "в", "п", "Д", "В", "П", "6", "^", "y", "Y"),
    "rightfinger4": ("л", "р", "о", "Л", "Р", "О", "7", "&", "u", "U"),
    "rightfinger5": ("б", "ж", "з", "й", "ц", "Б", "Ж", "З", "Й", "Ц", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "i", "I", "o", "O", "p", "P", "[", "]", "{", "}", "\\", "|", "/", "?", ".", ","),
}

HOME_KEYS_VYZOV = {"ч", "и", "е", "а", "н", "т", "с", "б", "Ч", "И", "Е", "А", "Н", "Т", "С", "Б"}

FINGER_TO_COL_VYZOV = {
    "leftfinger5": 0, "leftfinger4": 1, "leftfinger3": 2, "leftfinger2": 3,
    "rightfinger2": 4, "rightfinger3": 5, "rightfinger4": 6, "rightfinger5": 7,
}

KEY_GRID_VYZOV = {}
for finger, chars in KEYBOARD_VYZOV.items():
    if not chars or finger == "leftfinger1":
        continue
    col = FINGER_TO_COL_VYZOV.get(finger)
    if col is None:
        continue
    for ch in chars:
        row = 1 if ch.lower() in {c.lower() for c in HOME_KEYS_VYZOV} else (2 if ch.islower() or ch in "ёъыьэ" else 0)
        KEY_GRID_VYZOV[ch] = (col, row)

KEYBOARD_DICTOR = {
    "leftfinger5": ("у", "й", "ф", "я", "У", "Й", "Ф", "Я", "1", "!", "q", "Q"),
    "leftfinger4": ("и", "ы", "ч", "э", "И", "Ы", "Ч", "Э", "2", "@", "w", "W"),
    "leftfinger3": ("е", "в", "с", "ь", "Е", "В", "С", "Ь", "3", "#", "e", "E"),
    "leftfinger2": ("а", "к", "м", "п", "А", "К", "М", "П", "4", "$", "r", "R"),
    "leftfinger1": (),
    "rightfinger2": ("т", "н", "р", "о", "Т", "Н", "Р", "О", "5", "%", "t", "T"),
    "rightfinger3": ("д", "ш", "л", "б", "Д", "Ш", "Л", "Б", "6", "^", "y", "Y"),
    "rightfinger4": ("з", "щ", "ж", "ю", "З", "Щ", "Ж", "Ю", "7", "&", "u", "U"),
    "rightfinger5": ("г", "х", "ц", "ъ", "Г", "Х", "Ц", "Ъ", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "i", "I", "o", "O", "p", "P", "[", "]", "{", "}", "\\", "|", "/", "?", ".", ","),
}

HOME_KEYS_DICTOR = {"у", "и", "е", "а", "т", "д", "р", "г", "У", "И", "Е", "А", "Т", "Д", "Р", "Г"}

FINGER_TO_COL_DICTOR = {
    "leftfinger5": 0, "leftfinger4": 1, "leftfinger3": 2, "leftfinger2": 3,
    "rightfinger2": 4, "rightfinger3": 5, "rightfinger4": 6, "rightfinger5": 7,
}

KEY_GRID_DICTOR = {}
for finger, chars in KEYBOARD_DICTOR.items():
    if not chars or finger == "leftfinger1":
        continue
    col = FINGER_TO_COL_DICTOR.get(finger)
    if col is None:
        continue
    for ch in chars:
        row = 1 if ch.lower() in {c.lower() for c in HOME_KEYS_DICTOR} else (2 if ch.islower() else 0)
        KEY_GRID_DICTOR[ch] = (col, row)

KEYBOARD_ANT = {
    "leftfinger5": ("ф", "ш", "э", "ё", "Ф", "Ш", "Э", "Ё", "1", "!", "q", "Q"),
    "leftfinger4": ("ы", "ь", "ю", "б", "Ы", "Ь", "Ю", "Б", "2", "@", "w", "W"),
    "leftfinger3": ("а", "е", "и", "о", "А", "Е", "И", "О", "3", "#", "e", "E"),
    "leftfinger2": ("я", "р", "т", "Я", "Р", "Т", "4", "$", "r", "R"),
    "leftfinger1": (),
    "rightfinger2": ("у", "л", "д", "ж", "У", "Л", "Д", "Ж", "5", "%", "t", "T"),
    "rightfinger3": ("й", "к", "з", "х", "Й", "К", "З", "Х", "6", "^", "y", "Y"),
    "rightfinger4": ("ц", "щ", "ч", "п", "Ц", "Щ", "Ч", "П", "7", "&", "u", "U"),
    "rightfinger5": ("м", "г", "в", "н", "М", "Г", "В", "Н", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "i", "I", "o", "O", "p", "P", "[", "]", "{", "}", "\\", "|", "/", "?", ".", ","),
}

HOME_KEYS_ANT = {"а", "е", "и", "о", "у", "л", "д", "ж", "А", "Е", "И", "О", "У", "Л", "Д", "Ж"}

FINGER_TO_COL_ANT = {
    "leftfinger5": 0, "leftfinger4": 1, "leftfinger3": 2, "leftfinger2": 3,
    "rightfinger2": 4, "rightfinger3": 5, "rightfinger4": 6, "rightfinger5": 7,
}

KEY_GRID_ANT = {}
for finger, chars in KEYBOARD_ANT.items():
    if not chars or finger == "leftfinger1":
        continue
    col = FINGER_TO_COL_ANT.get(finger)
    if col is None:
        continue
    for ch in chars:
        row = 1 if ch.lower() in {c.lower() for c in HOME_KEYS_ANT} else (2 if ch.islower() else 0)
        KEY_GRID_ANT[ch] = (col, row)

KEYBOARD_RUSPHONE = {
    "leftfinger5": ("ю", "э", "я", "а", "Ю", "Э", "Я", "А", "1", "!", "q", "Q"),
    "leftfinger4": ("б", "ь", "з", "с", "Б", "Ь", "З", "С", "2", "@", "w", "W"),
    "leftfinger3": ("е", "р", "д", "ц", "Е", "Р", "Д", "Ц", "3", "#", "e", "E"),
    "leftfinger2": ("т", "ф", "г", "х", "Т", "Ф", "Г", "Х", "4", "$", "r", "R"),
    "leftfinger1": (),
    "rightfinger2": ("у", "й", "к", "л", "У", "Й", "К", "Л", "5", "%", "t", "T"),
    "rightfinger3": ("и", "о", "п", "ш", "И", "О", "П", "Ш", "6", "^", "y", "Y"),
    "rightfinger4": ("щ", "ч", "ж", "м", "Щ", "Ч", "Ж", "М", "7", "&", "u", "U"),
    "rightfinger5": ("н", "в", "ы", "ё", "Н", "В", "Ы", "Ё", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "i", "I", "o", "O", "p", "P", "[", "]", "{", "}", "\\", "|", "/", "?", ".", ","),
}

HOME_KEYS_RUSPHONE = {"е", "р", "д", "ц", "у", "й", "к", "л", "Е", "Р", "Д", "Ц", "У", "Й", "К", "Л"}

FINGER_TO_COL_RUSPHONE = {
    "leftfinger5": 0, "leftfinger4": 1, "leftfinger3": 2, "leftfinger2": 3,
    "rightfinger2": 4, "rightfinger3": 5, "rightfinger4": 6, "rightfinger5": 7,
}

KEY_GRID_RUSPHONE = {}
for finger, chars in KEYBOARD_RUSPHONE.items():
    if not chars or finger == "leftfinger1":
        continue
    col = FINGER_TO_COL_RUSPHONE.get(finger)
    if col is None:
        continue
    for ch in chars:
        row = 1 if ch.lower() in {c.lower() for c in HOME_KEYS_RUSPHONE} else (2 if ch.islower() else 0)
        KEY_GRID_RUSPHONE[ch] = (col, row)

KEYBOARD_SKOROPIS = {
    "leftfinger5": ("ф", "э", "ц", "у", "Ф", "Э", "Ц", "У", "1", "!", "q", "Q"),
    "leftfinger4": ("ь", "я", "и", "е", "Ь", "Я", "И", "Е", "2", "@", "w", "W"),
    "leftfinger3": ("з", "в", "о", "а", "З", "В", "О", "А", "3", "#", "e", "E"),
    "leftfinger2": ("с", "д", "л", "т", "С", "Д", "Л", "Т", "4", "$", "r", "R"),
    "leftfinger1": (),
    "rightfinger2": ("к", "п", "ш", "р", "К", "П", "Ш", "Р", "5", "%", "t", "T"),
    "rightfinger3": ("г", "ж", "щ", "й", "Г", "Ж", "Щ", "Й", "6", "^", "y", "Y"),
    "rightfinger4": ("ч", "х", "б", "м", "Ч", "Х", "Б", "М", "7", "&", "u", "U"),
    "rightfinger5": ("н", "ы", "ё", "ю", "Н", "Ы", "Ё", "Ю", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "i", "I", "o", "O", "p", "P", "[", "]", "{", "}", "\\", "|", "/", "?", ".", ","),
}

HOME_KEYS_SKOROPIS = {"ь", "я", "и", "е", "к", "п", "ш", "р", "Ь", "Я", "И", "Е", "К", "П", "Ш", "Р"}

FINGER_TO_COL_SKOROPIS = {
    "leftfinger5": 0, "leftfinger4": 1, "leftfinger3": 2, "leftfinger2": 3,
    "rightfinger2": 4, "rightfinger3": 5, "rightfinger4": 6, "rightfinger5": 7,
}

KEY_GRID_SKOROPIS = {}
for finger, chars in KEYBOARD_SKOROPIS.items():
    if not chars or finger == "leftfinger1":
        continue
    col = FINGER_TO_COL_SKOROPIS.get(finger)
    if col is None:
        continue
    for ch in chars:
        row = 1 if ch.lower() in {c.lower() for c in HOME_KEYS_SKOROPIS} else (2 if ch.islower() else 0)
        KEY_GRID_SKOROPIS[ch] = (col, row)

KEYBOARD_ZUBACHEW = KEYBOARD_ANT.copy()
HOME_KEYS_ZUBACHEW = HOME_KEYS_ANT.copy()
KEY_GRID_ZUBACHEW = KEY_GRID_ANT.copy()

FINGER_TO_IDX = {
    "leftfinger5": 0,
    "leftfinger4": 1,
    "leftfinger3": 2,
    "leftfinger2": 3,
    "leftfinger1": 4,
    "rightfinger1": 5,
    "rightfinger2": 6,
    "rightfinger3": 7,
    "rightfinger4": 8,
    "rightfinger5": 9,
}
