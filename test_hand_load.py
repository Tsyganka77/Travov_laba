import pytest
from function import load_hand_left, load_hand_right  


class TestHandLoad:

    def test_balanced_load(self):
        """Ровно 50/50 — например, по 10 нажатий на каждую руку."""
        load_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # 10 слева, 10 справа
        assert load_hand_left(load_list) == 50
        assert load_hand_right(load_list) == 50

    def test_all_left_hand(self):
        """Вся нагрузка на левой руке."""
        load_list = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 5 слева, 0 справа
        assert load_hand_left(load_list) == 100
        assert load_hand_right(load_list) == 0

    def test_all_right_hand(self):
        """Вся нагрузка на правой руке."""
        load_list = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]  # 0 слева, 5 справа
        assert load_hand_left(load_list) == 0
        assert load_hand_right(load_list) == 100

    def test_empty_load(self):
        """Нулевая нагрузка — деление на ноль избегается."""
        load_list = [0] * 10
        assert load_hand_left(load_list) == 0
        assert load_hand_right(load_list) == 0

    def test_only_left_pinky(self):
        """Один удар мизинцем левой руки."""
        load_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert load_hand_left(load_list) == 100
        assert load_hand_right(load_list) == 0

    def test_only_right_pinky(self):
        """Один удар мизинцем правой руки."""
        load_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        assert load_hand_left(load_list) == 0
        assert load_hand_right(load_list) == 100

    def test_mixed_realistic_load(self):
        """Реалистичный пример: больше на правой."""
        # Левая: 3+2+1+0+0 = 6
        # Правая: 0+5+4+3+2 = 14
        # Всего: 20 → левая = 6/20 = 30%, правая = 70%
        load_list = [3, 2, 1, 0, 0, 0, 5, 4, 3, 2]
        assert load_hand_left(load_list) == 30
        assert load_hand_right(load_list) == 70

    def test_rounding_down(self):
        """Проверка целочисленного округления вниз (int())."""
        # Левая: 1, Правая: 3 → всего 4 → левая = 25%, правая = 75%
        load_list = [1, 0, 0, 0, 0, 0, 1, 1, 1, 0]  # левая=1, правая=3
        assert load_hand_left(load_list) == 25
        assert load_hand_right(load_list) == 75

        # Левая: 1, Правая: 2 → 1/3 ≈ 33.33% → int → 33%
        load_list = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0]
        assert load_hand_left(load_list) == 33
        assert load_hand_right(load_list) == 66  # потому что 2/3 = 66.66 → 66

    def test_invalid_length_list(self):
        """Функции не проверяют длину, но работают, если список >=10.
        Однако в вашем случае всегда 10 элементов. Мы тестируем только валидные входы."""
        # Тесты предполагают корректный вход (10 элементов), как возвращается из count_finger_load
        pass

    def test_non_integer_values(self):
        """Функции работают с числами, но в реальности всегда int.
        Не тестируем float — не используется в вашем коде."""
        pass

    def test_sum_left_plus_sum_right_equals_total(self):
        """Гарантия: нагрузка левой + правой = 100% (если общая нагрузка > 0)."""
        test_cases = [
            [10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        ]
        for load_list in test_cases:
            total = sum(load_list)
            if total == 0:
                continue
            left = load_hand_left(load_list)
            right = load_hand_right(load_list)
            # Из-за округления вниз, сумма может быть 99 или 100
            assert left + right in (99, 100), f"Неверная сумма для {load_list}: {left} + {right} = {left + right}"

    def test_zero_total_returns_zero(self):
        """Если сумма 0 — обе функции возвращают 0."""
        load_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert load_hand_left(load_list) == 0
        assert load_hand_right(load_list) == 0
