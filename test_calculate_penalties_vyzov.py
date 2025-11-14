import pytest
from function import calculate_penalties_vyzov, \
    KEYBOARD_FINGER_VYZOV, KEYBOARD_FINGER_VYZOV_DOP, \
    FINGER_TO_COL_VYZOV, KEY_GRID_VYZOV, VALID_KEYS_VYZOV, IGNORE_CHARS, HOME_ROW_VYZOV


# -------------------------------------------------
# Фикстуры
# -------------------------------------------------

@pytest.fixture
def vyzov_layout():
    return KEYBOARD_FINGER_VYZOV

@pytest.fixture
def vyzov_dop_layout():
    return KEYBOARD_FINGER_VYZOV_DOP

@pytest.fixture
def vyzov_key_grid():
    return KEY_GRID_VYZOV

@pytest.fixture
def vyzov_valid_keys():
    return VALID_KEYS_VYZOV

@pytest.fixture
def vyzov_ignore_chars():
    return IGNORE_CHARS

@pytest.fixture
def vyzov_home_row():
    return HOME_ROW_VYZOV


# -------------------------------------------------
# Тесты
# -------------------------------------------------

def test_calculate_penalties_vyzov_empty():
    """Тест: пустой текст — 0 штрафов."""
    assert calculate_penalties_vyzov("") == 0


def test_calculate_penalties_vyzov_home_row(vyzov_home_row):
    """Тест: символы из домашнего ряда — 0 штрафов."""
    # HOME_ROW_VYZOV = ["ч", "и", "е", "а", "н", "т", "с", "б"]
    text = "".join(vyzov_home_row)
    assert calculate_penalties_vyzov(text) == 0


def test_calculate_penalties_vyzov_uppercase_ignored():
    """Тест: заглавные буквы приводятся к нижнему регистру и обрабатываются."""
    text = "ЧИЕА"
    assert calculate_penalties_vyzov(text) == 0


def test_calculate_penalties_vyzov_main_char_top():
    """Тест: символ из основной раскладки, но в верхнем ряду (если есть)."""
    # В VYZOV в KEY_GRID_VYZOV только row=1 (домашний) и row=2 (нижний)
    # Нет символов с row=0 в основной раскладке
    # Поэтому этот тест не применим
    pass


def test_calculate_penalties_vyzov_main_char_bottom():
    """Тест: символ из основной раскладки, но в нижнем ряду — 1 штраф."""
    # row = 2 → dy = abs(2 - 1) = 1 → штраф = 1
    text = "ч"  # домашний
    assert calculate_penalties_vyzov(text) == 0

    text = "я"  # допустим, есть в нижнем ряду
    # Проверим, есть ли "я" в KEY_GRID_VYZOV
    # В KEY_GRID_VYZOV:
    # "я": (0, 2)
    assert calculate_penalties_vyzov("я") == 1


def test_calculate_penalties_vyzov_space_ignored():
    """Тест: пробелы не дают штрафов."""
    text = "ч и е а"
    assert calculate_penalties_vyzov(text) == 0


def test_calculate_penalties_vyzov_ignore_chars(vyzov_ignore_chars):
    """Тест: символы из IGNORE_CHARS игнорируются."""
    text = f"ч{list(vyzov_ignore_chars)[0]}е"
    assert calculate_penalties_vyzov(text) == 0


def test_calculate_penalties_vyzov_invalid_chars():
    """Тест: невалидные символы игнорируются."""
    text = "ч木е"
    # '木' не в VALID_KEYS_VYZOV и не в DOP → игнорируется
    assert calculate_penalties_vyzov(text) == 0


def test_calculate_penalties_vyzov_only_ignore(vyzov_ignore_chars):
    """Тест: только игнорируемые символы — 0 штрафов."""
    text = "".join(list(vyzov_ignore_chars)[:5])
    assert calculate_penalties_vyzov(text) == 0
