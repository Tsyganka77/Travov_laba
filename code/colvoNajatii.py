"""Main script to analyze text on multiple keyboard layouts."""

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
    count_convenient_rolls_qwerty,
    count_convenient_rolls_vyzov,
    count_convenient_rolls_dictor,
    count_convenient_rolls_ant,
    count_convenient_rolls_rusphone,
    count_convenient_rolls_skoropis,
    count_convenient_rolls_zubachew,
    filter_single_char_words,
)

if __name__ == "__main__":
    with open("voina_i_mir.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Удаляем односимвольные СЛОВА (союзы), но не символы!
    text = filter_single_char_words(text)

    fingers = [
        "левый мизинец", "левый безымянный", "левый средний",
        "левый указательный", "левый большой",
        "правый большой", "правый указательный",
        "правый средний", "правый безымянный", "правый мизинец"
    ]

    # Собираем данные один раз
    layouts_data = {
        "ЙЦУКЕН": {
            "load": count_finger_load_qwerty(text),
            "penalties": calculate_penalties_qwerty(text),
            "convenient": count_convenient_rolls_qwerty(text),
        },
        "ВЫЗОВ": {
            "load": count_finger_load_vyzov(text),
            "penalties": calculate_penalties_vyzov(text),
            "convenient": count_convenient_rolls_vyzov(text),
        },
        "DICTOR": {
            "load": count_finger_load_dictor(text),
            "penalties": calculate_penalties_dictor(text),
            "convenient": count_convenient_rolls_dictor(text),
        },
        "ANT": {
            "load": count_finger_load_ant(text),
            "penalties": calculate_penalties_ant(text),
            "convenient": count_convenient_rolls_ant(text),
        },
        "RUSPHONE": {
            "load": count_finger_load_rusphone(text),
            "penalties": calculate_penalties_rusphone(text),
            "convenient": count_convenient_rolls_rusphone(text),
        },
        "SKOROPIS": {
            "load": count_finger_load_skoropis(text),
            "penalties": calculate_penalties_skoropis(text),
            "convenient": count_convenient_rolls_skoropis(text),
        },
        "ZUBACHEW": {
            "load": count_finger_load_zubachew(text),
            "penalties": calculate_penalties_zubachew(text),
            "convenient": count_convenient_rolls_zubachew(text),
        },
    }

    # Добавляем проценты левой/правой руки
    for data in layouts_data.values():
        load = data["load"]
        data["left"] = load_hand_left(load)
        data["right"] = load_hand_right(load)

    # === ТЕРМИНАЛЬНОЕ МЕНЮ ===
    while True:
        print("\n" + "="*50)
        print("1. ЙЦУКЕН")
        print("2. ВЫЗОВ")
        print("3. DICTOR")
        print("4. ANT")
        print("5. RUSPHONE")
        print("6. SKOROPIS")
        print("7. ZUBACHEW")
        print("8. Все сразу")
        print("0. Выйти")
        print("-"*50)
        
        try:
            choice = input("Выберите раскладку (0–8): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n До свидания!")
            break

        if choice == "0":
            print(" До свидания!")
            break
        elif choice == "8":
            for name, data in layouts_data.items():
                print("\n" + "="*68)
                print(name)
                print("="*68)
                print(f"Нагрузка: левая — {data['left']}%, правая — {data['right']}%")
                print("Нажатий каждым пальцем:")
                for finger, cnt in zip(fingers, data["load"]):
                    print(f"  • {finger}: {cnt}")
                print(f"Штрафы за смещение: {data['penalties']}")
                print(f"Удобных переборов: {data['convenient']}")
            print("\n" + "="*68)
        elif choice in "1234567":
            names = ["ЙЦУКЕН", "ВЫЗОВ", "DICTOR", "ANT", "RUSPHONE", "SKOROPIS", "ZUBACHEW"]
            name = names[int(choice)-1]
            data = layouts_data[name]
            print("\n" + "="*68)
            print(f" {name}")
            print("="*68)
            print(f"Нагрузка: левая — {data['left']}%, правая — {data['right']}%")
            print("Нажатий каждым пальцем:")
            for finger, cnt in zip(fingers, data["load"]):
                print(f"  • {finger}: {cnt}")
            print(f"Штрафы за смещение: {data['penalties']}")
            print(f"Удобных переборов: {data['convenient']}")
            print("="*68)
        else:
            print(" Неверный ввод. Введите число от 0 до 8.")
