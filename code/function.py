import re
import csv
from keyboard import (
    KEYBOARD_QWERTY, KEYBOARD_VYZOV, KEYBOARD_DICTOR,
    KEYBOARD_ANT, KEYBOARD_RUSPHONE, KEYBOARD_SKOROPIS, KEYBOARD_ZUBACHEW,
    KEY_GRID_QWERTY, KEY_GRID_VYZOV, KEY_GRID_DICTOR,
    KEY_GRID_ANT, KEY_GRID_RUSPHONE, KEY_GRID_SKOROPIS, KEY_GRID_ZUBACHEW,
    FINGER_TO_IDX,
)

def find_finger(char, layout):
    for finger, chars in layout.items():
        if isinstance(chars, str):
            if char in chars:
                return finger
        else:
            if char in chars:
                return finger
    return None

def filter_single_char_words(text):
    return re.sub(r'\b[^\W\d_]\b', '', text)

def count_finger_load(text, layout):
    counts = {f"leftfinger{i}": 0 for i in range(1, 6)}
    counts.update({f"rightfinger{i}": 0 for i in range(1, 6)})
    for char in text:
        if char == ' ':
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

def calculate_penalties(text, layout, grid, home_keys=None):
    penalties = 0
    for char in text:
        if char == ' ':
            continue
        ch = char if char in grid else char.lower()
        if ch not in grid:
            penalties += 2
            continue
        col, row = grid[ch]
        home_row = 1
        dy = abs(row - home_row)
        if dy == 1:
            penalties += 1
        elif dy >= 2:
            penalties += 2
    return penalties

def load_text(filename):
    if filename.endswith(".csv"):
        words = []
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    pair = row[1].strip()
                    if len(pair) == 2 and pair.isalpha():
                        words.append(pair)
        return " ".join(words)
    else:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r'[^а-яА-ЯёЁa-zA-Z\s]', ' ', text)
        return text

def classify_word(word, layout, grid):
    if len(word) < 2:
        return None, None
    fingers = []
    rows = []
    hand_seq = []
    for ch in word:
        f = find_finger(ch, layout)
        if f is None:
            f = find_finger(ch.lower(), layout)
        if f is None or f == "leftfinger1" or f == "rightfinger1":
            return None, None
        fingers.append(f)
        hand = 'left' if f.startswith('left') else 'right'
        hand_seq.append(hand)
        ch_key = ch if ch in grid else ch.lower()
        if ch_key in grid:
            _, row = grid[ch_key]
            rows.append(row)
        else:
            rows.append(-1)
    if -1 in rows:
        return "semi", hand_seq[0]
    if len(set(hand_seq)) > 1:
        return "inconvenient", None
    hand = hand_seq[0]
    try:
        idx_seq = [FINGER_TO_IDX[f] for f in fingers]
    except KeyError:
        return "semi", hand
    same_row = len(set(rows)) == 1
    if same_row:
        if hand == 'left':
            if all(idx_seq[i+1] > idx_seq[i] for i in range(len(idx_seq)-1)):
                return "convenient", hand
        elif hand == 'right':
            if all(idx_seq[i+1] < idx_seq[i] for i in range(len(idx_seq)-1)):
                return "convenient", hand
    return "semi", hand

def analyze_rolls(text, layout, grid):
    words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text)
    result = {
        "total": {"convenient": 0, "semi": 0, "inconvenient": 0},
        "by_length": {2: {"convenient": 0, "semi": 0, "inconvenient": 0},
                      3: {"convenient": 0, "semi": 0, "inconvenient": 0},
                      4: {"convenient": 0, "semi": 0, "inconvenient": 0},
                      5: {"convenient": 0, "semi": 0, "inconvenient": 0}},
    }
    for word in words:
        word = word.strip()
        if len(word) < 2 or len(word) > 5:
            continue
        kind, _ = classify_word(word, layout, grid)
        if kind is None:
            continue
        result["total"][kind] += 1
        result["by_length"][len(word)][kind] += 1
    return result

count_finger_load_qwerty = lambda text: count_finger_load(text, KEYBOARD_QWERTY)
count_finger_load_vyzov = lambda text: count_finger_load(text, KEYBOARD_VYZOV)
count_finger_load_dictor = lambda text: count_finger_load(text, KEYBOARD_DICTOR)
count_finger_load_ant = lambda text: count_finger_load(text, KEYBOARD_ANT)
count_finger_load_rusphone = lambda text: count_finger_load(text, KEYBOARD_RUSPHONE)
count_finger_load_skoropis = lambda text: count_finger_load(text, KEYBOARD_SKOROPIS)
count_finger_load_zubachew = lambda text: count_finger_load(text, KEYBOARD_ZUBACHEW)

calculate_penalties_qwerty = lambda text: calculate_penalties(text, KEYBOARD_QWERTY, KEY_GRID_QWERTY)
calculate_penalties_vyzov = lambda text: calculate_penalties(text, KEYBOARD_VYZOV, KEY_GRID_VYZOV)
calculate_penalties_dictor = lambda text: calculate_penalties(text, KEYBOARD_DICTOR, KEY_GRID_DICTOR)
calculate_penalties_ant = lambda text: calculate_penalties(text, KEYBOARD_ANT, KEY_GRID_ANT)
calculate_penalties_rusphone = lambda text: calculate_penalties(text, KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE)
calculate_penalties_skoropis = lambda text: calculate_penalties(text, KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS)
calculate_penalties_zubachew = lambda text: calculate_penalties(text, KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW)

analyze_rolls_qwerty = lambda text: analyze_rolls(text, KEYBOARD_QWERTY, KEY_GRID_QWERTY)
analyze_rolls_vyzov = lambda text: analyze_rolls(text, KEYBOARD_VYZOV, KEY_GRID_VYZOV)
analyze_rolls_dictor = lambda text: analyze_rolls(text, KEYBOARD_DICTOR, KEY_GRID_DICTOR)
analyze_rolls_ant = lambda text: analyze_rolls(text, KEYBOARD_ANT, KEY_GRID_ANT)
analyze_rolls_rusphone = lambda text: analyze_rolls(text, KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE)
analyze_rolls_skoropis = lambda text: analyze_rolls(text, KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS)
analyze_rolls_zubachew = lambda text: analyze_rolls(text, KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW)
