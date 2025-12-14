import pytest
import time
from function import (
    count_finger_load,
    calculate_penalties,
    count_convenient_rolls,
    count_finger_load_ant,
    count_finger_load_rusphone,
    count_finger_load_skoropis,
    count_finger_load_zubachew,
    calculate_penalties_ant,
    calculate_penalties_rusphone,
    calculate_penalties_skoropis,
    calculate_penalties_zubachew,
    count_convenient_rolls_ant,
    count_convenient_rolls_rusphone,
    count_convenient_rolls_skoropis,
    count_convenient_rolls_zubachew,
    find_finger,
    filter_single_char_words,
)
from keyboard import (
    KEYBOARD_QWERTY, KEYBOARD_ANT, KEYBOARD_RUSPHONE, KEYBOARD_SKOROPIS,
    KEYBOARD_ZUBACHEW, KEYBOARD_VYZOV, KEYBOARD_DICTOR,
    KEY_GRID_QWERTY, KEY_GRID_ANT, KEY_GRID_RUSPHONE, KEY_GRID_SKOROPIS,
    KEY_GRID_ZUBACHEW, KEY_GRID_VYZOV, KEY_GRID_DICTOR,
    HOME_KEYS_QWERTY, HOME_KEYS_ANT, HOME_KEYS_RUSPHONE, HOME_KEYS_SKOROPIS,
    HOME_KEYS_ZUBACHEW, HOME_KEYS_VYZOV, HOME_KEYS_DICTOR,
)


# Все раскладки для параметризованных тестов
LAYOUTS = [
    (KEYBOARD_QWERTY, KEY_GRID_QWERTY, HOME_KEYS_QWERTY, "QWERTY"),
    (KEYBOARD_VYZOV, KEY_GRID_VYZOV, HOME_KEYS_VYZOV, "VYZOV"),
    (KEYBOARD_DICTOR, KEY_GRID_DICTOR, HOME_KEYS_DICTOR, "DICTOR"),
    (KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT, "ANT"),
    (KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE, HOME_KEYS_RUSPHONE, "RUSPHONE"),
    (KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS, HOME_KEYS_SKOROPIS, "SKOROPIS"),
    (KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW, HOME_KEYS_ZUBACHEW, "ZUBACHEW"),
]


# === Базовые тесты ===

@pytest.mark.parametrize("layout,grid,home_keys,name", LAYOUTS)
def test_count_finger_load_ignores_spaces(layout, grid, home_keys, name):
    """Пробелы не учитываются в нагрузке."""
    load1 = count_finger_load("a", layout)
    load2 = count_finger_load(" a ", layout)
    assert load1 == load2


@pytest.mark.parametrize("layout,grid,home_keys,name", LAYOUTS)
def test_count_finger_load_case_sensitivity_handled(layout, grid, home_keys, name):
    """Функция должна находить и строчные, и заглавные буквы (они есть в раскладке)."""
    char_lower = None
    for chars in layout.values():
        for ch in (chars if isinstance(chars, (list, tuple)) else [chars]):
            if ch.isalpha() and ch.islower():
                char_lower = ch
                break
        if char_lower:
            break
    if not char_lower:
        pytest.skip(f"[{name}] Нет букв")

    load_lower = count_finger_load(char_lower, layout)
    load_upper = count_finger_load(char_lower.upper(), layout)
    assert load_lower == load_upper


def test_count_finger_load_output_order():
    """Проверка порядка: [l5, l4, l3, l2, l1, r1, r2, r3, r4, r5]"""
    load = count_finger_load("фн", KEYBOARD_ANT)
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert load == expected


@pytest.mark.parametrize("layout,grid,home_keys,name", LAYOUTS)
def test_calculate_penalties_ignores_spaces(layout, grid, home_keys, name):
    """Пробелы не учитываются в штрафах."""
    p1 = calculate_penalties("a", layout, grid, home_keys)
    p2 = calculate_penalties(" a ", layout, grid, home_keys)
    assert p1 == p2


@pytest.mark.parametrize("layout,grid,home_keys,name", LAYOUTS)
def test_calculate_penalties_home_row_zero_penalty(layout, grid, home_keys, name):
    """Символы из home-ряда дают 0 штрафа."""
    for ch in home_keys:
        if ch in grid:
            penalty = calculate_penalties(ch, layout, grid, home_keys)
            assert penalty == 0, f"[{name}] Символ '{ch}' из home-ряда дал штраф {penalty}"
            return
    pytest.skip(f"[{name}] Нет символов из home-ряда в grid")


def test_calculate_penalties_unknown_char():
    """Неизвестный символ -> штраф 2."""
    p = calculate_penalties("€", KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT)
    assert p == 2


def test_count_convenient_rolls_example():
    """Проверка удобного рулона на примере QWERTY: 'йц' -> l5->l4 -> [0,1] -> удобно."""
    rolls = count_convenient_rolls("йц", KEYBOARD_QWERTY)
    assert rolls == 1
    rolls = count_convenient_rolls("цй", KEYBOARD_QWERTY)
    assert rolls == 0
    rolls = count_convenient_rolls("йн", KEYBOARD_QWERTY)
    assert rolls == 0


# === Тесты интерфейсных функций ===

def test_ant_interface_functions():
    text = "ФЫАВОЛДЖ!"
    assert count_finger_load_ant(text) == count_finger_load(text, KEYBOARD_ANT)
    assert calculate_penalties_ant(text) == calculate_penalties(text, KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT)
    assert count_convenient_rolls_ant(text) == count_convenient_rolls(text, KEYBOARD_ANT)


def test_rusphone_interface_functions():
    text = "ЕРДЦУЙКЛ@"
    assert count_finger_load_rusphone(text) == count_finger_load(text, KEYBOARD_RUSPHONE)
    assert calculate_penalties_rusphone(text) == calculate_penalties(text, KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE, HOME_KEYS_RUSPHONE)
    assert count_convenient_rolls_rusphone(text) == count_convenient_rolls(text, KEYBOARD_RUSPHONE)


def test_skoropis_interface_functions():
    text = "ЬЯИЕКПШР#"
    assert count_finger_load_skoropis(text) == count_finger_load(text, KEYBOARD_SKOROPIS)
    assert calculate_penalties_skoropis(text) == calculate_penalties(text, KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS, HOME_KEYS_SKOROPIS)
    assert count_convenient_rolls_skoropis(text) == count_convenient_rolls(text, KEYBOARD_SKOROPIS)


def test_zubachew_identical_to_ant():
    """ZUBACHEW — копия ANT, результаты должны совпадать."""
    test_text = "Привет, ANT и Zubachew! 123"
    assert count_finger_load_zubachew(test_text) == count_finger_load_ant(test_text)
    assert calculate_penalties_zubachew(test_text) == calculate_penalties_ant(test_text)
    assert count_convenient_rolls_zubachew(test_text) == count_convenient_rolls_ant(test_text)


# === Дополнительные тесты (крайние случаи и надёжность) ===

def test_count_finger_load_empty_string():
    """Пустая строка должна возвращать список из 10 нулей."""
    assert count_finger_load("", KEYBOARD_ANT) == [0] * 10


def test_count_finger_load_only_invalid_chars():
    """Строка из недопустимых символов должна давать нулевую нагрузку."""
    assert count_finger_load("€§±", KEYBOARD_ANT) == [0] * 10


def test_calculate_penalties_only_invalid_chars():
    """Недопустимые символы дают по +2 за каждый."""
    assert calculate_penalties("€§", KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT) == 4


def test_calculate_penalties_mixed_valid_invalid():
    """Смешанный текст: допустимые + недопустимые символы."""
    assert calculate_penalties("а€", KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT) == 2


def test_count_convenient_rolls_empty_text():
    """Пустой текст → 0 рулонов."""
    assert count_convenient_rolls("", KEYBOARD_ANT) == 0


def test_count_convenient_rolls_single_char():
    """Одна буква → не рулон (нужно минимум 2)."""
    assert count_convenient_rolls("а", KEYBOARD_ANT) == 0


def test_count_convenient_rolls_word_with_non_letter():
    """Слово с цифрами/пунктуацией — пропускается (re.findall ищет только буквы)."""
    assert count_convenient_rolls("a1b", KEYBOARD_QWERTY) == 0


def test_count_convenient_rolls_mixed_case_word():
    """Слово в разном регистре должно обрабатываться корректно."""
    assert count_convenient_rolls("Йц", KEYBOARD_QWERTY) == 1


def test_ant_duplicate_yery():
    """В ANT "ы" есть и в leftfinger4, и в leftfinger2.
    find_finger вернёт первый найденный (leftfinger4)."""
    assert find_finger("ы", KEYBOARD_ANT) == "leftfinger4"


# === Проверка согласованности данных ===

def test_all_grid_keys_present_in_keyboard():
    """Убедимся, что каждый символ в KEY_GRID_* присутствует в KEYBOARD_*.
    Иначе calculate_penalties найдёт символ, но find_finger не сможет определить палец."""
    ALL_LAYOUTS_GRIDS = [
        (KEYBOARD_QWERTY, KEY_GRID_QWERTY, "QWERTY"),
        (KEYBOARD_VYZOV, KEY_GRID_VYZOV, "VYZOV"),
        (KEYBOARD_DICTOR, KEY_GRID_DICTOR, "DICTOR"),
        (KEYBOARD_ANT, KEY_GRID_ANT, "ANT"),
        (KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE, "RUSPHONE"),
        (KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS, "SKOROPIS"),
        (KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW, "ZUBACHEW"),
    ]
    for layout, grid, name in ALL_LAYOUTS_GRIDS:
        layout_chars = set()
        for chars in layout.values():
            layout_chars.update(chars if isinstance(chars, (list, tuple)) else [chars])

        for ch in grid.keys():
            assert ch in layout_chars, f"[{name}] Символ '{ch}' из KEY_GRID отсутствует в KEYBOARD"


def test_home_keys_subset_of_grid_keys():
    """Все символы из HOME_KEYS_* должны быть в KEY_GRID_*."""
    ALL_HOME_GRIDS = [
        (HOME_KEYS_QWERTY, KEY_GRID_QWERTY, "QWERTY"),
        (HOME_KEYS_VYZOV, KEY_GRID_VYZOV, "VYZOV"),
        (HOME_KEYS_DICTOR, KEY_GRID_DICTOR, "DICTOR"),
        (HOME_KEYS_ANT, KEY_GRID_ANT, "ANT"),
        (HOME_KEYS_RUSPHONE, KEY_GRID_RUSPHONE, "RUSPHONE"),
        (HOME_KEYS_SKOROPIS, KEY_GRID_SKOROPIS, "SKOROPIS"),
        (HOME_KEYS_ZUBACHEW, KEY_GRID_ZUBACHEW, "ZUBACHEW"),
    ]
    for home_keys, grid, name in ALL_HOME_GRIDS:
        for ch in home_keys:
            assert ch in grid, f"[{name}] Символ '{ch}' из HOME_KEYS отсутствует в KEY_GRID"


# === Производительность и утилиты ===

def test_performance_large_text():
    """Проверка, что функции не зависают на большом тексте."""
    large_text = "Привет! Это тест для проверки производительности. " * 1000

    start = time.time()
    _ = count_finger_load(large_text, KEYBOARD_ANT)
    _ = calculate_penalties(large_text, KEYBOARD_ANT, KEY_GRID_ANT, HOME_KEYS_ANT)
    _ = count_convenient_rolls(large_text, KEYBOARD_ANT)
    elapsed = time.time() - start

    assert elapsed < 2.0, "Обработка 50k символов заняла слишком много времени"


def test_filter_single_char_words_integration():
    """Убедимся, что filter_single_char_words корректно удаляет однобуквенные слова."""
    text = "Я иду в аптеку за лекарством, и это важно."
    filtered = filter_single_char_words(text)
    words = filtered.split()
    assert "Я" not in words
    assert "и" not in words
    assert "а" not in words
    assert "за" in words
    assert "это" in words
