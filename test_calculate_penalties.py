import pytest
from keyboard import (
    KEYBOARD_QWERTY, KEYBOARD_VYZOV, KEYBOARD_ANT,
    KEY_GRID_QWERTY, KEY_GRID_VYZOV, KEY_GRID_ANT,
    KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE,
    KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS,
    KEYBOARD_DICTOR, KEY_GRID_DICTOR,
    KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW,
)
from function import calculate_penalties

# Собираем все пары (layout, grid) для параметризации
LAYOUT_GRID_PAIRS = [
    ("qwerty", KEYBOARD_QWERTY, KEY_GRID_QWERTY),
    ("vyzov", KEYBOARD_VYZOV, KEY_GRID_VYZOV),
    ("dictor", KEYBOARD_DICTOR, KEY_GRID_DICTOR),
    ("ant", KEYBOARD_ANT, KEY_GRID_ANT),
    ("rusphone", KEYBOARD_RUSPHONE, KEY_GRID_RUSPHONE),
    ("skoropis", KEYBOARD_SKOROPIS, KEY_GRID_SKOROPIS),
    ("zubachew", KEYBOARD_ZUBACHEW, KEY_GRID_ZUBACHEW),
]


@pytest.mark.parametrize("name, layout, grid", LAYOUT_GRID_PAIRS)
def test_empty_text(name, layout, grid):
    """Пустой текст → 0 штрафов."""
    assert calculate_penalties("", layout, grid) == 0


@pytest.mark.parametrize("name, layout, grid", LAYOUT_GRID_PAIRS)
def test_only_spaces(name, layout, grid):
    """Только пробелы → 0 штрафов."""
    assert calculate_penalties("     ", layout, grid) == 0


def test_qwerty_home_row_no_penalty():
    """Символы домашнего ряда QWERTY (row=1) → 0 штрафов."""
    # Согласно KEY_GRID_QWERTY: "ф", "ы", "в", "а", "о", "л", "д", "ж" → row=1
    home_chars = "фывалдж"
    assert calculate_penalties(home_chars, KEYBOARD_QWERTY, KEY_GRID_QWERTY) == 0


def test_qwerty_top_row_penalty_1():
    """Верхний ряд QWERTY (row=0) → +1 за символ."""
    # "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ"
    top_chars = "йцукенгшщзхъ"
    assert calculate_penalties(top_chars, KEYBOARD_QWERTY, KEY_GRID_QWERTY) == len(top_chars) * 1


def test_qwerty_bottom_row_penalty_1():
    """Нижний ряд QWERTY (row=2) → +1 за символ."""
    # "я", "ч", "с", "м", "и", "т", "ь", "б", "ю"
    bottom_chars = "ячсмитьбю"
    assert calculate_penalties(bottom_chars, KEYBOARD_QWERTY, KEY_GRID_QWERTY) == len(bottom_chars) * 1


def test_qwerty_extended_keys_penalty_2():
    """Клавиши за пределами основной зоны (row=0, но col=12,13) — всё равно row=0 → +1.
    Но если бы был row=3 — было бы +2. В QWERTY максимум row=2.
    Поэтому создадим искусственную сетку для проверки +2."""
    pass  # Покроем в отдельном тесте


def test_case_insensitive_fallback():
    """Если символа нет как есть — пробуем .lower()."""
    # В QWERTY есть "Ф" и "ф"
    assert calculate_penalties("Ф", KEYBOARD_QWERTY, KEY_GRID_QWERTY) == 0  # домашний ряд
    # Но представим раскладку, где только строчные:
    fake_grid = {"а": (0, 1)}  # домашний ряд
    fake_layout = {"leftfinger2": ("а",)}
    # Передаём "А" → должен найти через .lower()
    assert calculate_penalties("А", fake_layout, fake_grid) == 0


def test_mixed_penalties():
    """Смешанный текст: домашний, верхний, неизвестный."""
    # "ф" (0) + "й" (1) + "日" (2) = 0 + 1 + 2 = 3
    assert calculate_penalties("фй日", KEYBOARD_QWERTY, KEY_GRID_QWERTY) == 3


def test_spaces_ignored():
    """Пробелы не учитываются."""
    assert calculate_penalties("ф й 日", KEYBOARD_QWERTY, KEY_GRID_QWERTY) == 3


def test_artificial_grid_with_row_3():
    """Проверка +2 штрафа для row=3 (в реальных раскладках такого нет, но логика должна работать)."""
    fake_grid = {
        "a": (0, 1),  # home → 0
        "b": (0, 0),  # dy=1 → +1
        "c": (0, 2),  # dy=1 → +1
        "d": (0, 3),  # dy=2 → +2
        "e": (0, -1),  # dy=2 → +2
    }
    fake_layout = {f"leftfinger{i}": () for i in range(1, 6)}
    fake_layout.update({f"rightfinger{i}": () for i in range(1, 6)})
    # Заполним хотя бы один палец, чтобы layout был валидным (хотя он не используется в penalties!)
    fake_layout["leftfinger2"] = ("a", "b", "c", "d", "e")

    text = "abcde"
    # a:0, b:1, c:1, d:2, e:2 → total = 0+1+1+2+2 = 6
    assert calculate_penalties(text, fake_layout, fake_grid) == 6


@pytest.mark.parametrize("name, layout, grid", LAYOUT_GRID_PAIRS)
def test_all_known_chars_produce_non_negative_penalties(name, layout, grid):
    """Для каждой раскладки: все символы из layout дают штраф 0, 1 или 2."""
    all_chars = set()
    for chars in layout.values():
        all_chars.update(chars)

    if not all_chars:
        pytest.skip(f"Раскладка {name} пустая")

    # Преобразуем в строку (игнорируем не-строки, хотя у вас всё str)
    text = "".join(str(c) for c in list(all_chars)[:30])  # ограничим для скорости
    penalty = calculate_penalties(text, layout, grid)
    assert penalty >= 0
    # Максимум 2 на символ
    assert penalty <= 2 * len(text)


def test_vyzov_home_row_no_penalty():
    """Проверка домашнего ряда для Vyzov через явные символы."""
    # Согласно коду: HOME_KEYS_VYZOV = {"ч", "и", "е", "а", "н", "т", "с", "б", ...}
    # В KEY_GRID_VYZOV они имеют row=1
    home_chars = "чиенасб"
    assert calculate_penalties(home_chars, KEYBOARD_VYZOV, KEY_GRID_VYZOV) == 0
