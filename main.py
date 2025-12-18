import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pathlib import Path
import sys
import warnings

warnings.filterwarnings('ignore')

from function import (
    count_finger_load_qwerty, count_finger_load_vyzov, count_finger_load_dictor,
    count_finger_load_ant, count_finger_load_rusphone, count_finger_load_skoropis,
    count_finger_load_zubachew, calculate_penalties_qwerty, calculate_penalties_vyzov,
    calculate_penalties_dictor, calculate_penalties_ant, calculate_penalties_rusphone,
    calculate_penalties_skoropis, calculate_penalties_zubachew,
    analyze_rolls_qwerty, analyze_rolls_vyzov, analyze_rolls_dictor,
    analyze_rolls_ant, analyze_rolls_rusphone, analyze_rolls_skoropis,
    analyze_rolls_zubachew, load_text, filter_single_char_words
)

LAYOUT_COLORS = {
    "ЙЦУКЕН": "#FF0000",  # красный
    "ВЫЗОВ": "#000000",  # чёрный
    "DICTOR": "#FFFF00",  # жёлтый
    "ANT": "#3366FF",  # чуть другой синий как Зубачёв, т.к. близкая раскладка
    "RUSPHONE": "#FF69B4",  # розовый
    "SKOROPIS": "#00FF00",  # зелёный
    "ZUBACHEW": "#0000FF",  # синий
}

LAYOUT_NAMES_RU = {
    "ЙЦУКЕН": "ЙЦУКЕН",
    "ВЫЗОВ": "ВЫЗОВ",
    "DICTOR": "Диктор",
    "ANT": "ANT",
    "RUSPHONE": "Русская фонетическая",
    "SKOROPIS": "Скоропись",
    "ZUBACHEW": "Зубачёв",
}

TEXT_FILES = {
    "voina-i-mir.txt": "«Война и мир»",
    "sortchbukw.csv": "sortchbukw",
    "1grams-3.txt": "1grams-3"
}


class KeyboardAnalyzer:

    def __init__(self):
        self.layouts = {
            "ЙЦУКЕН": {
                "load_func": count_finger_load_qwerty,
                "penalty_func": calculate_penalties_qwerty,
                "roll_analyzer": analyze_rolls_qwerty,
                "color": LAYOUT_COLORS["ЙЦУКЕН"]
            },
            "ВЫЗОВ": {
                "load_func": count_finger_load_vyzov,
                "penalty_func": calculate_penalties_vyzov,
                "roll_analyzer": analyze_rolls_vyzov,
                "color": LAYOUT_COLORS["ВЫЗОВ"]
            },
            "DICTOR": {
                "load_func": count_finger_load_dictor,
                "penalty_func": calculate_penalties_dictor,
                "roll_analyzer": analyze_rolls_dictor,
                "color": LAYOUT_COLORS["DICTOR"]
            },
            "ANT": {
                "load_func": count_finger_load_ant,
                "penalty_func": calculate_penalties_ant,
                "roll_analyzer": analyze_rolls_ant,
                "color": LAYOUT_COLORS["ANT"]
            },
            "RUSPHONE": {
                "load_func": count_finger_load_rusphone,
                "penalty_func": calculate_penalties_rusphone,
                "roll_analyzer": analyze_rolls_rusphone,
                "color": LAYOUT_COLORS["RUSPHONE"]
            },
            "SKOROPIS": {
                "load_func": count_finger_load_skoropis,
                "penalty_func": calculate_penalties_skoropis,
                "roll_analyzer": analyze_rolls_skoropis,
                "color": LAYOUT_COLORS["SKOROPIS"]
            },
            "ZUBACHEW": {
                "load_func": count_finger_load_zubachew,
                "penalty_func": calculate_penalties_zubachew,
                "roll_analyzer": analyze_rolls_zubachew,
                "color": LAYOUT_COLORS["ZUBACHEW"]
            },
        }

        self.finger_names = [
            "Левый мизинец", "Левый безымянный", "Левый средний",
            "Левый указательный", "Левый большой",
            "Правый большой", "Правый указательный",
            "Правый средний", "Правый безымянный", "Правый мизинец"
        ]

        self.finger_short = ["Л. М.", "Л. Б.", "Л. С.", "Л. У.", "Л. Бол.", "П. Бол.", "П. У.", "П. С.", "П. Б.", "П. М."]

        self.results = {}
        self.current_text = ""
        self.text_name = ""

    def load_and_process(self, filename):
        try:
            raw_text = load_text(filename)
            self.current_text = filter_single_char_words(raw_text)
            self.text_name = TEXT_FILES.get(filename, filename)
            return True
        except Exception as e:
            print(f"Ошибка загрузки файла {filename}: {e}")
            return False

    def analyze_all_layouts(self):
        if not self.current_text:
            print("Сначала загрузите текст!")
            return

        self.results = {}

        for layout_name, layout_funcs in self.layouts.items():
            print(f"Анализ раскладки: {layout_name}")

            finger_load = layout_funcs["load_func"](self.current_text)
            total_load = sum(finger_load)

            penalties = layout_funcs["penalty_func"](self.current_text)

            left_load = sum(finger_load[:5])
            right_load = sum(finger_load[5:])
            total = left_load + right_load
            left_percent = int((left_load * 100) / total) if total > 0 else 0
            right_percent = int((right_load * 100) / total) if total > 0 else 0
            both_percent = 0

            roll_result = layout_funcs["roll_analyzer"](self.current_text)
            totals = roll_result["total"]
            grand_total = sum(totals.values())

            left_rolls = {2: 0, 3: 0, 4: 0, 5: 0}
            right_rolls = {2: 0, 3: 0, 4: 0, 5: 0}

            for length in [2, 3, 4, 5]:
                if length in roll_result["by_length"]:
                    stats = roll_result["by_length"][length]
                    total_this_length = sum(stats.values())
                    if total_this_length > 0:
                        left_rolls[length] = stats['convenient'] // 2
                        right_rolls[length] = stats['convenient'] - left_rolls[length]

            self.results[layout_name] = {
                "finger_load": finger_load,
                "total_load": total_load,
                "penalties": penalties,
                "left_percent": left_percent,
                "right_percent": right_percent,
                "both_percent": both_percent,
                "roll_stats": roll_result,
                "left_rolls": left_rolls,
                "right_rolls": right_rolls,
                "color": layout_funcs["color"]
            }

        return self.results

    def plot_finger_load_comparison(self, selected_layouts=None):
        if not self.results:
            print("Сначала выполните анализ!")
            return

        if selected_layouts is None:
            selected_layouts = list(self.layouts.keys())

        fig, axes = plt.subplots(2, 1, figsize=(14, 10))

        ax1 = axes[0]
        x = np.arange(len(self.finger_short))
        width = 0.12

        for i, layout_name in enumerate(selected_layouts):
            if layout_name in self.results:
                load = self.results[layout_name]["finger_load"]
                normalized_load = [l / max(load) * 100 if max(load) > 0 else 0 for l in load]
                ax1.bar(x + i * width - width * len(selected_layouts) / 2 + width / 2,
                        normalized_load, width,
                        label=LAYOUT_NAMES_RU[layout_name],
                        color=self.results[layout_name]["color"])

        ax1.set_xlabel('Пальцы')
        ax1.set_ylabel('Нагрузка (%)')
        ax1.set_title(f'Сравнение нагрузки на пальцы\nТекст: {self.text_name}')
        ax1.set_xticks(x)
        ax1.set_xticklabels(self.finger_short, rotation=45)
        ax1.legend(loc='upper right', ncol=2)
        ax1.grid(True, alpha=0.3)

        ax2 = axes[1]
        layout_names = []
        penalties = []
        colors = []

        for layout_name in selected_layouts:
            if layout_name in self.results:
                layout_names.append(LAYOUT_NAMES_RU[layout_name])
                penalties.append(self.results[layout_name]["penalties"])
                colors.append(self.results[layout_name]["color"])

        bars = ax2.bar(layout_names, penalties, color=colors)
        ax2.set_xlabel('Раскладка')
        ax2.set_ylabel('Штрафы')
        ax2.set_title('Сравнение штрафов за смещение от домашнего ряда')
        ax2.grid(True, alpha=0.3)

        for bar, penalty in zip(bars, penalties):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                     f'{penalty}', ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

    def plot_hand_distribution(self, selected_layouts=None):
        if not self.results:
            print("Сначала выполните анализ!")
            return

        if selected_layouts is None:
            selected_layouts = list(self.layouts.keys())

        n_layouts = len(selected_layouts)
        n_cols = min(3, n_layouts)
        n_rows = (n_layouts + n_cols - 1) // n_cols

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(4 * n_cols, 4 * n_rows))
        if n_layouts == 1:
            axes = np.array([axes])
        if n_rows == 1 and n_cols > 1:
            axes = axes.reshape(1, -1)

        for idx, layout_name in enumerate(selected_layouts):
            if layout_name in self.results:
                row = idx // n_cols
                col = idx % n_cols
                ax = axes[row, col] if n_rows > 1 or n_cols > 1 else axes[idx]

                left_percent = self.results[layout_name]["left_percent"]
                right_percent = self.results[layout_name]["right_percent"]
                both_percent = 100 - left_percent - right_percent

                sizes = [left_percent, right_percent, both_percent]
                labels = ['Левая', 'Правая', 'Обе руки']
                colors = ['#FF6B6B', '#4ECDC4', '#95E1D3']

                wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                                  autopct='%1.1f%%', startangle=90)

                ax.set_title(f'{LAYOUT_NAMES_RU[layout_name]}\nРаспределение нагрузки',
                             fontsize=10)

                for text in texts + autotexts:
                    text.set_fontsize(9)

        for idx in range(n_layouts, n_rows * n_cols):
            row = idx // n_cols
            col = idx % n_cols
            axes[row, col].axis('off')

        plt.suptitle(f'Распределение нагрузки на руки\nТекст: {self.text_name}', fontsize=14)
        plt.tight_layout()
        plt.show()

    def plot_rolls_comparison(self, selected_layouts=None):
        if not self.results:
            print("Сначала выполните анализ!")
            return

        if selected_layouts is None:
            selected_layouts = list(self.layouts.keys())

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()

        lengths = [2, 3]
        titles = [
            'Удобные переборы (левая рука)',
            'Удобные переборы (правая рука)',
            'Все удобные последовательности',
            'Частично удобные и неудобные (2 символа)'
        ]

        for plot_idx in range(4):
            ax = axes[plot_idx]
            x = np.arange(len(lengths)) if plot_idx != 3 else np.arange(2)
            width = 0.15

            for i, layout_name in enumerate(selected_layouts):
                if layout_name in self.results:
                    stats = self.results[layout_name]["roll_stats"]
                    color = self.results[layout_name]["color"]

                    if plot_idx == 0:
                        values = [self.results[layout_name]["left_rolls"][l] for l in lengths]
                        x_pos = x
                    elif plot_idx == 1:
                        values = [self.results[layout_name]["right_rolls"][l] for l in lengths]
                        x_pos = x
                    elif plot_idx == 2:
                        values = [stats["by_length"][l]["convenient"] for l in lengths]
                        x_pos = x
                    else:
                        values = [
                            stats["by_length"][2]["semi"],
                            stats["by_length"][2]["inconvenient"]
                        ]
                        x_pos = np.arange(2)

                    ax.bar(x_pos + i * width - width * len(selected_layouts) / 2 + width / 2,
                           values, width, label=LAYOUT_NAMES_RU[layout_name],
                           color=color, alpha=0.8)

            ax.set_xlabel('Длина последовательности' if plot_idx != 3 else 'Тип последовательности')
            ax.set_ylabel('Количество')
            ax.set_title(titles[plot_idx])

            if plot_idx != 3:
                ax.set_xticks(x)
                ax.set_xticklabels([f'{l} симв.' for l in lengths])
            else:
                ax.set_xticks([0, 1])
                ax.set_xticklabels(['Частично\nудобные', 'Неудобные'])

            ax.grid(True, alpha=0.3)

            if plot_idx == 0:
                ax.legend(loc='upper left', fontsize=8)

        plt.suptitle(f'Анализ переборов по раскладкам\nТекст: {self.text_name}', fontsize=14)
        plt.tight_layout()
        plt.show()

    def plot_overall_convenience(self, selected_layouts=None):
        if not self.results:
            print("Сначала выполните анализ!")
            return

        if selected_layouts is None:
            selected_layouts = list(self.layouts.keys())

        fig, ax = plt.subplots(figsize=(12, 6))

        categories = ['Удобные', 'Частично удобные', 'Неудобные']
        x = np.arange(len(categories))
        width = 0.12

        for i, layout_name in enumerate(selected_layouts):
            if layout_name in self.results:
                stats = self.results[layout_name]["roll_stats"]["total"]
                values = [stats['convenient'], stats['semi'], stats['inconvenient']]

                ax.bar(x + i * width - width * len(selected_layouts) / 2 + width / 2,
                       values, width, label=LAYOUT_NAMES_RU[layout_name],
                       color=self.results[layout_name]["color"], alpha=0.8)

        ax.set_xlabel('Категория удобства')
        ax.set_ylabel('Количество последовательностей')
        ax.set_title(f'Распределение нажатий по удобству\nТекст: {self.text_name}')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend(loc='upper right')
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    def plot_individual_finger_load(self, layout_name):
        if layout_name not in self.results:
            print(f"Раскладка {layout_name} не найдена в результатах!")
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        load = self.results[layout_name]["finger_load"]
        total = sum(load)
        percentages = [l / total * 100 if total > 0 else 0 for l in load]

        bars = ax1.bar(self.finger_short, percentages,
                       color=['#FF9999', '#FFB366', '#FFFF66', '#99FF99', '#66B3FF',
                              '#66B3FF', '#99FF99', '#FFFF66', '#FFB366', '#FF9999'])

        ax1.set_xlabel('Пальцы')
        ax1.set_ylabel('Нагрузка (%)')
        ax1.set_title(f'Нагрузка на пальцы - {LAYOUT_NAMES_RU[layout_name]}\nТекст: {self.text_name}')
        ax1.grid(True, alpha=0.3)

        for bar, percentage in zip(bars, percentages):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                     f'{percentage:.1f}%', ha='center', va='bottom', fontsize=9)

        wedges, texts, autotexts = ax2.pie(percentages, labels=self.finger_short,
                                           autopct='%1.1f%%', startangle=90)
        ax2.set_title(f'Распределение нагрузки\n{LAYOUT_NAMES_RU[layout_name]}')

        plt.tight_layout()
        plt.show()

    def print_statistics(self, selected_layouts=None):
        if not self.results:
            print("Сначала выполните анализ!")
            return

        if selected_layouts is None:
            selected_layouts = list(self.layouts.keys())

        print("\n" + "=" * 80)
        print(f"СТАТИСТИКА АНАЛИЗА РАСКЛАДОК")
        print(f"Текст: {self.text_name}")
        print("=" * 80)

        for layout_name in selected_layouts:
            if layout_name in self.results:
                data = self.results[layout_name]
                print(f"\n{LAYOUT_NAMES_RU[layout_name]}:")
                print(f"  Общая нагрузка: {data['total_load']} нажатий")
                print(f"  Штрафы: {data['penalties']}")
                print(f"  Нагрузка на руки: Левая {data['left_percent']}%, Правая {data['right_percent']}%")

                rolls = data['roll_stats']['total']
                total_rolls = sum(rolls.values())
                if total_rolls > 0:
                    print(
                        f"  Переборы: Удобные {rolls['convenient']} ({rolls['convenient'] / total_rolls * 100:.1f}%), "
                        f"Частично {rolls['semi']} ({rolls['semi'] / total_rolls * 100:.1f}%), "
                        f"Неудобные {rolls['inconvenient']} ({rolls['inconvenient'] / total_rolls * 100:.1f}%)")
                else:
                    print(f"  Переборы: нет данных")


def main_menu():
    analyzer = KeyboardAnalyzer()

    while True:
        print("\n" + "=" * 60)
        print("АНАЛИЗАТОР РАСКЛАДОК КЛАВИАТУР")
        print("=" * 60)
        print("\n1. Загрузить текст для анализа")
        print("2. Выполнить анализ всех раскладок")
        print("3. Сравнить выбранные раскладки")
        print("4. Показать все графики")
        print("5. Индивидуальный анализ раскладки")
        print("6. Вывести статистику")
        print("0. Выход")

        choice = input("\nВыберите действие (0-6): ").strip()

        if choice == "0":
            print("До свидания!")
            break

        elif choice == "1":
            print("\nДоступные файлы:")
            for i, (filename, desc) in enumerate(TEXT_FILES.items(), 1):
                print(f"{i}. {desc} ({filename})")

            file_choice = input("\nВыберите файл (1-3): ").strip()
            if file_choice in ["1", "2", "3"]:
                filename = list(TEXT_FILES.keys())[int(file_choice) - 1]
                if analyzer.load_and_process(filename):
                    print(f"✓ Текст '{TEXT_FILES[filename]}' загружен и обработан")
                else:
                    print("✗ Ошибка загрузки файла")
            else:
                print("Неверный выбор")

        elif choice == "2":
            if not analyzer.current_text:
                print("Сначала загрузите текст!")
                continue

            print("Выполняется анализ всех раскладок...")
            analyzer.analyze_all_layouts()
            print("✓ Анализ завершен")

        elif choice == "3":
            if not analyzer.results:
                print("Сначала выполните анализ!")
                continue

            print("\nДоступные раскладки:")
            for i, layout_name in enumerate(LAYOUT_NAMES_RU.keys(), 1):
                print(f"{i}. {LAYOUT_NAMES_RU[layout_name]}")

            print("\nВведите номера раскладок для сравнения (через пробел):")
            print("Пример: 1 3 5 или 'all' для всех")

            selection = input("Ваш выбор: ").strip()

            if selection.lower() == 'all':
                selected_layouts = list(LAYOUT_NAMES_RU.keys())
            else:
                try:
                    indices = [int(x) - 1 for x in selection.split()]
                    selected_layouts = [list(LAYOUT_NAMES_RU.keys())[i] for i in indices]
                except:
                    print("Неверный формат ввода")
                    continue

            print("\nГенерация графиков сравнения...")
            analyzer.plot_finger_load_comparison(selected_layouts)
            analyzer.plot_hand_distribution(selected_layouts)
            analyzer.plot_rolls_comparison(selected_layouts)
            analyzer.plot_overall_convenience(selected_layouts)

        elif choice == "4":
            if not analyzer.results:
                print("Сначала выполните анализ!")
                continue

            print("Генерация всех графиков...")
            analyzer.plot_finger_load_comparison()
            analyzer.plot_hand_distribution()
            analyzer.plot_rolls_comparison()
            analyzer.plot_overall_convenience()

        elif choice == "5":
            if not analyzer.results:
                print("Сначала выполните анализ!")
                continue

            print("\nДоступные раскладки:")
            for i, layout_name in enumerate(LAYOUT_NAMES_RU.keys(), 1):
                print(f"{i}. {LAYOUT_NAMES_RU[layout_name]}")

            layout_choice = input("\nВыберите раскладку (1-7): ").strip()
            if layout_choice in [str(i) for i in range(1, 8)]:
                layout_name = list(LAYOUT_NAMES_RU.keys())[int(layout_choice) - 1]
                analyzer.plot_individual_finger_load(layout_name)
            else:
                print("Неверный выбор")

        elif choice == "6":
            if not analyzer.results:
                print("Сначала выполните анализ!")
                continue
            analyzer.print_statistics()

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    plt.style.use('seaborn-v0_8-darkgrid')
    mpl.rcParams['font.family'] = 'DejaVu Sans'
    mpl.rcParams['font.size'] = 10
    mpl.rcParams['figure.titlesize'] = 12
    mpl.rcParams['axes.titlesize'] = 11

    main_menu()
