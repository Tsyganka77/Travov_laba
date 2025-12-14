import pytest
from function import (
    count_finger_load_rusphone,
    RUSPHONE_FINGER_COUNT,
    KEYBOARD_FINGER_RUSPHONE,
    KEYBOARD_FINGER_RUSPHONE_DOP,
    VALID_KEYS_RUSPHONE,
)


@pytest.fixture(scope="session")
def finger_order():
    """Фиксированный порядок пальцев, как определено в RUSPHONE_FINGER_COUNT."""
    return list(RUSPHONE_FINGER_COUNT.keys())


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
    assert count_finger_load_rusphone("") == zero_counts


def test_only_spaces(finger_order, idx, zero_counts):
    """Проверяет обработку пробелов: каждый пробел должен увеличивать счётчик 'leftfinger1'."""
    res = count_finger_load_rusphone("  ")
    expected = zero_counts.copy()
    expected[idx("leftfinger1")] = 2
    assert res == expected


def test_lowercase_letter_in_main(finger_order, idx, zero_counts):
    """Проверяет, что строчная буква из основной раскладки (например, 'а') учитывается
    за нужный палец без дополнительного нажатия Shift (leftfinger5 не увеличивается)."""
    # В RUSPHONE: "а" ∈ leftfinger5
    res = count_finger_load_rusphone("а")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_uppercase_letter_adds_shift(finger_order, idx, zero_counts):
    """Проверяет, что заглавная буква (например, 'А') учитывается:
    - 1 раз за саму букву (в её пальце),
    - 1 раз за нажатие Shift (в 'leftfinger5')."""
    res = count_finger_load_rusphone("А")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 2  # "а" + Shift
    assert res == expected


def test_dop_symbol_exclamation(finger_order, idx, zero_counts):
    """Проверяет символ из дополнительной раскладки ('!' ∈ leftfinger5 DOP):
    - 1 раз за сам символ (в его пальце),
    - 1 раз за нажатие Shift (flag_nado == 1 → +1 к 'leftfinger5')."""
    res = count_finger_load_rusphone("!")
    expected = zero_counts.copy()
    expected[idx("leftfinger5")] = 2
    assert res == expected


def test_dop_symbol_at_sign(finger_order, idx, zero_counts):
    """Проверяет символ '@', который в RUSPHONE_DOP находится в 'leftfinger4':
    - 1 раз за символ (в 'leftfinger4'),
    - 1 раз за Shift (в 'leftfinger5')."""
    res = count_finger_load_rusphone("@")
    expected = zero_counts.copy()
    expected[idx("leftfinger4")] = 1
    expected[idx("leftfinger5")] = 1
    assert res == expected


def test_invalid_characters_ignored(finger_order, idx, zero_counts):
    """Проверяет, что недопустимые символы (например, '[', ']') игнорируются,
    а допустимые (например, 'у') обрабатываются корректно."""
    # 'у' ∈ RUSPHONE → rightfinger2
    res = count_finger_load_rusphone("[у]")
    expected = zero_counts.copy()
    expected[idx("rightfinger2")] = 1
    assert res == expected


def test_mixed_valid_text(finger_order, idx, zero_counts):
    """Проверяет смешанный ввод: заглавная буква и доп-символ.
    'У' → 'у' в rightfinger2 + Shift,
    '@' → в leftfinger4 + Shift.
    Итого: rightfinger2=1, leftfinger4=1, leftfinger5=2 (два Shift'а)."""
    res = count_finger_load_rusphone("У@")
    expected = zero_counts.copy()
    expected[idx("rightfinger2")] = 1  # за "у"
    expected[idx("leftfinger4")] = 1   # за "@"
    expected[idx("leftfinger5")] = 2   # два Shift'а
    assert res == expected
