import pytest
from function import (
    calculate_penalties_ant,
    KEYBOARD_FINGER_ANT,
    KEYBOARD_FINGER_ANT_DOP,
    KEY_GRID_ANT,
    FINGER_TO_COL_ANT,
    HOME_KEYS_ANT,
    IGNORE_CHARS,
    VALID_KEYS_ANT,
)


def test_empty_string():
    """Пустая строка → 0 штрафов."""
    assert calculate_penalties_ant("") == 0


def test_ignored_chars_and_spaces():
    """Пробелы и IGNORE_CHARS (.,!? и др.) полностью игнорируются → 0 штрафов."""
    text = " ,.!?;:\"'()[]{}-_+=*/\\|@#$%^&`~ \t\n\r"
    assert calculate_penalties_ant(text) == 0


def test_valid_home_row_char_no_penalty():
    """Символы из home-ряда (row=1) не дают штрафа за движение.
    Например, 'а', 'е', 'и', 'о', 'у', 'л', 'д', 'ж' → row=1 → dy=0 → 0 за движение.
    И если они не в DOP — нет и штрафа за Shift."""
    for char in HOME_KEYS_ANT:
        assert calculate_penalties_ant(char) == 0


def test_valid_bottom_row_char_penalty_1():
    """Символы из нижнего ряда (row=2) → dy = |2-1| = 1 → штраф +1.
    Пример: 'ф' — в ANT, row=2, не в DOP → только +1."""
    # 'ф' ∈ KEYBOARD_FINGER_ANT → row=2
    assert calculate_penalties_ant("ф") == 1


def test_dop_symbol_adds_extra_penalty():
    """Любой символ из KEYBOARD_FINGER_ANT_DOP даёт +1 за использование доп-ряда (Shift)."""
    # '1' ∈ leftfinger5 DOP → row=0 → +1 (движение) +1 (DOP) = 2
    assert calculate_penalties_ant("1") == 2


def test_lowercase_letter_not_in_dop_no_extra_penalty():
    """Строчные буквы из основной раскладки, даже если не в home-ряду,
    не получают штраф за DOP — только за движение."""
    # 'ф' → row=2 → +1, не в DOP → итого 1
    assert calculate_penalties_ant("ф") == 1
    # 'я' → row=2 → +1
    assert calculate_penalties_ant("я") == 1


def test_invalid_char_ignored_no_penalty():
    """Недопустимые символы (не в VALID_KEYS_ANT и не в DOP) игнорируются → 0 штрафов."""
    assert calculate_penalties_ant("[") == 0
    assert calculate_penalties_ant("€") == 0


def test_case_insensitive():
    """Функция приводит текст к нижнему регистру → 'Ф' и 'ф' дают одинаковый результат."""
    assert calculate_penalties_ant("Ф") == calculate_penalties_ant("ф")
    assert calculate_penalties_ant("А") == calculate_penalties_ant("а") == 0
