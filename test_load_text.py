import pytest
import csv
from pathlib import Path
from function import load_text


# === ТЕСТЫ ДЛЯ ОБЫЧНОГО ТЕКСТОВОГО ФАЙЛА ===
def test_load_text_file_empty(tmp_path):
    """Пустой текстовый файл."""
    text_file = tmp_path / "empty.txt"
    text_file.write_text("", encoding="utf-8")
    result = load_text(str(text_file))
    assert result == ""


def test_load_text_file_no_letters(tmp_path):
    """Текст без букв — только цифры и знаки → результат состоит только из пробелов."""
    text_file = tmp_path / "no_letters.txt"
    content = "123!@# $%^"
    text_file.write_text(content, encoding="utf-8")
    result = load_text(str(text_file))

    # Проверяем, что в результате только пробелы (возможно, много)
    assert result.strip() == "", "Результат должен содержать только пробелы"
    assert all(c == ' ' for c in result), "Все символы должны быть пробелами"

    # Дополнительно: длина совпадает с исходной (поскольку каждый символ → пробел или остаётся пробелом)
    assert len(result) == len(content)


def test_load_text_file_cyrillic_and_latin(tmp_path):
    """Смешанный кириллический и латинский текст: знаки препинания заменяются на пробелы,
    но слова сохраняются в правильном порядке."""
    text_file = tmp_path / "mixed.txt"
    text_file.write_text("Hello привет! Мир world.", encoding="utf-8")
    result = load_text(str(text_file))

    # Проверяем, что слова остались, а спецсимволы исчезли
    words = result.split()
    assert words == ["Hello", "привет", "Мир", "world"]


def test_load_text_file_preserves_whitespace_as_spaces(tmp_path):
    """Не-буквы заменяются на пробелы; другие пробельные символы (\n, \t) сохраняются."""
    text_file = tmp_path / "whitespace.txt"
    text_file.write_text("a\nb\tc!d", encoding="utf-8")
    result = load_text(str(text_file))
    # Ожидаем: 'a\nb\tc d'
    expected = "a\nb\tc d"
    assert result == expected


# === ТЕСТЫ ДЛЯ CSV-ФАЙЛА ===

def test_load_csv_file_basic(tmp_path):
    """CSV: извлекаем двухбуквенные пары из второго столбца."""
    csv_file = tmp_path / "pairs.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "bigram"])
        writer.writerow(["1", "аб"])
        writer.writerow(["2", "cd"])
        writer.writerow(["3", "ef"])

    result = load_text(str(csv_file))
    assert result == "аб cd ef"


def test_load_csv_file_skips_invalid_rows(tmp_path):
    """CSV: пропускаем строки без второго столбца или с не-двухбуквенными парами."""
    csv_file = tmp_path / "invalid.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["1", "ab"])
        writer.writerow(["2", "x"])       # 1 символ — пропустить
        writer.writerow(["3", "abc"])     # 3 символа — пропустить
        writer.writerow(["4", "12"])      # не alpha — пропустить
        writer.writerow(["5", "a1"])      # не alpha — пропустить
        writer.writerow(["6"])            # нет второго столбца — пропустить
        writer.writerow(["7", "ёж"])      # кириллица — alpha → оставить

    result = load_text(str(csv_file))
    assert result == "ab ёж"


def test_load_csv_file_empty(tmp_path):
    """Пустой CSV-файл."""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("", encoding="utf-8")
    result = load_text(str(csv_file))
    assert result == ""


def test_load_csv_file_no_valid_pairs(tmp_path):
    """CSV без валидных двухбуквенных пар."""
    csv_file = tmp_path / "no_valid.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["1", "a"])
        writer.writerow(["2", "123"])
        writer.writerow(["3", "!!"])

    result = load_text(str(csv_file))
    assert result == ""


def test_load_csv_case_sensitivity(tmp_path):
    """CSV: буквы любого регистра допустимы (isalpha() разрешает)."""
    csv_file = tmp_path / "case.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["1", "Ab"])
        writer.writerow(["2", "ЁЖ"])

    result = load_text(str(csv_file))
    assert result == "Ab ЁЖ"  # оригинальный регистр сохраняется


def test_file_not_found():
    """Файл не существует → ожидаем FileNotFoundError (не перехватывается)."""
    with pytest.raises(FileNotFoundError):
        load_text("/non/existent/file.txt")
