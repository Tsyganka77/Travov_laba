"""Functions for calculating finger load, penalties, and convenient rolls."""

import re
from keyboard import (
    KEYBOARD_QWERTY, KEYBOARD_VYZOV, KEYBOARD_DICTOR,
    KEYBOARD_ANT, KEYBOARD_RUSPHONE, KEYBOARD_SKOROPIS, KEYBOARD_ZUBACHEW,
    KEY_GRID_QWERTY, KEY_GRID_VYZOV, KEY_GRID_DICTOR,
    KEY_GRID_ANT, KEY_GRID_RUSPHONE, KEY_GRID_SKOROPIS,
    KEY_GRID_ZUBACHEW, HOME_KEYS_QWERTY, HOME_KEYS_VYZOV,
    HOME_KEYS_DICTOR, HOME_KEYS_ANT, HOME_KEYS_RUSPHONE,
    HOME_KEYS_SKOROPIS, HOME_KEYS_ZUBACHEW,  # ← ДОБАВЛЕНО!
    FINGER_TO_IDX,
    VALID_KEYS_QWERTY, VALID_KEYS_VYZOV, VALID_KEYS_DICTOR,
    VALID_KEYS_ANT, VALID_KEYS_RUSPHONE, VALID_KEYS_SKOROPIS,
    VALID_KEYS_ZUBACHEW,
)

# === Вспомогательные функции ===

def find_finger(char, layout):
    """Find finger for char (case-sensitive), return finger name or None."""
    for finger, chars in layout.items():
        if char in (chars if isinstance(chars, (list, tuple)) else [chars]):
            return finger
    return None

def filter_single_char_words(text):
    """Remove standalone single-letter words (like 'и', 'а'), but keep punctuation and digits."""
    return re.sub(r'\b[^\W\d_]\b', '', text)

def is_convenient_roll(finger_seq):
    """Check if finger sequence is a convenient roll (inward for one hand)."""
    if len(finger_seq) < 2:
        return False
    try:
        idx_seq = [FINGER_TO_IDX[f] for f in finger_seq]
    except KeyError:
        return False
    if all(i <= 4 for i in idx_seq):  # left hand: 0→1→2→3→4 (increasing)
        return all(idx_seq[i+1] > idx_seq[i] for i in range(len(idx_seq)-1))
    elif all(i >= 5 for i in idx_seq):  # right hand: 9→8→7→6→5 (decreasing)
        return all(idx_seq[i+1] < idx_seq[i] for i in range(len(idx_seq)-1))
    else:
        return False  # mixed hands

def count_convenient_rolls(text, layout):
    words = re.findall(r'\b[^\W\d_]+\b', text, re.UNICODE)  # only letter-words
    count = 0
    for word in words:
        if len(word) < 2:
            continue
        fingers = []
        for ch in word:
            f = find_finger(ch, layout)
            if f is None:
                f = find_finger(ch.lower(), layout)
            if f and f != "leftfinger1":
                fingers.append(f)
        if len(fingers) == len(word) and is_convenient_roll(fingers):
            count += 1
    return count

# === Подсчёт нагрузки (без пробелов!) ===

def count_finger_load(text, layout):
    counts = {f"leftfinger{i}": 0 for i in range(1, 6)}
    counts.update({f"rightfinger{i}": 0 for i in range(1, 6)})
    for char in text:
        if char == ' ':  # ← пробелы НЕ учитываются
            continue
        finger = find_finger(char, layout)
        if finger is None:
            finger = find_finger(char.lower(), layout)
        if finger and finger in counts:
            counts[finger] += 1
    return [counts[f"leftfinger{i}"] for i in range(5, 0, -1)] + \
           [counts[f"rightfinger{i}"] for i in range(1, 6)]

def load_hand_left(load_list):
    return int((sum(load_list[:5]) * 100) / sum(load_list)) if sum(load_list) else 0

def load_hand_right(load_list):
    return int((sum(load_list[5:]) * 100) / sum(load_list)) if sum(load_list) else 0

# === Штрафы (только за смещение, Shift уже в нагрузке) ===

def calculate_penalties(text, layout, grid, home_keys):
    penalties = 0
    for char in text:
        if char == ' ':
            continue
        ch = char if char in grid else char.lower()
        if ch not in grid:
            penalties += 2  # unknown char
            continue
        col, row = grid[ch]
        home_row = 1
        dy = abs(row - home_row)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2
    return penalties

# === Интерфейсные функции (для main) ===

def count_finger_load_qwerty(text): return count_finger_load(text, KEYBOARD_QWERTY)
def count_finger_load_vyzov(text): return count_finger_load(text, KEYBOARD_VYZOV)
def count_finger_load_dictor(text): return count_finger_load(text, KEYBOARD_DICTOR)
def count_finger_load_ant(text): return count_finger_load(text, KEYBOARD_ANT)
def count_finger_load_rusphone(text): return count_finger_load(text, KEYBOARD_RUSPHONE)
def count_finger_load_skoropis(text): return count_finger_load(text, KEYBOARD_SKOROPIS)
def count_finger_load_zubachew(text): return count_finger_load(text, KEYBOARD_ZUBACHEW)

def calculate_penalties_qwerty(text): return calculate_penalties(text, KEYBOARD_QWERTY, KEY_GRID_QWERTY, HOME_KEYS_QWERTY)
def calculate_penalties_vyzov(text): return calculate_penalties(text, KEYBOARD_VYZOV, KEY_GRID_VYZOV, HOME_KEYS_VYZOV)
def calculate_penalties_dictor(text): return calculate_penalties(text, KEYBOARD_DICTOR, KEY_GRID_DICTOR, HOME_KEYS_DICTOR)
def calculate_penalties_ant(text): return calculate_penalties(text, KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT)
def calculate_penalties_rusphone(text): return calculate_penalties(text, KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE, HOME_KEYS_RUSPHONE)
def calculate_penalties_skoropis(text): return calculate_penalties(text, KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS, HOME_KEYS_SKOROPIS)
def calculate_penalties_zubachew(text): return calculate_penalties(text, KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW, HOME_KEYS_ZUBACHEW)

def count_convenient_rolls_qwerty(text): return count_convenient_rolls(text, KEYBOARD_QWERTY)
def count_convenient_rolls_vyzov(text): return count_convenient_rolls(text, KEYBOARD_VYZOV)
def count_convenient_rolls_dictor(text): return count_convenient_rolls(text, KEYBOARD_DICTOR)
def count_convenient_rolls_ant(text): return count_convenient_rolls(text, KEYBOARD_ANT)
def count_convenient_rolls_rusphone(text): return count_convenient_rolls(text, KEYBOARD_RUSPHONE)
def count_convenient_rolls_skoropis(text): return count_convenient_rolls(text, KEYBOARD_SKOROPIS)
def count_convenient_rolls_zubachew(text): return count_convenient_rolls(text, KEYBOARD_ZUBACHEW)
