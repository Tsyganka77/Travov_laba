import pytest
from function import (
    count_finger_load_zubachew,
    ZUBACHEW_FINGER_COUNT,
    KEYBOARD_FINGER_ZUBACHEW,
    KEYBOARD_FINGER_ZUBACHEW_DOP,
    VALID_KEYS_ZUBACHEW,
)


@pytest.fixture(scope="session")
def finger_order():
    """Фиксированный порядок пальцев, как определено в ZUBACHEW_FINGER_COUNT.
    Поскольку ZUBACHEW идентичен ANT, порядок такой же, как в ANT_FINGER_COUNT."""
    return list(ZUBACHEW_FINGER_COUNT.keys())


@pytest.fixture(scope="session")
def idx(finger_order):
    """Вспомогательная функция: возвращает индекс пальца по его имени."""
    def _idx(name: str) -> int:
        return finger_order.index(name)
    return _idx


@pytest.fixture(scope="session")
def zero_counts(finger_order):
    """Список нулей длины, равной количеству пальцев."""
    return [0] * len(finger_order)


def test_empty_string(zero_counts):
    """Проверяет, что пустая строка возвращает список из нулей."""
    assert count_finger_load_zubachew("") == zero_counts


def test_only_spaces(finger_order, idx, zero_counts):
    """Проверяет, что каждый пробел увеличивает счётчик 'leftfinger1'."""
    res = count_finger_load_zubachew("  ")
    expected = zero_counts.copy()
    expected[idx("leftfinger1")] = 2
    assert res == expected


def test_lowercase_letter_in_main(finger_order, idx, zero_counts):
    """Проверяет строчную букву из основной раскладки (например, 'ф').
    В ZUBACHEW (как и в ANT): 'ф' → leftfinger5."""
    res = count_finger_load_zubachew("ф")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_uppercase_letter_adds_shift(finger_order, idx, zero_counts):
    """Проверяет, что заглавная буква вызывает:
    - 1 нажатие основного пальца,
    - 1 нажатие leftfinger5 (Shift)."""
    res = count_finger_load_zubachew("Ф")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 2
    assert res == expected


def test_dop_symbol_exclamation(finger_order, idx, zero_counts):
    """Проверяет символ '!', который в ZUBACHEW_DOP относится к leftfinger5:
    - 1 за символ,
    - 1 за Shift (flag_nado == 1)."""
    res = count_finger_load_zubachew("!")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 2
    assert res == expected


def test_dop_symbol_at_sign(finger_order, idx, zero_counts):
    """Проверяет символ '@', который в ZUBACHEW_DOP относится к leftfinger4:
    - 1 за символ (leftfinger4),
    - 1 за Shift (leftfinger5)."""
    res = count_finger_load_zubachew("@")
    expected = zero_counts.copy()
    expected[idx("leftfinger4")] = 1
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_invalid_characters_ignored(finger_order, idx, zero_counts):
    """Проверяет, что недопустимые символы игнорируются,
    а допустимые (например, 'ф') обрабатываются."""
    res = count_finger_load_zubachew("[ф]")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_mixed_valid_text(finger_order, idx, zero_counts):
    """Проверяет комбинацию заглавной буквы и доп-символа:
    'Ф!' → leftfinger5 (буква) + leftfinger5 (символ) + 2×Shift → итого 4 в leftfinger5."""
    res = count_finger_load_zubachew("Ф!")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 4
    assert res == expected
