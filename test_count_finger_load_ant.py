import pytest
from function import (
    count_finger_load_ant,
    ANT_FINGER_COUNT,
    KEYBOARD_FINGER_ANT,
    KEYBOARD_FINGER_ANT_DOP,
    VALID_KEYS_ANT,
)


@pytest.fixture(scope="session")
def finger_order():
    """Фиксированный порядок пальцев, как определено в ANT_FINGER_COUNT."""
    return list(ANT_FINGER_COUNT.keys())


@pytest.fixture(scope="session")
def idx(finger_order):
    """Вспомогательная функция: возвращает индекс пальца по его имени."""
    def _idx(name: str) -> int:
        return finger_order.index(name)
    return _idx


@pytest.fixture(scope="session")
def zero_counts(finger_order):
    """Список нулей длины, равной количеству пальцев — для инициализации ожидаемых значений."""
    return [0] * len(finger_order)


def test_empty_string(zero_counts):
    """Проверяет, что пустая строка возвращает список из нулей (никакой нагрузки)."""
    assert count_finger_load_ant("") == zero_counts


def test_only_spaces(finger_order, idx, zero_counts):
    """Проверяет обработку пробелов: каждый пробел должен увеличивать счётчик 'leftfinger1'."""
    res = count_finger_load_ant("   ")
    expected = zero_counts.copy()
    expected[idx("leftfinger1")] = 3
    assert res == expected


def test_lowercase_letter_in_main(finger_order, idx, zero_counts):
    """Проверяет, что строчная буква из основной раскладки (например, 'ф') учитывается
    за нужный палец без дополнительного нажатия Shift (leftfinger5 не увеличивается)."""
    res = count_finger_load_ant("ф")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_uppercase_letter_adds_shift(finger_order, idx, zero_counts):
    """Проверяет, что заглавная буква (например, 'Ф') учитывается:
    - 1 раз за саму букву (в её пальце),
    - 1 раз за нажатие Shift (в 'leftfinger5')."""
    res = count_finger_load_ant("Ф")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 2
    assert res == expected


def test_dop_symbol_exclamation(finger_order, idx, zero_counts):
    """Проверяет символ из дополнительной раскладки ('!' ∈ leftfinger5 DOP):
    - 1 раз за сам символ (в его пальце),
    - 1 раз за нажатие Shift (flag_nado == 1 → +1 к 'leftfinger5')."""
    res = count_finger_load_ant("!")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 2
    assert res == expected


def test_dop_symbol_at_sign(finger_order, idx, zero_counts):
    """Проверяет другой символ из доп. раскладки ('@' ∈ leftfinger4 DOP):
    - 1 раз за символ (в 'leftfinger4'),
    - 1 раз за Shift (в 'leftfinger5')."""
    res = count_finger_load_ant("@")
    expected = zero_counts.copy()
    expected[idx("leftfinger4")] = 1
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_invalid_characters_ignored(finger_order, idx, zero_counts):
    """Проверяет, что недопустимые символы (например, '[', ']') игнорируются,
    а допустимые (например, 'ф') обрабатываются корректно."""
    res = count_finger_load_ant("[ф]")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 1  # только 'ф' учитывается
    assert res == expected


def test_mixed_valid_text(finger_order, idx, zero_counts):
    """Проверяет смешанный ввод: заглавная буква и доп-символ.
    'А' → 'а' в leftfinger3 + Shift,
    '!' → в leftfinger5 + Shift.
    Итого: leftfinger3=1, leftfinger5=1 (символ) + 2 (два Shift'а)."""
    res = count_finger_load_ant("А!")
    expected = zero_counts.copy()
    expected[idx("leftfinger3")] = 1  # за "а"
    expected[idx("leftfinger5")] = 1  # за "!"
    expected[idx("leftfinger5")] += 2  # два Shift'а: от "А" и от "!"
    assert res == expected
