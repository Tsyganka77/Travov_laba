import pytest
from function import calculate_penalties_dictor, \
    KEYBOARD_FINGER_DICTOR, KEYBOARD_FINGER_DICTOR_DOP, \
    FINGER_TO_COL_DICTOR, KEY_GRID_DICTOR, VALID_KEYS_DICTOR, IGNORE_CHARS, HOME_ROW_DICTOR


# -------------------------------------------------
# Фикстуры
# -------------------------------------------------

@pytest.fixture
def dictor_layout():
    return KEYBOARD_FINGER_DICTOR

@pytest.fixture
def dictor_dop_layout():
    return KEYBOARD_FINGER_DICTOR_DOP

@pytest.fixture
def dictor_key_grid():
    return KEY_GRID_DICTOR

@pytest.fixture
def dictor_valid_keys():
    return VALID_KEYS_DICTOR

@pytest.fixture
def dictor_ignore_chars():
    return IGNORE_CHARS

@pytest.fixture
def dictor_home_row():
    return HOME_ROW_DICTOR


# -------------------------------------------------
# Тесты
# -------------------------------------------------

def test_calculate_penalties_dictor_empty():
    """Тест: пустой текст — 0 штрафов."""
    assert calculate_penalties_dictor("") == 0


def test_calculate_penalties_dictor_home_row(dictor_home_row):
    """Тест: символы из домашнего ряда — 0 штрафов."""
    # HOME_ROW_DICTOR = ["у", "и", "е", "а", "т", "с", "р", "й"]
    text = "".join(dictor_home_row)
    assert calculate_penalties_dictor(text) == 0


def test_calculate_penalties_dictor_uppercase_ignored():
    """Тест: заглавные буквы приводятся к нижнему регистру и обрабатываются."""
    text = "УИЕА"
    assert calculate_penalties_dictor(text) == 0


def test_calculate_penalties_dictor_main_char_bottom():
    """Тест: символ из основной раскладки, но в нижнем ряду — 1 штраф."""
    # row = 2 → dy = abs(2 - 1) = 1 → штраф = 1
    text = "у"  # домашний
    assert calculate_penalties_dictor(text) == 0

    text = "я"  # допустим, есть в нижнем ряду
    # Проверим, есть ли "я" в KEY_GRID_DICTOR
    # В KEY_GRID_DICTOR:
    # "я": (0, 2) — если есть
    assert calculate_penalties_dictor("я") == 1


def test_calculate_penalties_dictor_space_ignored():
    """Тест: пробелы не дают штрафов."""
    text = "у и е а"
    assert calculate_penalties_dictor(text) == 0


def test_calculate_penalties_dictor_ignore_chars(dictor_ignore_chars):
    """Тест: символы из IGNORE_CHARS игнорируются."""
    text = f"у{list(dictor_ignore_chars)[0]}е"
    assert calculate_penalties_dictor(text) == 0


def test_calculate_penalties_dictor_invalid_chars():
    """Тест: невалидные символы игнорируются."""
    text = "у木е"
    # '木' не в VALID_KEYS_DICTOR и не в DOP → игнорируется
    assert calculate_penalties_dictor(text) == 0


def test_calculate_penalties_dictor_only_ignore(dictor_ignore_chars):
    """Тест: только игнорируемые символы — 0 штрафов."""
    text = "".join(list(dictor_ignore_chars)[:5])
    assert calculate_penalties_dictor(text) == 0
