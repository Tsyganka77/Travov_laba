import pytest
from function import find_finger, KEYBOARD_FINGER_QWERTY, KEYBOARD_FINGER_QWERTY_DOP, \
    KEYBOARD_FINGER_VYZOV, KEYBOARD_FINGER_VYZOV_DOP, \
    KEYBOARD_FINGER_DICTOR, KEYBOARD_FINGER_DICTOR_DOP


# -------------------------------------------------
# Фикстуры для раскладок
# -------------------------------------------------

@pytest.fixture
def qwerty_layout():
    return KEYBOARD_FINGER_QWERTY

@pytest.fixture
def qwerty_dop_layout():
    return KEYBOARD_FINGER_QWERTY_DOP

@pytest.fixture
def vyzov_layout():
    return KEYBOARD_FINGER_VYZOV

@pytest.fixture
def vyzov_dop_layout():
    return KEYBOARD_FINGER_VYZOV_DOP

@pytest.fixture
def dictor_layout():
    return KEYBOARD_FINGER_DICTOR

@pytest.fixture
def dictor_dop_layout():
    return KEYBOARD_FINGER_DICTOR_DOP


# -------------------------------------------------
# Тесты для QWERTY
# -------------------------------------------------

def test_find_finger_qwerty_main(qwerty_layout):
    """Символ из основной раскладки QWERTY"""
    finger, flag = find_finger('ф', qwerty_layout)
    assert finger == 'leftfinger5'
    assert flag == 0

def test_find_finger_qwerty_dop(qwerty_layout):
    """Символ из дополнительной раскладки QWERTY"""
    finger, flag = find_finger('!', qwerty_layout)
    assert finger == 'leftfinger5'
    assert flag == 1

def test_find_finger_qwerty_invalid(qwerty_layout):
    """Невалидный символ в QWERTY"""
    result, flag = find_finger('木', qwerty_layout)
    assert result == "Invalid character: 木"
    assert flag == 0


# -------------------------------------------------
# Тесты для VYZOV
# -------------------------------------------------

def test_find_finger_vyzov_main(vyzov_layout):
    """Символ из основной раскладки VYZOV"""
    finger, flag = find_finger('ч', vyzov_layout)
    assert finger == 'leftfinger5'
    assert flag == 0

def test_find_finger_vyzov_dop(vyzov_layout):
    """Символ из дополнительной раскладки VYZOV"""
    finger, flag = find_finger('%', vyzov_layout)
    assert finger == 'leftfinger5'
    assert flag == 1

def test_find_finger_vyzov_invalid(vyzov_layout):
    """Невалидный символ в VYZOV"""
    result, flag = find_finger('木', vyzov_layout)
    assert result == "Invalid character: 木"
    assert flag == 0


# -------------------------------------------------
# Тесты для DICTOR
# -------------------------------------------------

def test_find_finger_dictor_main(dictor_layout):
    """Символ из основной раскладки DICTOR"""
    finger, flag = find_finger('у', dictor_layout)
    assert finger == 'leftfinger5'
    assert flag == 0

def test_find_finger_dictor_dop(dictor_layout):
    """Символ из дополнительной раскладки DICTOR"""
    finger, flag = find_finger('#', dictor_layout)
    assert finger == 'rightfinger5'
    assert flag == 1

def test_find_finger_dictor_invalid(dictor_layout):
    """Невалидный символ в DICTOR"""
    result, flag = find_finger('木', dictor_layout)
    assert result == "Invalid character: 木"
    assert flag == 0


# -------------------------------------------------
# Тесты: строка, список, кортеж в раскладке
# -------------------------------------------------

def test_find_finger_string_char():
    layout = {'leftfinger5': 'abc'}
    finger, flag = find_finger('b', layout)
    assert finger == 'leftfinger5'
    assert flag == 0

def test_find_finger_tuple_char():
    layout = {'leftfinger5': ('x', 'y')}
    finger, flag = find_finger('y', layout)
    assert finger == 'leftfinger5'
    assert flag == 0

def test_find_finger_list_char():
    layout = {'leftfinger5': ['m', 'n']}
    finger, flag = find_finger('m', layout)
    assert finger == 'leftfinger5'
    assert flag == 0


# -------------------------------------------------
# Тесты: пробел и другие специальные символы
# -------------------------------------------------

def test_find_finger_space(qwerty_layout, vyzov_layout, dictor_layout):
    """Пробел в QWERTY"""
    finger, flag = find_finger(' ', qwerty_layout)
    assert finger == 'leftfinger1'
    assert flag == 0

    """Пробел в VYZOV"""
    finger, flag = find_finger(' ', vyzov_layout)
    assert finger == 'leftfinger1'
    assert flag == 0

    """Пробел в DICTOR"""
    finger, flag = find_finger(' ', dictor_layout)
    assert finger == 'leftfinger1'
    assert flag == 0
