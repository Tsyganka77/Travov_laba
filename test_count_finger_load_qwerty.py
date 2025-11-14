import pytest
from function import count_finger_load_qwerty, QWERTY_FINGER_COUNT, \
    KEYBOARD_FINGER_QWERTY, KEYBOARD_FINGER_QWERTY_DOP

# Фикстура для сброса счётчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_qwerty_finger_count():
    for key in QWERTY_FINGER_COUNT:
        QWERTY_FINGER_COUNT[key] = 0


# -------------------------------------------------
# Тесты
# -------------------------------------------------

def test_count_finger_load_qwerty_basic_lowercase():
    """Тест: строчные буквы увеличивают только соответствующий палец."""
    text = "ф"
    result = count_finger_load_qwerty(text)
    # 'ф' → leftfinger5
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_qwerty_uppercase():
    """Тест: заглавные буквы увеличивают палец + shift (leftfinger5)."""
    text = "Ф"
    result = count_finger_load_qwerty(text)
    # 'ф' → leftfinger5, заглавная → ещё +1 к leftfinger5
    # Итого: leftfinger5 = 2
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_qwerty_space():
    """Тест: пробел обрабатывается отдельно."""
    text = " "
    result = count_finger_load_qwerty(text)
    # ' ' → leftfinger1
    expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]  # leftfinger1 = 1
    assert result == expected


def test_count_finger_load_qwerty_dop_char():
    """Тест: символ из вспомогательной раскладки (например, '!') увеличивает палец и shift."""
    text = "!"
    result = count_finger_load_qwerty(text)
    # '!' → leftfinger5 (вспомогательная), flag_nado = 1 → ещё +1 к leftfinger5
    # Итого: leftfinger5 = 2
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_qwerty_empty():
    """Тест: пустой текст — все счётчики 0."""
    text = ""
    result = count_finger_load_qwerty(text)
    expected = [0] * 10
    assert result == expected
