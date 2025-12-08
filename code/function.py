"""Functions for calculating finger load and penalties."""

from keyboard import (
    KEYBOARD_FINGER_QWERTY,
    KEYBOARD_FINGER_QWERTY_DOP,
    QWERTY_FINGER_COUNT,
    VALID_KEYS_QWERTY,
    KEYBOARD_FINGER_VYZOV,
    KEYBOARD_FINGER_VYZOV_DOP,
    VYZOV_FINGER_COUNT,
    VALID_KEYS_VYZOV,
    KEYBOARD_FINGER_DICTOR,
    KEYBOARD_FINGER_DICTOR_DOP,
    DICTOR_FINGER_COUNT,
    VALID_KEYS_DICTOR,
    HOME_KEYS_QWERTY,
    KEY_GRID_QWERTY,
    KEY_GRID_VYZOV,
    KEY_GRID_DICTOR,
    HOME_ROW_VYZOV,
    HOME_ROW_DICTOR,
    FINGER_TO_COL_VYZOV,
    FINGER_TO_COL_DICTOR,
    IGNORE_CHARS,

    # Новые раскладки
    KEYBOARD_FINGER_ANT,
    KEYBOARD_FINGER_ANT_DOP,
    ANT_FINGER_COUNT,
    VALID_KEYS_ANT,
    HOME_KEYS_ANT,
    KEY_GRID_ANT,
    FINGER_TO_COL_ANT,

    KEYBOARD_FINGER_RUSPHONE,
    KEYBOARD_FINGER_RUSPHONE_DOP,
    RUSPHONE_FINGER_COUNT,
    VALID_KEYS_RUSPHONE,
    HOME_KEYS_RUSPHONE,
    KEY_GRID_RUSPHONE,
    FINGER_TO_COL_RUSPHONE,

    KEYBOARD_FINGER_SKOROPIS,
    KEYBOARD_FINGER_SKOROPIS_DOP,
    SKOROPIS_FINGER_COUNT,
    VALID_KEYS_SKOROPIS,
    HOME_KEYS_SKOROPIS,
    KEY_GRID_SKOROPIS,
    FINGER_TO_COL_SKOROPIS,

    KEYBOARD_FINGER_ZUBACHEW,
    KEYBOARD_FINGER_ZUBACHEW_DOP,
    ZUBACHEW_FINGER_COUNT,
    VALID_KEYS_ZUBACHEW,
    HOME_KEYS_ZUBACHEW,
    KEY_GRID_ZUBACHEW,
    FINGER_TO_COL_ZUBACHEW,
)


def find_finger(character, keyboard_layout):
    """Find which finger types the character."""
    for finger_name, characters in keyboard_layout.items():
        if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
            return finger_name, 0
    # Проверяем дополнительные символы
    if keyboard_layout is KEYBOARD_FINGER_QWERTY:
        for finger_name, characters in KEYBOARD_FINGER_QWERTY_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    elif keyboard_layout is KEYBOARD_FINGER_VYZOV:
        for finger_name, characters in KEYBOARD_FINGER_VYZOV_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    elif keyboard_layout is KEYBOARD_FINGER_DICTOR:
        for finger_name, characters in KEYBOARD_FINGER_DICTOR_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    elif keyboard_layout is KEYBOARD_FINGER_ANT:
        for finger_name, characters in KEYBOARD_FINGER_ANT_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    elif keyboard_layout is KEYBOARD_FINGER_RUSPHONE:
        for finger_name, characters in KEYBOARD_FINGER_RUSPHONE_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    elif keyboard_layout is KEYBOARD_FINGER_SKOROPIS:
        for finger_name, characters in KEYBOARD_FINGER_SKOROPIS_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    elif keyboard_layout is KEYBOARD_FINGER_ZUBACHEW:
        for finger_name, characters in KEYBOARD_FINGER_ZUBACHEW_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    return f"Invalid character: {character}", 0


def count_finger_load_qwerty(text):
    """Count finger load for QWERTY layout."""
    for key in QWERTY_FINGER_COUNT:
        QWERTY_FINGER_COUNT[key] = 0

    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_QWERTY)
            if finger_name in QWERTY_FINGER_COUNT:
                QWERTY_FINGER_COUNT[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_QWERTY
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_QWERTY_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_QWERTY)
        if finger_name in QWERTY_FINGER_COUNT:
            QWERTY_FINGER_COUNT[finger_name] += 1
            if char.isupper() or flag_nado == 1:
                QWERTY_FINGER_COUNT["leftfinger5"] += 1
    return list(QWERTY_FINGER_COUNT.values())


def count_finger_load_vyzov(text):
    """Count finger load for VYZOV layout."""
    finger_count = {k: 0 for k in VYZOV_FINGER_COUNT}
    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_VYZOV)
            if finger_name in finger_count:
                finger_count[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_VYZOV
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_VYZOV_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_VYZOV)
        if finger_name in finger_count:
            finger_count[finger_name] += 1
        if char.isupper() or flag_nado == 1:
            finger_count["leftfinger5"] += 1
    return list(finger_count.values())


def count_finger_load_dictor(text):
    """Count finger load for DICTOR layout."""
    finger_count = {k: 0 for k in DICTOR_FINGER_COUNT}
    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_DICTOR)
            if finger_name in finger_count:
                finger_count[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_DICTOR
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_DICTOR_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_DICTOR)
        if finger_name in finger_count:
            finger_count[finger_name] += 1
        if char.isupper() or flag_nado == 1:
            finger_count["leftfinger5"] += 1
    return list(finger_count.values())


def count_finger_load_ant(text):
    """Count finger load for ANT layout."""
    finger_count = {k: 0 for k in ANT_FINGER_COUNT}
    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_ANT)
            if finger_name in finger_count:
                finger_count[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_ANT
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_ANT_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_ANT)
        if finger_name in finger_count:
            finger_count[finger_name] += 1
        if char.isupper() or flag_nado == 1:
            finger_count["leftfinger5"] += 1
    return list(finger_count.values())


def count_finger_load_rusphone(text):
    """Count finger load for RUSPHONE layout."""
    finger_count = {k: 0 for k in RUSPHONE_FINGER_COUNT}
    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_RUSPHONE)
            if finger_name in finger_count:
                finger_count[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_RUSPHONE
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_RUSPHONE_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_RUSPHONE)
        if finger_name in finger_count:
            finger_count[finger_name] += 1
        if char.isupper() or flag_nado == 1:
            finger_count["leftfinger5"] += 1
    return list(finger_count.values())


def count_finger_load_skoropis(text):
    """Count finger load for SKOROPIS layout."""
    finger_count = {k: 0 for k in SKOROPIS_FINGER_COUNT}
    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_SKOROPIS)
            if finger_name in finger_count:
                finger_count[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_SKOROPIS
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_SKOROPIS_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_SKOROPIS)
        if finger_name in finger_count:
            finger_count[finger_name] += 1
        if char.isupper() or flag_nado == 1:
            finger_count["leftfinger5"] += 1
    return list(finger_count.values())


def count_finger_load_zubachew(text):
    """Count finger load for ZUBACHEW layout."""
    finger_count = {k: 0 for k in ZUBACHEW_FINGER_COUNT}
    for char in text:
        if char == " ":
            finger_name, _ = find_finger(" ", KEYBOARD_FINGER_ZUBACHEW)
            if finger_name in finger_count:
                finger_count[finger_name] += 1
            continue

        ch_low = char.lower()
        in_main = ch_low in VALID_KEYS_ZUBACHEW
        in_dop = any(
            ch_low in (v if isinstance(v, (list, tuple)) else [v])
            for v in KEYBOARD_FINGER_ZUBACHEW_DOP.values()
        )
        if not (in_main or in_dop):
            continue

        finger_name, flag_nado = find_finger(ch_low, KEYBOARD_FINGER_ZUBACHEW)
        if finger_name in finger_count:
            finger_count[finger_name] += 1
        if char.isupper() or flag_nado == 1:
            finger_count["leftfinger5"] += 1
    return list(finger_count.values())


def load_hand_left(load_list):
    """Calculate left hand load percentage."""
    total = sum(load_list)
    return int((sum(load_list[:5]) * 100) / total) if total > 0 else 0


def load_hand_right(load_list):
    """Calculate right hand load percentage."""
    total = sum(load_list)
    return int((sum(load_list[5:10]) * 100) / total) if total > 0 else 0


def calculate_penalties_qwerty(text):
    """Calculate movement penalties for QWERTY."""
    penalties = 0
    for char in text.lower():
        if char in IGNORE_CHARS or char not in VALID_KEYS_QWERTY:
            continue
        if char == " ":
            continue  # Пробел не даёт штрафов
        col, row = KEY_GRID_QWERTY[char]
        home_char = None
        for h in HOME_KEYS_QWERTY:
            if KEY_GRID_QWERTY[h][0] == col:
                home_char = h
                break
        if home_char is None:
            penalties += 2
            continue
        home_row = KEY_GRID_QWERTY[home_char][1]
        dy = abs(row - home_row)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2
    return penalties


def calculate_penalties_vyzov(text):
    """Calculate movement + shift penalties for VYZOV."""
    penalties = 0
    dop_chars = set()
    for chars in KEYBOARD_FINGER_VYZOV_DOP.values():
        dop_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

    for char in text.lower():
        if char in IGNORE_CHARS:
            continue
        if char == " ":
            continue

        if char not in VALID_KEYS_VYZOV and char not in dop_chars:
            continue

        col, row = None, None
        if char in KEY_GRID_VYZOV:
            col, row = KEY_GRID_VYZOV[char]
        else:
            for finger, chars in KEYBOARD_FINGER_VYZOV_DOP.items():
                if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
                    col = FINGER_TO_COL_VYZOV.get(finger)
                    row = 0
                    break
        if col is None or col >= len(HOME_ROW_VYZOV):
            penalties += 2
            continue

        dy = abs(row - 1)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

        if char in dop_chars:
            penalties += 1
    return penalties


def calculate_penalties_dictor(text):
    """Calculate movement + shift penalties for DICTOR."""
    penalties = 0
    dop_chars = set()
    for chars in KEYBOARD_FINGER_DICTOR_DOP.values():
        dop_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

    for char in text.lower():
        if char in IGNORE_CHARS:
            continue
        if char == " ":
            continue

        if char not in VALID_KEYS_DICTOR and char not in dop_chars:
            continue

        col, row = None, None
        if char in KEY_GRID_DICTOR:
            col, row = KEY_GRID_DICTOR[char]
        else:
            for finger, chars in KEYBOARD_FINGER_DICTOR_DOP.items():
                if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
                    col = FINGER_TO_COL_DICTOR.get(finger)
                    row = 0
                    break
        if col is None or col >= len(HOME_ROW_DICTOR):
            penalties += 2
            continue

        dy = abs(row - 1)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

        if char in dop_chars:
            penalties += 1
    return penalties


def calculate_penalties_ant(text):
    """Calculate movement + shift penalties for ANT."""
    penalties = 0
    dop_chars = set()
    for chars in KEYBOARD_FINGER_ANT_DOP.values():
        dop_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

    for char in text.lower():
        if char in IGNORE_CHARS:
            continue
        if char == " ":
            continue

        if char not in VALID_KEYS_ANT and char not in dop_chars:
            continue

        col, row = None, None
        if char in KEY_GRID_ANT:
            col, row = KEY_GRID_ANT[char]
        else:
            for finger, chars in KEYBOARD_FINGER_ANT_DOP.items():
                if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
                    col = FINGER_TO_COL_ANT.get(finger)
                    row = 0
                    break
        if col is None or col >= len(HOME_KEYS_ANT):
            penalties += 2
            continue

        dy = abs(row - 1)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

        if char in dop_chars:
            penalties += 1
    return penalties


def calculate_penalties_rusphone(text):
    """Calculate movement + shift penalties for RUSPHONE."""
    penalties = 0
    dop_chars = set()
    for chars in KEYBOARD_FINGER_RUSPHONE_DOP.values():
        dop_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

    for char in text.lower():
        if char in IGNORE_CHARS:
            continue
        if char == " ":
            continue

        if char not in VALID_KEYS_RUSPHONE and char not in dop_chars:
            continue

        col, row = None, None
        if char in KEY_GRID_RUSPHONE:
            col, row = KEY_GRID_RUSPHONE[char]
        else:
            for finger, chars in KEYBOARD_FINGER_RUSPHONE_DOP.items():
                if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
                    col = FINGER_TO_COL_RUSPHONE.get(finger)
                    row = 0
                    break
        if col is None or col >= len(HOME_KEYS_RUSPHONE):
            penalties += 2
            continue

        dy = abs(row - 1)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

        if char in dop_chars:
            penalties += 1
    return penalties


def calculate_penalties_skoropis(text):
    """Calculate movement + shift penalties for SKOROPIS."""
    penalties = 0
    dop_chars = set()
    for chars in KEYBOARD_FINGER_SKOROPIS_DOP.values():
        dop_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

    for char in text.lower():
        if char in IGNORE_CHARS:
            continue
        if char == " ":
            continue

        if char not in VALID_KEYS_SKOROPIS and char not in dop_chars:
            continue

        col, row = None, None
        if char in KEY_GRID_SKOROPIS:
            col, row = KEY_GRID_SKOROPIS[char]
        else:
            for finger, chars in KEYBOARD_FINGER_SKOROPIS_DOP.items():
                if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
                    col = FINGER_TO_COL_SKOROPIS.get(finger)
                    row = 0
                    break
        if col is None or col >= len(HOME_KEYS_SKOROPIS):
            penalties += 2
            continue

        dy = abs(row - 1)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

        if char in dop_chars:
            penalties += 1
    return penalties


def calculate_penalties_zubachew(text):
    """Calculate movement + shift penalties for ZUBACHEW."""
    penalties = 0
    dop_chars = set()
    for chars in KEYBOARD_FINGER_ZUBACHEW_DOP.values():
        dop_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

    for char in text.lower():
        if char in IGNORE_CHARS:
            continue
        if char == " ":
            continue

        if char not in VALID_KEYS_ZUBACHEW and char not in dop_chars:
            continue

        col, row = None, None
        if char in KEY_GRID_ZUBACHEW:
            col, row = KEY_GRID_ZUBACHEW[char]
        else:
            for finger, chars in KEYBOARD_FINGER_ZUBACHEW_DOP.items():
                if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
                    col = FINGER_TO_COL_ZUBACHEW.get(finger)
                    row = 0
                    break
        if col is None or col >= len(HOME_KEYS_ZUBACHEW):
            penalties += 2
            continue

        dy = abs(row - 1)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2

        if char in dop_chars:
            penalties += 1
    return penalties
