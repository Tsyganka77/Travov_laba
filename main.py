import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from typing import Dict, List, Tuple, Any
import os

from function import (
    count_finger_load_qwerty, count_finger_load_vyzov, count_finger_load_dictor,
    count_finger_load_ant, count_finger_load_rusphone, count_finger_load_skoropis,
    count_finger_load_zubachew,
    load_hand_left, load_hand_right,
    calculate_penalties_qwerty, calculate_penalties_vyzov, calculate_penalties_dictor,
    calculate_penalties_ant, calculate_penalties_rusphone, calculate_penalties_skoropis,
    calculate_penalties_zubachew,
    count_convenient_rolls_qwerty, count_convenient_rolls_vyzov, count_convenient_rolls_dictor,
    count_convenient_rolls_ant, count_convenient_rolls_rusphone, count_convenient_rolls_skoropis,
    count_convenient_rolls_zubachew,
    filter_single_char_words
)

LAYOUT_COLORS = {
    "ЙЦУКЕН": "#FF0000",  # Красный
    "RUSPHONE": "#FF69B4",  # Розовый
    "DICTOR": "#FFFF00",  # Жёлтый
    "SKOROPIS": "#00FF00",  # Зелёный
    "ZUBACHEW": "#0000FF",  # Синий
    "ВЫЗОВ": "#000000",  # Чёрный
    "ANT": "#4169E1",  # Королевский синий
}

LAYOUT_NAMES = {
    "ЙЦУКЕН": "ЙЦУКЕН",
    "ВЫЗОВ": "ВЫЗОВ",
    "DICTOR": "ДИКТОР",
    "ANT": "ANT",
    "RUSPHONE": "Русская фонетическая",
    "SKOROPIS": "Скоропись",
    "ZUBACHEW": "Зубачёв"
}

LAYOUT_FUNCTIONS = {
    "ЙЦУКЕН": {
        "load": count_finger_load_qwerty,
        "penalties": calculate_penalties_qwerty,
        "convenient": count_convenient_rolls_qwerty,
    },
    "ВЫЗОВ": {
        "load": count_finger_load_vyzov,
        "penalties": calculate_penalties_vyzov,
        "convenient": count_convenient_rolls_vyzov,
    },
    "DICTOR": {
        "load": count_finger_load_dictor,
        "penalties": calculate_penalties_dictor,
        "convenient": count_convenient_rolls_dictor,
    },
    "ANT": {
        "load": count_finger_load_ant,
        "penalties": calculate_penalties_ant,
        "convenient": count_convenient_rolls_ant,
    },
    "RUSPHONE": {
        "load": count_finger_load_rusphone,
        "penalties": calculate_penalties_rusphone,
        "convenient": count_convenient_rolls_rusphone,
    },
    "SKOROPIS": {
        "load": count_finger_load_skoropis,
        "penalties": calculate_penalties_skoropis,
        "convenient": count_convenient_rolls_skoropis,
    },
    "ZUBACHEW": {
        "load": count_finger_load_zubachew,
        "penalties": calculate_penalties_zubachew,
        "convenient": count_convenient_rolls_zubachew,
    },
}


def load_text_files():
    texts = {}
    file_paths = {
        "voina-i-mir": "voina-i-mir.txt",
        "sortchbukw": "sortchbukw.csv",
        "1grams-3": "1grams-3.txt"
    }

    for name, path in file_paths.items():
        try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    texts[name] = f.read()
                print(f"✓ Загружен файл: {path}")
            else:
                print(f"✗ Файл не найден: {path}")
                texts[name] = ""
        except Exception as e:
            print(f"✗ Ошибка при загрузке {path}: {e}")
            texts[name] = ""

    return texts


def analyze_text(text: str, layout_name: str) -> Dict[str, Any]:
    if not text:
        return {}

    functions = LAYOUT_FUNCTIONS[layout_name]
    filtered_text = filter_single_char_words(text)

    load = functions["load"](filtered_text)
    total_chars = sum(load)

    left_percent = load_hand_left(load)
    right_percent = load_hand_right(load)

    both_hands_percent = 100 - (left_percent + right_percent)

    penalties = functions["penalties"](filtered_text)
    convenient_rolls = functions["convenient"](filtered_text)

    return {
        "name": layout_name,
        "load": load,
        "left_percent": left_percent,
        "right_percent": right_percent,
        "both_hands_percent": both_hands_percent,
        "penalties": penalties,
        "convenient_rolls": convenient_rolls,
        "total_chars": total_chars,
        "penalty_per_char": penalties / total_chars if total_chars > 0 else 0,
        "rolls_per_char": convenient_rolls / total_chars if total_chars > 0 else 0,
    }


def plot_finger_load_comparison(results: Dict[str, Dict[str, Any]], filename: str = None):
    fig, ax = plt.subplots(figsize=(14, 8))

    fingers = [
        "Л. мизинец", "Л. безымянный", "Л. средний", "Л. указательный", "Л. большой",
        "П. большой", "П. указательный", "П. средний", "П. безымянный", "П. мизинец"
    ]

    x = np.arange(len(fingers))
    width = 0.8 / len(results)

    for i, (layout_name, data) in enumerate(results.items()):
        if not data:
            continue
        offset = width * i - width * (len(results) - 1) / 2
        ax.bar(x + offset, data["load"], width,
               label=LAYOUT_NAMES.get(layout_name, layout_name),
               color=LAYOUT_COLORS.get(layout_name, "#888888"),
               alpha=0.7)

    ax.set_xlabel('Пальцы', fontsize=12)
    ax.set_ylabel('Количество нажатий', fontsize=12)
    ax.set_title('Сравнение нагрузки на пальцы для разных раскладок', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(fingers, rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"График сохранён как {filename}")
    plt.show()


def plot_hand_distribution_pie(results: Dict[str, Dict[str, Any]], filename: str = None):
    n_layouts = len(results)
    if n_layouts == 0:
        return

    # Определяем размер сетки
    if n_layouts <= 3:
        cols = n_layouts
        rows = 1
    elif n_layouts <= 6:
        cols = 3
        rows = 2
    else:
        cols = 4
        rows = 2

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))
    if n_layouts == 1:
        axes = np.array([axes])
    axes = axes.flatten()

    for idx, (layout_name, data) in enumerate(results.items()):
        if idx >= len(axes):
            break
        if not data:
            continue

        ax = axes[idx]
        sizes = [data["left_percent"], data["right_percent"], data["both_hands_percent"]]
        labels = [f'Левая: {sizes[0]:.1f}%',
                  f'Правая: {sizes[1]:.1f}%',
                  f'Двуеручие: {sizes[2]:.1f}%']
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']

        wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                          startangle=90, textprops={'fontsize': 9})

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax.set_title(f'{LAYOUT_NAMES.get(layout_name, layout_name)}\n', fontsize=11, fontweight='bold')

    for idx in range(len(results), len(axes)):
        axes[idx].set_visible(False)

    plt.suptitle('Распределение нагрузки на руки (левая/правая/двуеручие)',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Круговые диаграммы сохранены как {filename}")
    plt.show()


def plot_penalties_comparison(results: Dict[str, Dict[str, Any]], filename: str = None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    layouts = []
    penalties = []
    penalty_per_char = []
    colors = []

    for layout_name, data in results.items():
        if not data:
            continue
        layouts.append(LAYOUT_NAMES.get(layout_name, layout_name))
        penalties.append(data["penalties"])
        penalty_per_char.append(data["penalty_per_char"] * 100)  # В процентах
        colors.append(LAYOUT_COLORS.get(layout_name, "#888888"))

    # График 1: Общие штрафы
    bars1 = ax1.bar(layouts, penalties, color=colors, alpha=0.7)
    ax1.set_xlabel('Раскладка', fontsize=12)
    ax1.set_ylabel('Общее количество штрафов', fontsize=12)
    ax1.set_title('Штрафы за смещение пальцев', fontsize=13, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)

    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2., height + max(penalties) * 0.01,
                 f'{int(height)}', ha='center', va='bottom', fontsize=9)

    # График 2: Штрафы на символ
    bars2 = ax2.bar(layouts, penalty_per_char, color=colors, alpha=0.7)
    ax2.set_xlabel('Раскладка', fontsize=12)
    ax2.set_ylabel('Штрафов на 100 символов (%)', fontsize=12)
    ax2.set_title('Относительные штрафы (на символ)', fontsize=13, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2., height + max(penalty_per_char) * 0.01,
                 f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"График штрафов сохранён как {filename}")
    plt.show()


def plot_convenient_rolls_comparison(results: Dict[str, Dict[str, Any]], filename: str = None):
    """Строит график сравнения удобных переборов."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    layouts = []
    rolls = []
    rolls_per_char = []
    colors = []

    for layout_name, data in results.items():
        if not data:
            continue
        layouts.append(LAYOUT_NAMES.get(layout_name, layout_name))
        rolls.append(data["convenient_rolls"])
        rolls_per_char.append(data["rolls_per_char"] * 100)  # В процентах
        colors.append(LAYOUT_COLORS.get(layout_name, "#888888"))

    # График 1: Общие удобные переборы
    bars1 = ax1.bar(layouts, rolls, color=colors, alpha=0.7)
    ax1.set_xlabel('Раскладка', fontsize=12)
    ax1.set_ylabel('Количество удобных переборов', fontsize=12)
    ax1.set_title('Удобные переборы (последовательности)', fontsize=13, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)

    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2., height + max(rolls) * 0.01,
                 f'{int(height)}', ha='center', va='bottom', fontsize=9)

    # График 2: Удобные переборы на символ
    bars2 = ax2.bar(layouts, rolls_per_char, color=colors, alpha=0.7)
    ax2.set_xlabel('Раскладка', fontsize=12)
    ax2.set_ylabel('Переборов на 100 символов (%)', fontsize=12)
    ax2.set_title('Относительные удобные переборы (на символ)', fontsize=13, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2., height + max(rolls_per_char) * 0.01,
                 f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"График переборов сохранён как {filename}")
    plt.show()


def plot_summary_radar(results: Dict[str, Dict[str, Any]], filename: str = None):
    if len(results) < 2:
        print("Для радиальной диаграммы нужно минимум 2 раскладки")
        return

    # Нормализуем метрики
    metrics = ['left_percent', 'penalty_per_char', 'rolls_per_char']
    metric_names = ['Левая рука (%)', 'Штрафы/символ', 'Переборы/символ']

    # Инвертируем штрафы
    normalized_data = {}
    for layout_name, data in results.items():
        if not data:
            continue
        # Для левой руки
        left_score = 1 - abs(data['left_percent'] - 50) / 50

        max_penalty = max(d['penalty_per_char'] for d in results.values() if d)
        penalty_score = 1 - (data['penalty_per_char'] / max_penalty if max_penalty > 0 else 0)

        max_rolls = max(d['rolls_per_char'] for d in results.values() if d)
        rolls_score = data['rolls_per_char'] / max_rolls if max_rolls > 0 else 0

        normalized_data[layout_name] = [left_score, penalty_score, rolls_score]

    # Углы для осей
    angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
    angles += angles[:1]  # Замыкаем круг

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    for layout_name, scores in normalized_data.items():
        values = scores + scores[:1]  # Замыкаем круг
        ax.plot(angles, values, 'o-', linewidth=2,
                label=LAYOUT_NAMES.get(layout_name, layout_name),
                color=LAYOUT_COLORS.get(layout_name, "#888888"))
        ax.fill(angles, values, alpha=0.1, color=LAYOUT_COLORS.get(layout_name, "#888888"))

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metric_names, fontsize=12)
    ax.set_ylim(0, 1)
    ax.set_title('Сравнительный анализ раскладок (нормализованные метрики)\n',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    ax.grid(True)

    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Радиальная диаграмма сохранена как {filename}")
    plt.show()


def print_statistics_table(results: Dict[str, Dict[str, Any]], text_name: str = ""):
    print(f"\n{'=' * 80}")
    print(f"СТАТИСТИКА РАСКЛАДОК {text_name}")
    print('=' * 80)

    headers = ["Раскладка", "Левая рука", "Правая рука", "Двуеручие", "Штрафы", "Штраф/симв", "Переборы", "Пер/симв"]
    print(
        f"{headers[0]:<20} {headers[1]:<10} {headers[2]:<10} {headers[3]:<10} {headers[4]:<8} {headers[5]:<10} {headers[6]:<10} {headers[7]:<10}")
    print("-" * 100)

    for layout_name, data in results.items():
        if not data:
            continue

        print(f"{LAYOUT_NAMES.get(layout_name, layout_name):<20} "
              f"{data['left_percent']:<10.1f} "
              f"{data['right_percent']:<10.1f} "
              f"{data['both_hands_percent']:<10.1f} "
              f"{data['penalties']:<8.0f} "
              f"{data['penalty_per_char'] * 100:<10.2f} "
              f"{data['convenient_rolls']:<10.0f} "
              f"{data['rolls_per_char'] * 100:<10.2f}")

    print('=' * 80)


def compare_layouts_interactive():
    print("=" * 60)
    print("СРАВНЕНИЕ РАСКЛАДОК КЛАВИАТУР")
    print("=" * 60)

    # Загружаем тексты
    texts = load_text_files()

    if not any(texts.values()):
        print("Нет доступных текстов для анализа!")
        return

    # Выбор текста
    print("\nДоступные тексты:")
    text_options = []
    for i, (name, content) in enumerate(texts.items(), 1):
        if content:
            text_options.append(name)
            print(f"{i}. {name} ({len(content):,} символов)")

    if not text_options:
        print("Нет текстов для анализа!")
        return

    try:
        choice = int(input(f"\nВыберите текст (1-{len(text_options)}): ")) - 1
        if 0 <= choice < len(text_options):
            text_name = text_options[choice]
            text = texts[text_name]
        else:
            print("Неверный выбор, используем первый доступный текст")
            text_name = text_options[0]
            text = texts[text_name]
    except:
        print("Неверный ввод, используем первый доступный текст")
        text_name = text_options[0]
        text = texts[text_name]

    print(f"\nВыбран текст: {text_name} ({len(text):,} символов)")

    print("\nДоступные раскладки:")
    all_layouts = list(LAYOUT_NAMES.keys())
    for i, layout in enumerate(all_layouts, 1):
        print(f"{i}. {LAYOUT_NAMES[layout]}")
    print(f"{len(all_layouts) + 1}. Все раскладки")

    selected_layouts = []
    try:
        choices = input("\nВыберите раскладки через запятую (например: 1,3,5) или 'все': ").strip()
        if choices.lower() == 'все':
            selected_layouts = all_layouts
        else:
            indices = [int(x.strip()) - 1 for x in choices.split(',')]
            selected_layouts = [all_layouts[i] for i in indices if 0 <= i < len(all_layouts)]
    except:
        print("Неверный ввод, используем все раскладки")
        selected_layouts = all_layouts

    if not selected_layouts:
        selected_layouts = all_layouts

    print(f"\nСравниваем раскладки: {', '.join([LAYOUT_NAMES[l] for l in selected_layouts])}")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ТЕКСТА...")
    print("=" * 60)

    results = {}
    for layout_name in selected_layouts:
        print(f"Анализ {LAYOUT_NAMES[layout_name]}...", end=' ', flush=True)
        results[layout_name] = analyze_text(text, layout_name)
        print("✓")

    print_statistics_table(results, f"({text_name})")

    print("\n" + "=" * 60)
    print("СОЗДАНИЕ ГРАФИКОВ...")
    print("=" * 60)

    os.makedirs("графики", exist_ok=True)
    base_filename = f"графики/{text_name}_"

    # 1. Нагрузка на пальцы
    print("1. График нагрузки на пальцы...")
    plot_finger_load_comparison(results, base_filename + "нагрузка.png")

    # 2. Круговые диаграммы для рук
    print("2. Круговые диаграммы распределения нагрузки...")
    plot_hand_distribution_pie(results, base_filename + "руки.png")

    # 3. Штрафы
    print("3. График сравнения штрафов...")
    plot_penalties_comparison(results, base_filename + "штрафы.png")

    # 4. Удобные переборы
    print("4. График удобных переборов...")
    plot_convenient_rolls_comparison(results, base_filename + "переборы.png")

    # 5. Радиальная диаграмма
    if len(results) >= 2:
        print("5. Радиальная диаграмма сравнения...")
        plot_summary_radar(results, base_filename + "радар.png")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН!")
    print(f"Графики сохранены в папке 'графики/'")
    print("=" * 60)


def main():
    while True:
        print("\n" + "=" * 60)
        print("СРАВНЕНИЕ РАСКЛАДОК КЛАВИАТУР")
        print("=" * 60)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 60)
        print("1. Сравнить раскладки на одном тексте")
        print("2. Выйти")
        print("-" * 60)

        choice = input("Выберите действие (1-2): ").strip()

        if choice == "1":
            compare_layouts_interactive()
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

        input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['font.family'] = 'DejaVu Sans'  # Для поддержки кириллицы
    plt.rcParams['axes.unicode_minus'] = False

    main()