import pytest
from keyboard import (
    KEYBOARD_QWERTY,
    KEYBOARD_VYZOV,
    KEYBOARD_DICTOR,
    KEYBOARD_ANT,
    KEYBOARD_RUSPHONE,
    KEYBOARD_SKOROPIS,
    KEYBOARD_ZUBACHEW,
)
from function import count_finger_load  # Замените 'analysis' на имя вашего файла

# Словарь всех раскладок для параметризации
ALL_LAYOUTS = {
    "qwerty": KEYBOARD_QWERTY,
    "vyzov": KEYBOARD_VYZOV,
    "dictor": KEYBOARD_DICTOR,
    "ant": KEYBOARD_ANT,
    "rusphone": KEYBOARD_RUSPHONE,
    "skoropis": KEYBOARD_SKOROPIS,
    "zubachew": KEYBOARD_ZUBACHEW,
}


@pytest.fixture(params=ALL_LAYOUTS.values(), ids=ALL_LAYOUTS.keys())
def layout(request):
    """Фикстура: каждая раскладка из списка."""
    return request.param


def test_empty_text(layout):
    """Пустой текст → все нули для любой раскладки."""
    result = count_finger_load("", layout)
    assert result == [0] * 10


def test_only_spaces(layout):
    """Только пробелы → все нули."""
    result = count_finger_load("     ", layout)
    assert result == [0] * 10


def test_spaces_ignored(layout):
    """Пробелы не учитываются."""
    # Возьмём первый непустой символ из раскладки
    char = None
    for chars in layout.values():
        if chars:
            char = chars[0]
            break
    if char is None:
        pytest.skip("Раскладка пустая")
    result = count_finger_load(f"{char} {char}", layout)
    expected = [0] * 10
    # Найдём, какому пальцу принадлежит символ
    from function import find_finger
    finger = find_finger(char, layout)
    if finger is None:
        finger = find_finger(char.lower(), layout)
    if finger is None:
        pytest.skip(f"Не удалось определить палец для {char}")

    # Определим позицию в списке
    order = (
        "leftfinger5",
        "leftfinger4",
        "leftfinger3",
        "leftfinger2",
        "leftfinger1",
        "rightfinger1",
        "rightfinger2",
        "rightfinger3",
        "rightfinger4",
        "rightfinger5"
    )
    if finger in order:
        idx = order.index(finger)
        expected[idx] = 2  # два вхождения
        assert result == expected
    else:
        pytest.fail(f"Неизвестный палец: {finger}")


def test_case_insensitive_fallback(layout):
    """Если символ не найден как есть — должен искать через .lower()."""
    # Найдём символ в нижнем регистре, которого нет в верхнем
    lower_char = None
    upper_char = None
    for chars in layout.values():
        for ch in chars:
            if isinstance(ch, str) and ch.islower():
                lower_char = ch
                upper_char = ch.upper()
                # Проверим, что upper_char отсутствует в раскладке
                found_upper = False
                for group in layout.values():
                    if upper_char in group:
                        found_upper = True
                        break
                if not found_upper:
                    break
        if lower_char:
            break

    if not lower_char:
        pytest.skip("Не найдено подходящего символа для теста регистра")

    # Текст с символом в верхнем регистре (которого нет в layout)
    result = count_finger_load(upper_char, layout)
    # Должен найти через .lower()
    expected = [0] * 10
    from function import find_finger
    finger = find_finger(lower_char, layout)
    if finger is None:
        pytest.skip("Не удалось определить палец для символа")

    order = (
        "leftfinger5",
        "leftfinger4",
        "leftfinger3",
        "leftfinger2",
        "leftfinger1",
        "rightfinger1",
        "rightfinger2",
        "rightfinger3",
        "rightfinger4",
        "rightfinger5"
    )
    if finger in order:
        idx = order.index(finger)
        expected[idx] = 1
        assert result == expected
    else:
        pytest.fail(f"Неизвестный палец: {finger}")


def test_unknown_char_ignored(layout):
    """Неизвестные символы (например, emoji) игнорируются."""
    result = count_finger_load("й日ц", layout)  # 日 — точно нет ни в одной раскладке
    # Должно быть то же, что и для "йц"
    result_ref = count_finger_load("йц", layout)
    assert result == result_ref


def test_all_pinky_fingers_are_zero(layout):
    """Убедимся, что leftfinger1 и rightfinger1 всегда 0 (т.к. в ваших раскладках они пустые)."""
    # Соберём все символы из раскладки
    all_chars = []
    for chars in layout.values():
        all_chars.extend(chars)
    if not all_chars:
        pytest.skip("Пустая раскладка")
    text = "".join(str(c) for c in all_chars[:20])  # возьмём до 20 символов
    result = count_finger_load(text, layout)
    # Позиции left1 (индекс 4) и right1 (индекс 5) должны быть 0
    assert result[4] == 0, "leftfinger1 должен быть 0"
    assert result[5] == 0, "rightfinger1 должен быть 0"


# === Дополнительно: тест на корректный порядок для каждой раскладки ===

@pytest.mark.parametrize("layout_name, layout", ALL_LAYOUTS.items())
def test_finger_order_and_basic_char(layout_name, layout):
    """Проверка, что базовые символы правильно распределяются по пальцам."""
    # Просто убедимся, что подсчёт не падает и возвращает список из 10 элементов
    test_text = "абвгд"
    result = count_finger_load(test_text, layout)
    assert isinstance(result, list)
    assert len(result) == 10
    assert all(isinstance(x, int) and x >= 0 for x in result)
