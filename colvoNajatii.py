from function import (
    count_finger_load_qwerty,
    count_finger_load_vyzov,
    count_finger_load_dictor,
    count_finger_load_ant,
    count_finger_load_rusphone,
    count_finger_load_skoropis,
    count_finger_load_zubachew,
    load_hand_left,
    load_hand_right,
    calculate_penalties_qwerty,
    calculate_penalties_vyzov,
    calculate_penalties_dictor,
    calculate_penalties_ant,
    calculate_penalties_rusphone,
    calculate_penalties_skoropis,
    calculate_penalties_zubachew,
    filter_single_char_words,
    analyze_rolls_qwerty,
    analyze_rolls_vyzov,
    analyze_rolls_dictor,
    analyze_rolls_ant,
    analyze_rolls_rusphone,
    analyze_rolls_skoropis,
    analyze_rolls_zubachew,
    load_text,
)

TEXT_FILES = [
    ("voina_i_mir.txt", "«Война и мир»"),
    ("1grams-3.txt", "1-граммы"),
    ("sortchbukw.csv", "CSV-файл"),
]

LAYOUTS = {
    "ЙЦУКЕН": {
        "load_func": count_finger_load_qwerty,
        "penalty_func": calculate_penalties_qwerty,
        "roll_analyzer": analyze_rolls_qwerty,
    },
    "ВЫЗОВ": {
        "load_func": count_finger_load_vyzov,
        "penalty_func": calculate_penalties_vyzov,
        "roll_analyzer": analyze_rolls_vyzov,
    },
    "DICTOR": {
        "load_func": count_finger_load_dictor,
        "penalty_func": calculate_penalties_dictor,
        "roll_analyzer": analyze_rolls_dictor,
    },
    "ANT": {
        "load_func": count_finger_load_ant,
        "penalty_func": calculate_penalties_ant,
        "roll_analyzer": analyze_rolls_ant,
    },
    "RUSPHONE": {
        "load_func": count_finger_load_rusphone,
        "penalty_func": calculate_penalties_rusphone,
        "roll_analyzer": analyze_rolls_rusphone,
    },
    "SKOROPIS": {
        "load_func": count_finger_load_skoropis,
        "penalty_func": calculate_penalties_skoropis,
        "roll_analyzer": analyze_rolls_skoropis,
    },
    "ZUBACHEW": {
        "load_func": count_finger_load_zubachew,
        "penalty_func": calculate_penalties_zubachew,
        "roll_analyzer": analyze_rolls_zubachew,
    },
}

if __name__ == "__main__":
    texts = {}
    for filename, _ in TEXT_FILES:
        try:
            texts[filename] = load_text(filename)
        except Exception as e:
            print(f"Ошибка загрузки '{filename}': {e}")
            texts[filename] = ""

    fingers = [
        "левый мизинец", "левый безымянный", "левый средний",
        "левый указательный", "левый большой",
        "правый большой", "правый указательный",
        "правый средний", "правый безымянный", "правый мизинец"
    ]

    while True:
        print("\n" + "=" * 50)
        print("1. ЙЦУКЕН")
        print("2. ВЫЗОВ")
        print("3. DICTOR")
        print("4. ANT")
        print("5. RUSPHONE")
        print("6. SKOROPIS")
        print("7. ZUBACHEW")
        print("0. Выйти")
        print("-" * 50)

        try:
            choice = input("Выберите раскладку (0–7): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n До свидания!")
            break

        if choice == "0":
            print(" До свидания!")
            break
        if not choice or choice not in "1234567":
            print(" Неверный ввод. Введите число от 0 до 7.")
            continue

        layout_name = list(LAYOUTS.keys())[int(choice) - 1]
        cfg = LAYOUTS[layout_name]

        print("\n" + "=" * 50)
        for i, (_, desc) in enumerate(TEXT_FILES, 1):
            print(f"{i}. {desc}")
        print("0. Отмена")
        print("-" * 50)

        try:
            text_choice = input("Выберите текст (0–3): ").strip()
        except (KeyboardInterrupt, EOFError):
            continue

        if text_choice == "0":
            continue
        if not text_choice or text_choice not in "123":
            print(" Неверный ввод.")
            continue

        filename, desc = TEXT_FILES[int(text_choice) - 1]
        raw_text = texts[filename]
        if not raw_text:
            print(f"Текст '{desc}' не загружен.")
            continue

        text = filter_single_char_words(raw_text)

        load = cfg["load_func"](text)
        penalties = cfg["penalty_func"](text)
        left_pct = load_hand_left(load)
        right_pct = load_hand_right(load)

        print(f"\n{layout_name} — {desc}")
        print("=" * 68)
        print(f"Нагрузка: левая — {left_pct}%, правая — {right_pct}%")
        print("Нажатий каждым пальцем:")
        for finger, cnt in zip(fingers, load):
            print(f"  • {finger}: {cnt}")
        print(f"Штрафы за смещение: {penalties}")

        roll_result = cfg["roll_analyzer"](text)

        for length in [2, 3, 4, 5]:
            if length not in roll_result["by_length"]:
                continue
            stats = roll_result["by_length"][length]
            total = sum(stats.values())
            if total == 0:
                continue
            print(f"\nСлова длиной {length}:")
            print(f"  Удобные:          {stats['convenient']}")
            print(f"  Частично удобные: {stats['semi']}")
            print(f"  Неудобные:        {stats['inconvenient']}")

        totals = roll_result["total"]
        grand_total = sum(totals.values())
        if grand_total:
            print("\nИТОГО по переборам:")
            print(f"  Удобные:          {totals['convenient']} ({totals['convenient'] / grand_total * 100:.1f}%)")
            print(f"  Частично удобные: {totals['semi']} ({totals['semi'] / grand_total * 100:.1f}%)")
            print(f"  Неудобные:        {totals['inconvenient']} ({totals['inconvenient'] / grand_total * 100:.1f}%)")
        else:
            print("\nНи одного слова из букв не найдено.")

        print("=" * 68)
