import pytest
from function import count_finger_load_vyzov, VYZOV_FINGER_COUNT, \
    KEYBOARD_FINGER_VYZOV, KEYBOARD_FINGER_VYZOV_DOP

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
def empty_vyzov_finger_count():
    return {k: 0 for k in VYZOV_FINGER_COUNT}


# -------------------------------------------------
# Тесты
# -------------------------------------------------

def test_count_finger_load_vyzov_basic_lowercase(vyzov_layout):
    """Тест: строчные буквы увеличивают только соответствующий палец."""
    text = "ч"
    result = count_finger_load_vyzov(text)
    # 'ч' → leftfinger5
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_vyzov_uppercase(vyzov_layout):
    """Тест: заглавные буквы увеличивают палец + shift (leftfinger5)."""
    text = "Ч"
    result = count_finger_load_vyzov(text)
    # 'ч' → leftfinger5, заглавная → ещё +1 к leftfinger5
    # Итого: leftfinger5 = 2
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_vyzov_space(vyzov_layout):
    """Тест: пробел обрабатывается отдельно."""
    text = " "
    result = count_finger_load_vyzov(text)
    # ' ' → leftfinger1
    expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]  # leftfinger1 = 1
    assert result == expected


def test_count_finger_load_vyzov_dop_char(vyzov_layout, vyzov_dop_layout):
    """Тест: символ из вспомогательной раскладки (например, '%') увеличивает палец и shift."""
    text = "%"
    result = count_finger_load_vyzov(text)
    # '%' → leftfinger5 (вспомогательная), flag_nado = 1 → ещё +1 к leftfinger5
    # Итого: leftfinger5 = 2
    expected = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert result == expected


def test_count_finger_load_vyzov_empty(vyzov_layout):
    """Тест: пустой текст — все счётчики 0."""
    text = ""
    result = count_finger_load_vyzov(text)
    expected = [0] * 10
    assert result == expected
