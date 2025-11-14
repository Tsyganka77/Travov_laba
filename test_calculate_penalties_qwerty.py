import pytest
from function import calculate_penalties_qwerty, HOME_KEYS_QWERTY, KEY_GRID_QWERTY, IGNORE_CHARS, VALID_KEYS_QWERTY


# -------------------------------------------------
# Фикстуры
# -------------------------------------------------

@pytest.fixture
def home_keys():
    return HOME_KEYS_QWERTY

@pytest.fixture
def key_grid():
    return KEY_GRID_QWERTY

@pytest.fixture
def ignore_chars():
    return IGNORE_CHARS

@pytest.fixture
def valid_keys():
    return VALID_KEYS_QWERTY


# -------------------------------------------------
# Тесты
# -------------------------------------------------

def test_calculate_penalties_qwerty_empty():
    """Тест: пустой текст — 0 штрафов."""
    assert calculate_penalties_qwerty("") == 0


def test_calculate_penalties_qwerty_home_row(home_keys):
    """Тест: символы из домашнего ряда — 0 штрафов."""
    # HOME_KEYS_QWERTY = {"ф", "ы", "в", "а", "о", "л", "д", "ж"}
    text = "".join(home_keys)
    assert calculate_penalties_qwerty(text) == 0


def test_calculate_penalties_qwerty_uppercase_ignored():
    """Тест: заглавные буквы приводятся к нижнему регистру и обрабатываются."""
    text = "ФЫВАОЛДЖ"
    assert calculate_penalties_qwerty(text) == 0


def test_calculate_penalties_qwerty_space_ignored():
    """Тест: пробелы не дают штрафов."""
    text = "ф ы в а о"
    assert calculate_penalties_qwerty(text) == 0


def test_calculate_penalties_qwerty_ignore_chars(ignore_chars):
    """Тест: символы из IGNORE_CHARS игнорируются."""
    # Возьмём несколько из них
    ignore_sample = "!@#$%^&*()_+"
    text = f"ф{ignore_sample}в"
    # Только 'ф' и 'в' — домашние → 0 штрафов
    assert calculate_penalties_qwerty(text) == 0


def test_calculate_penalties_qwerty_invalid_chars(valid_keys):
    """Тест: невалидные символы игнорируются."""
    # Предположим, что '木' нет в valid_keys
    text = "ф木в"
    # '木' не в VALID_KEYS_QWERTY → игнорируется
    assert calculate_penalties_qwerty(text) == 0


def test_calculate_penalties_qwerty_no_home_key():
    """Тест: символ, столбец которого не имеет домашней клавиши — 2 штрафа."""
    # В вашем KEY_GRID_QWERTY столбцы 10 и 11: 'х': (10,0), 'ъ': (11,0)
    # HOME_KEYS_QWERTY: {"ф":(0,1), "ы":(1,1), ..., "ж":(9,1)}
    # Столбцы 10 и 11 — нет соответствия в HOME_KEYS_QWERTY
    # Значит, 'х' и 'ъ' должны давать по 2 штрафа каждый
    text = "хъ"
    assert calculate_penalties_qwerty(text) == 4  # 2 + 2


def test_calculate_penalties_qwerty_only_ignore(ignore_chars):
    """Тест: только игнорируемые символы — 0 штрафов."""
    text = "".join(list(ignore_chars)[:10])  # Возьмём первые 10 символов из ignore_chars
    assert calculate_penalties_qwerty(text) == 0
