import pytest
from function import count_finger_load_dictor, DICTOR_FINGER_COUNT, \
    KEYBOARD_FINGER_DICTOR, KEYBOARD_FINGER_DICTOR_DOP

# -------------------------------------------------
# Фикстуры
# -------------------------------------------------

@pytest.fixture
def dictor_layout():
    return KEYBOARD_FINGER_DICTOR

@pytest.fixture
def dictor_dop_layout():
    return KEYBOARD_FINGER_DICTOR_DOP


# -------------------------------------------------
# Тесты
# -------------------------------------------------

def test_count_finger_load_dictor_basic_lowercase(dictor_layout):
    """Тест: строчные буквы увеличивают только соответствующий палец."""
    text = "у"
    result = count_finger_load_dictor(text)
    # 'у' → leftfinger5
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_dictor_uppercase(dictor_layout):
    """Тест: заглавные буквы увеличивают палец + shift (leftfinger5)."""
    text = "У"
    result = count_finger_load_dictor(text)
    # 'у' → leftfinger5, заглавная → ещё +1 к leftfinger5
    # Итого: leftfinger5 = 2
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_dictor_space(dictor_layout):
    """Тест: пробел обрабатывается отдельно."""
    text = " "
    result = count_finger_load_dictor(text)
    # ' ' → leftfinger1
    expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]  # leftfinger1 = 1
    assert result == expected


def test_count_finger_load_dictor_dop_char(dictor_layout, dictor_dop_layout):
    """Тест: символ из вспомогательной раскладки (например, '#') увеличивает палец и shift."""
    text = "#"
    result = count_finger_load_dictor(text)
    # '#' → rightfinger5 (вспомогательная), flag_nado = 1 → +1 к leftfinger5
    # Итого: rightfinger5 = 1, leftfinger5 = 1
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert result == expected


def test_count_finger_load_dictor_invalid_char(dictor_layout):
    """Тест: невалидные символы игнорируются."""
    text = "у木#"
    result = count_finger_load_dictor(text)
    # 'у' → leftfinger5 = 1
    # '#' → rightfinger5 = 1 (вспомогательная), +1 shift → leftfinger5 = 2
    # '木' → игнорируется
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert result == expected


def test_count_finger_load_dictor_empty(dictor_layout):
    """Тест: пустой текст — все счётчики 0."""
    text = ""
    result = count_finger_load_dictor(text)
    expected = [0] * 10
    assert result == expected
