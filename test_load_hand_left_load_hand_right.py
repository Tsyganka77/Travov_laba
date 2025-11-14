import pytest
from function import load_hand_left, load_hand_right


# -------------------------------------------------
# Тесты для load_hand_left
# -------------------------------------------------

def test_load_hand_left_all_left():
    """Тест: вся нагрузка на левой руке — 100%."""
    data = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]
    result = load_hand_left(data)
    assert result == 100


def test_load_hand_left_all_right():
    """Тест: вся нагрузка на правой руке — 0%."""
    data = [0, 0, 0, 0, 0, 10, 10, 10, 10, 10]
    result = load_hand_left(data)
    assert result == 0


def test_load_hand_left_mixed():
    """Тест: нагрузка распределена — 50/50."""
    data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result = load_hand_left(data)
    assert result == 50  # 5 / 10 * 100 = 50


def test_load_hand_left_mixed_uneven():
    """Тест: нагрузка распределена неравномерно — 25/75."""
    data = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3]  # левая = 5, правая = 15, всего = 20
    result = load_hand_left(data)
    assert result == 25  # 5 / 20 * 100 = 25


def test_load_hand_left_zero_total():
    """Тест: общая нагрузка = 0 — возвращается 0."""
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = load_hand_left(data)
    assert result == 0


def test_load_hand_left_rounding():
    """Тест: округление вниз (int)."""
    data = [2, 0, 0, 0, 0, 3, 0, 0, 0, 0]  # левая = 2, правая = 3, всего = 5
    result = load_hand_left(data)
    assert result == 40  # int(2/5 * 100) = int(40.0) = 40


# -------------------------------------------------
# Тесты для load_hand_right
# -------------------------------------------------

def test_load_hand_right_all_right():
    """Тест: вся нагрузка на правой руке — 100%."""
    data = [0, 0, 0, 0, 0, 10, 10, 10, 10, 10]
    result = load_hand_right(data)
    assert result == 100


def test_load_hand_right_all_left():
    """Тест: вся нагрузка на левой руке — 0%."""
    data = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]
    result = load_hand_right(data)
    assert result == 0


def test_load_hand_right_mixed():
    """Тест: нагрузка распределена — 50/50."""
    data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    result = load_hand_right(data)
    assert result == 50  # 5 / 10 * 100 = 50


def test_load_hand_right_mixed_uneven():
    """Тест: нагрузка распределена неравномерно — 75/25."""
    data = [3, 3, 3, 3, 3, 1, 1, 1, 1, 1]  # левая = 15, правая = 5, всего = 20
    result = load_hand_right(data)
    assert result == 25  # 5 / 20 * 100 = 25


def test_load_hand_right_zero_total():
    """Тест: общая нагрузка = 0 — возвращается 0."""
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = load_hand_right(data)
    assert result == 0


def test_load_hand_right_rounding():
    """Тест: округление вниз (int)."""
    data = [3, 0, 0, 0, 0, 2, 0, 0, 0, 0]  # левая = 3, правая = 2, всего = 5
    result = load_hand_right(data)
    assert result == 40  # int(2/5 * 100) = int(40.0) = 40


# -------------------------------------------------
# Граничные и специальные случаи
# -------------------------------------------------

def test_load_hand_left_single_element():
    """Тест: список из 10 элементов, один из левой руки."""
    data = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = load_hand_left(data)
    assert result == 100


def test_load_hand_right_single_element():
    """Тест: список из 10 элементов, один из правой руки."""
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 7]
    result = load_hand_right(data)
    assert result == 100


def test_load_hand_right_small_list():
    """Тест: короткий список — правая рука = 0."""
    result = load_hand_right([1, 2, 3])
    assert result == 0
