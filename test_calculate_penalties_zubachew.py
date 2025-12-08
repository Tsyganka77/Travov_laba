import pytest
from function import (
    calculate_penalties_zubachew,
    calculate_penalties_ant,
    KEYBOARD_FINGER_ZUBACHEW,
    KEYBOARD_FINGER_ZUBACHEW_DOP,
    KEY_GRID_ZUBACHEW,
    FINGER_TO_COL_ZUBACHEW,
    HOME_KEYS_ZUBACHEW,
    IGNORE_CHARS,
    VALID_KEYS_ZUBACHEW,
)


def test_zubachew_identical_to_ant():
    """Проверяет, что для любого текста штрафы Zubachew и ANT совпадают,
    поскольку раскладки полностью идентичны."""
    test_cases = [
        "",
        " ",
        "а о у л д ж",           # home row
        "ф ш э ё",               # bottom row
        "!", "@", "1", "2",      # top row (DOP)
        "ФШЭ!",                  # uppercase + DOP
        "Привет, Мир! Это ANT/Zubachew.",
        " ,.!?;:\"'()[]{}-_+=*/\\|@#$%^&`~",
        "аф!юё@",                # mixed: home + bottom + DOP
        "[\x00€",                # invalid chars
    ]
    for text in test_cases:
        assert calculate_penalties_zubachew(text) == calculate_penalties_ant(text), \
            f"Несовпадение для текста: {repr(text)}"


# --- Дополнительные smoke-тесты для уверенности (необязательны, но полезны) ---

def test_empty_and_ignored_chars():
    """Базовые случаи: пустая строка, пробелы, игнорируемые символы → 0 штрафов."""
    assert calculate_penalties_zubachew("") == 0
    assert calculate_penalties_zubachew(" ,.!? \t\n") == 0


def test_home_row_no_penalty():
    """Символы из home-ряда (а, е, и, о, у, л, д, ж) не дают штрафа."""
    for char in HOME_KEYS_ZUBACHEW:
        assert calculate_penalties_zubachew(char) == 0


def test_bottom_row_penalty_1():
    """Буквы из нижнего ряда (например, 'ф') → +1 за движение."""
    assert calculate_penalties_zubachew("ф") == 1



def test_case_insensitive():
    """Регистр не влияет — функция использует .lower()."""
    assert calculate_penalties_zubachew("Ф") == calculate_penalties_zubachew("ф")
