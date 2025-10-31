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
)


def find_finger(character, keyboard_layout):
    """Find which finger types the character."""
    for finger_name, characters in keyboard_layout.items():
        if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
            return finger_name, 0
    if keyboard_layout is KEYBOARD_FINGER_QWERTY:
        for finger_name, characters in KEYBOARD_FINGER_QWERTY_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    if keyboard_layout is KEYBOARD_FINGER_VYZOV:
        for finger_name, characters in KEYBOARD_FINGER_VYZOV_DOP.items():
            if character in (characters if isinstance(characters, (list, tuple)) else [characters]):
                return finger_name, 1
    if keyboard_layout is KEYBOARD_FINGER_DICTOR:
        for finger_name, characters in KEYBOARD_FINGER_DICTOR_DOP.items():
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
