

import pytest
from keyboard import KEYBOARD_QWERTY, KEYBOARD_VYZOV, KEYBOARD_ANT, KEYBOARD_DICTOR, KEYBOARD_RUSPHONE
from function import find_finger


class TestFindFinger:
    """Тесты для функции find_finger"""

    def test_qwerty_char_in_tuple_lowercase(self):
        """Символы в нижнем регистре, хранятся в кортеже"""
        assert find_finger("й", KEYBOARD_QWERTY) == "leftfinger5"
        assert find_finger("ц", KEYBOARD_QWERTY) == "leftfinger4"
        assert find_finger("у", KEYBOARD_QWERTY) == "leftfinger3"
        assert find_finger("к", KEYBOARD_QWERTY) == "leftfinger2"
        assert find_finger("н", KEYBOARD_QWERTY) == "rightfinger2"
        assert find_finger("ш", KEYBOARD_QWERTY) == "rightfinger3"
        assert find_finger("з", KEYBOARD_QWERTY) == "rightfinger5"

    def test_qwerty_char_in_tuple_uppercase(self):
        """Символы в верхнем регистре, хранятся в кортеже"""
        assert find_finger("Й", KEYBOARD_QWERTY) == "leftfinger5"
        assert find_finger("Ц", KEYBOARD_QWERTY) == "leftfinger4"
        assert find_finger("У", KEYBOARD_QWERTY) == "leftfinger3"
        assert find_finger("К", KEYBOARD_QWERTY) == "leftfinger2"
        assert find_finger("Н", KEYBOARD_QWERTY) == "rightfinger2"
        assert find_finger("Ш", KEYBOARD_QWERTY) == "rightfinger3"
        assert find_finger("З", KEYBOARD_QWERTY) == "rightfinger5"

    def test_qwerty_special_chars(self):
        """Спецсимволы и цифры"""
        assert find_finger("1", KEYBOARD_QWERTY) == "leftfinger5"
        assert find_finger("!", KEYBOARD_QWERTY) == "leftfinger5"
        assert find_finger("2", KEYBOARD_QWERTY) == "leftfinger4"
        assert find_finger("\"", KEYBOARD_QWERTY) == "leftfinger4"
        assert find_finger("0", KEYBOARD_QWERTY) == "rightfinger5"
        assert find_finger("=", KEYBOARD_QWERTY) == "rightfinger5"
        assert find_finger("[", KEYBOARD_QWERTY) == "rightfinger5"

    def test_vyzov_layout_mixed_content(self):
        """Проверка на другой раскладке (Vyzov), где есть и буквы, и латиница, и цифры"""
        assert find_finger("ч", KEYBOARD_VYZOV) == "leftfinger5"
        assert find_finger("Q", KEYBOARD_VYZOV) == "leftfinger5"
        assert find_finger("и", KEYBOARD_VYZOV) == "leftfinger4"
        assert find_finger("@", KEYBOARD_VYZOV) == "leftfinger4"
        assert find_finger("н", KEYBOARD_VYZOV) == "rightfinger2"
        assert find_finger("t", KEYBOARD_VYZOV) == "rightfinger2"
        assert find_finger("б", KEYBOARD_VYZOV) == "rightfinger5"
        assert find_finger(".", KEYBOARD_VYZOV) == "rightfinger5"

    def test_ant_layout_with_latin(self):
        """Проверка раскладки Ant с латинскими символами"""
        assert find_finger("ф", KEYBOARD_ANT) == "leftfinger5"
        assert find_finger("q", KEYBOARD_ANT) == "leftfinger5"
        assert find_finger("а", KEYBOARD_ANT) == "leftfinger3"
        assert find_finger("e", KEYBOARD_ANT) == "leftfinger3"
        assert find_finger("у", KEYBOARD_ANT) == "rightfinger2"
        assert find_finger("t", KEYBOARD_ANT) == "rightfinger2"
        assert find_finger("м", KEYBOARD_ANT) == "rightfinger5"
        assert find_finger("p", KEYBOARD_ANT) == "rightfinger5"

    def test_char_not_found_returns_none(self):
        """Символ отсутствует — возвращается None"""
        assert find_finger(" ", KEYBOARD_QWERTY) is None
        assert find_finger("\n", KEYBOARD_QWERTY) is None
        assert find_finger("a", KEYBOARD_QWERTY) is None  # латинская 'a', в QWERTY только кириллица и спецсимволы

    def test_empty_finger_ignored(self):
        """Пустой leftfinger1 не вызывает ошибок"""
        # Убеждаемся, что итерация по пустому кортежу не ломается
        assert find_finger("ё", KEYBOARD_QWERTY) == "leftfinger5"  # должен найти, несмотря на пустой finger1

    def test_case_sensitivity_respected(self):
        """Функция не приводит к нижнему регистру автоматически — ищет как есть"""
        # В QWERTY есть и "ф", и "Ф" — оба находятся
        assert find_finger("ф", KEYBOARD_QWERTY) == "leftfinger5"
        assert find_finger("Ф", KEYBOARD_QWERTY) == "leftfinger5"
        # Но латинская 'f' отсутствует
        assert find_finger("f", KEYBOARD_QWERTY) is None

    def test_duplicate_char_in_multiple_fingers_returns_first(self):
        """Если символ по ошибке дублируется, возвращается первый найденный (порядок dict)"""
        # Создадим искусственную раскладку с дубликатом
        fake_layout = {
            "leftfinger5": ("а",),
            "leftfinger4": ("а", "б")
        }
        assert find_finger("а", fake_layout) == "leftfinger5"

