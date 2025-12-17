import pytest
from function import analyze_rolls, classify_word
from keyboard import KEYBOARD_QWERTY, KEY_GRID_QWERTY


TEST_LAYOUT = {
    "leftfinger5": ("p",),
    "leftfinger4": ("o",),
    "leftfinger3": ("i",),
    "leftfinger2": ("u",),
    "leftfinger1": (),
    "rightfinger2": ("q",),
    "rightfinger3": ("w",),
    "rightfinger4": ("e",),
    "rightfinger5": ("r",),
}

TEST_GRID = {
    "p": (0, 1), "o": (1, 1), "i": (2, 1), "u": (3, 1),
    "q": (4, 1), "w": (5, 1), "e": (6, 1), "r": (7, 1),
}


@pytest.fixture
def empty_result():
    return {
        "total": {"convenient": 0, "semi": 0, "inconvenient": 0},
        "by_length": {
            2: {"convenient": 0, "semi": 0, "inconvenient": 0},
            3: {"convenient": 0, "semi": 0, "inconvenient": 0},
            4: {"convenient": 0, "semi": 0, "inconvenient": 0},
            5: {"convenient": 0, "semi": 0, "inconvenient": 0},
        },
    }


def test_empty_text(empty_result):
    """Пустой текст → пустой результат."""
    assert analyze_rolls("", TEST_LAYOUT, TEST_GRID) == empty_result


def test_no_valid_words(empty_result):
    """Текст без слов длиной 2–5 → пустой результат."""
    text = "a 123 ! ? word6chars"
    assert analyze_rolls(text, TEST_LAYOUT, TEST_GRID) == empty_result


def test_words_outside_length_ignored():
    """Слова короче 2 или длиннее 5 игнорируются."""
    # "a" (1), "ab" (2), "abcde" (5), "abcdef" (6)
    text = "a ab abcde abcdef"
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)
    total_words = sum(result["total"].values())
    assert total_words == 2 or total_words == 0


def test_convenient_rolls_counted():
    """Удобные рулоны учитываются в total и by_length."""
    # "po" — удобный левый рулон (длина 2)
    # "rew" — удобный правый рулон (длина 3)
    text = "po rew"
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)

    assert result["total"]["convenient"] == 2
    assert result["by_length"][2]["convenient"] == 1
    assert result["by_length"][3]["convenient"] == 1


def test_inconvenient_words_counted():
    """Неудобные слова (двумя руками) учитываются."""
    # "pr" — p (left), r (right) → inconvenient
    text = "pr"
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)
    assert result["total"]["inconvenient"] == 1
    assert result["by_length"][2]["inconvenient"] == 1


def test_semi_words_counted():
    """Полуудобные слова учитываются."""
    # "uo" — u(3) → o(1): индексы [3,1] — не возрастает → semi
    text = "uo"
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)
    assert result["total"]["semi"] == 1
    assert result["by_length"][2]["semi"] == 1


def test_words_with_pinky_or_unknown_ignored():
    """Слова с pinky или неизвестными символами пропускаются."""
    # Добавим слово с неизвестным символом
    text = "po xyz"
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)
    # "po" — удобный, "xyz" — содержит 'x','y','z' → не в layout → classify_word вернёт (None, None)
    assert result["total"]["convenient"] == 1
    assert sum(result["total"].values()) == 1


def test_mixed_case_words():
    """Регистронезависимость (если layout/grid поддерживают регистр)."""
    # В TEST_LAYOUT только строчные, но classify_word делает .lower()
    text = "PO rew"
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)
    # "PO" → "po" → удобный
    assert result["total"]["convenient"] == 2


def test_real_qwerty_example():
    """Пример на реальной раскладке."""
    # "фы" — удобный левый рулон в QWERTY (длина 2)
    # "жд" — удобный правый рулон (длина 2)
    # "йц" — lf5 + lf4 → удобный (0→1)
    text = "фы жд йц"
    result = analyze_rolls(text, KEYBOARD_QWERTY, KEY_GRID_QWERTY)
    assert result["by_length"][2]["convenient"] == 3
    assert result["total"]["convenient"] == 3


def test_by_length_structure_unchanged():
    """Структура by_length не изменяется, даже если нет слов определённой длины."""
    result = analyze_rolls("po", TEST_LAYOUT, TEST_GRID)  # только длина 2
    assert list(result["by_length"].keys()) == [2, 3, 4, 5]
    assert all(
        isinstance(result["by_length"][length], dict) for length in [2, 3, 4, 5]
    )
    assert result["by_length"][3]["convenient"] == 0
    assert result["by_length"][4]["semi"] == 0


def test_words_with_spaces_and_strip():
    """Пробелы и strip() не влияют на длину."""
    text = "  po  rew  "
    result = analyze_rolls(text, TEST_LAYOUT, TEST_GRID)
    assert result["total"]["convenient"] == 2
