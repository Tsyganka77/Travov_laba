import pytest
from function import filter_single_char_words


class TestFilterSingleCharWords:

    def test_removes_single_latin_letters(self):
        assert filter_single_char_words("a test b") == " test "
        assert filter_single_char_words("I am ok") == " am ok"  # 'I' удалится
        assert filter_single_char_words("x y z") == "  "  # остаются пробелы

    def test_preserves_multi_char_words(self):
        assert filter_single_char_words("hello world") == "hello world"
        assert filter_single_char_words("привет мир") == "привет мир"

    def test_preserves_digits_and_special_tokens(self):
        # Односимвольные цифры НЕ удаляются (по задумке regex)
        assert filter_single_char_words("a 1 b 2") == " 1  2"
        # Слова с цифрами или спецсимволами не считаются "буквенными"
        assert filter_single_char_words("a _ b") == " _ "
        assert filter_single_char_words("a 5 b") == " 5 "

    def test_handles_punctuation_correctly(self):
        assert filter_single_char_words("a, b and c.") == ",  and ."
        assert filter_single_char_words("Он сказал: «я».") == "Он сказал: «»."

    def test_handles_mixed_latin_cyrillic(self):
        assert filter_single_char_words("a я test") == "  test"

    def test_empty_string(self):
        assert filter_single_char_words("") == ""

    def test_only_single_letters(self):
        assert filter_single_char_words("a b c") == "  "
        assert filter_single_char_words("я и с") == "  "

    def test_no_single_letters(self):
        assert filter_single_char_words("hello bye") == "hello bye"
        assert filter_single_char_words("мама мыла раму") == "мама мыла раму"

    def test_single_letter_at_start_end(self):
        assert filter_single_char_words("a hello") == " hello"
        assert filter_single_char_words("hello b") == "hello "
        assert filter_single_char_words("a") == ""
        assert filter_single_char_words("я") == ""

    def test_preserves_underscore_and_digits_in_words(self):
        # Эти не являются "словами из одной буквы", поэтому не трогаются
        assert filter_single_char_words("_ a 1") == "_  1"
        # Но сами по себе буквы удаляются

    def test_consecutive_spaces_after_removal(self):
        # Допустимо, что остаются лишние пробелы — это ожидаемо
        result = filter_single_char_words("a b c")
        assert result == "  "  # три буквы → два пробела между, но на самом деле " a b c" → "   " → но regex заменяет каждую на пустое → "  " (3 символа → 3 замены → "   " → нет, давайте проверим)

        # Уточнение: "a b c" → после удаления: "" + " " + "" + " " + "" → "  "
        assert result == "  "
