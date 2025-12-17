import pytest
from function import classify_word, FINGER_TO_IDX
from keyboard import KEYBOARD_QWERTY, KEY_GRID_QWERTY


# === ВСПОМОГАТЕЛЬНЫЕ ДАННЫЕ ===

# Искусственная раскладка для тестов
ROLL_LAYOUT = {
    "leftfinger5": ("p",),
    "leftfinger4": ("o",),
    "leftfinger3": ("i",),
    "leftfinger2": ("u",),
    "leftfinger1": (),
    "rightfinger2": ("q",),
    "rightfinger3": ("w",),
    "rightfinger4": ("e",),
    "rightfinger5": ("r",),
}

ROLL_GRID = {
    "p": (0, 1), "o": (1, 1), "i": (2, 1), "u": (3, 1),  # всё в строке 1
    "q": (4, 1), "w": (5, 1), "e": (6, 1), "r": (7, 1),
}

# Раскладка с символом вне grid
PARTIAL_GRID_LAYOUT = {"leftfinger2": ("a", "b")}
PARTIAL_GRID = {"a": (0, 1)}  # 'b' отсутствует


# === ТЕСТЫ ===

def test_word_too_short():
    """Слова короче 2 букв возвращают (None, None)."""
    assert classify_word("a", KEYBOARD_QWERTY, KEY_GRID_QWERTY) == (None, None)
    assert classify_word("", KEYBOARD_QWERTY, KEY_GRID_QWERTY) == (None, None)


def test_unknown_char_or_pinky():
    """Символ без пальца или pinky (left1/right1) → (None, None)."""
    # Неизвестный символ
    assert classify_word("ax", KEYBOARD_QWERTY, KEY_GRID_QWERTY) == (None, None)  # 'a' есть, 'x' — латинская, нет в QWERTY
    # Pinky (в ваших раскладках left1/right1 пустые, но проверим явно)
    pinky_layout = {"leftfinger1": ("z",), "leftfinger2": ("a",)}
    pinky_grid = {"z": (0, 1), "a": (1, 1)}
    assert classify_word("za", pinky_layout, pinky_grid) == (None, None)  # содержит leftfinger1


def test_char_not_in_grid():
    """Символ есть в layout, но отсутствует в grid → semi."""
    result = classify_word("ab", PARTIAL_GRID_LAYOUT, PARTIAL_GRID)
    assert result == ("semi", "left")  # 'a' в grid, 'b' нет → rows = [1, -1] → semi


def test_two_hands_inconvenient():
    """Слово двумя руками → inconvenient."""
    # В QWERTY: "й" — левая, "н" — правая
    result = classify_word("йн", KEYBOARD_QWERTY, KEY_GRID_QWERTY)
    assert result == ("inconvenient", None)


def test_convenient_left_roll():
    """Удобный перебор левой рукой: индексы пальцев возрастают (left5→left2 = 0→3)."""
    result = classify_word("poiu", ROLL_LAYOUT, ROLL_GRID)  # p(0) → o(1) → i(2) → u(3)
    assert result == ("convenient", "left")


def test_convenient_right_roll():
    """Удобный перебор правой рукой: индексы пальцев убывают (right2→right5 = 6→9 → должно быть 9→8→7→6)."""
    result = classify_word("rewq", ROLL_LAYOUT, ROLL_GRID)
    assert result == ("convenient", "right")


def test_left_roll_wrong_direction():
    """Левая рука: убывающие индексы → не удобный (semi)."""
    result = classify_word("uipo", ROLL_LAYOUT, ROLL_GRID)
    assert result == ("semi", "left")


def test_right_roll_wrong_direction():
    """Правая рука: возрастающие индексы → не удобный (semi)."""
    result = classify_word("qwer", ROLL_LAYOUT, ROLL_GRID)  # q(6)→w(7)→e(8)→r(9) — возрастает
    assert result == ("semi", "right")


def test_not_same_row():
    """Одноручное слово, но символы в разных рядах → semi."""
    mixed_grid = {
        "a": (0, 1),  # home
        "b": (0, 2),  # bottom
    }
    layout = {"leftfinger2": ("a", "b")}
    result = classify_word("ab", layout, mixed_grid)
    assert result == ("semi", "left")


def test_all_same_row_but_not_roll():
    """Одноручное, одна строка, но не монотонный перебор → semi."""
    # "pui" → p(0) → u(3) → i(2) → не возрастает
    result = classify_word("pui", ROLL_LAYOUT, ROLL_GRID)
    assert result == ("semi", "left")


def test_finger_not_in_finger_to_idx():
    """Палец отсутствует в FINGER_TO_IDX → semi."""
    bad_layout = {"leftfinger99": ("z",), "leftfinger2": ("a",)}
    bad_grid = {"z": (0, 1), "a": (1, 1)}
    result = classify_word("za", bad_layout, bad_grid)
    assert result == ("semi", "left")


def test_real_qwerty_convenient_examples():
    """Примеры удобных рулонов в QWERTY (если существуют)."""
    # В QWERTY сложно найти чистые рулоны, но проверим, что функция не падает
    # Например, "фы" — lf5 + lf4 → индексы: 0,1 → возрастает → удобный?
    result = classify_word("фы", KEYBOARD_QWERTY, KEY_GRID_QWERTY)
    # "ф": (0,1) → row=1, "ы": (1,1) → row=1 → same row
    # fingers: ["leftfinger5", "leftfinger4"] → idx: [0, 1] → возрастает → convenient
    assert result == ("convenient", "left")

    # "жд" — rf5 + rf4 → idx: [9,8] → убывает → удобный
    result = classify_word("жд", KEYBOARD_QWERTY, KEY_GRID_QWERTY)
    assert result == ("convenient", "right")


def test_real_qwerty_semi_examples():
    """Примеры полуудобных слов в QWERTY."""
    # "ав" — lf2 + lf3 → idx: [3,2] → убывает → не удобный для левой → semi
    result = classify_word("ав", KEYBOARD_QWERTY, KEY_GRID_QWERTY)
    assert result == ("semi", "left")
