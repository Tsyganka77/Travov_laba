"""
Считывает количество нажатий и показывает результат в красивом графическом окне
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from function import (
    count_finger_load_qwerty,
    count_finger_load_vyzov,
    load_hand_left,
    load_hand_right,
    calculate_penalties,
    calculate_penalties_vyzov
)

def format_finger_data(d):
    """Преобразует словарь нажатий в читаемый многострочный текст."""
    lines = []
    for finger, count in d.items():
        lines.append(f"  • {finger}: {count}")
    return "\n".join(lines)

def main():
    # Чтение текста
    try:
        with open('voina_i_mir.txt', "r", encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        tk.messagebox.showerror("Ошибка", "Файл 'voina_i_mir.txt' не найден!")
        return

    # Подсчёт данных
    qwerty_finger_load = count_finger_load_qwerty(text)
    vyzov_finger_load = count_finger_load_vyzov(text)
    left_qwerty = load_hand_left(qwerty_finger_load)
    right_qwerty = load_hand_right(qwerty_finger_load)
    left_vyzov = load_hand_left(vyzov_finger_load)
    right_vyzov = load_hand_right(vyzov_finger_load)
    penalties_qwerty = calculate_penalties(text)
    penalties_vyzov = calculate_penalties_vyzov(text)

    # Формирование данных для отображения
    fing = [
        'левый мизинец', 'левый безымянный', 'левый средний',
        'левый указательный', 'левый большой',
        'правый большой', 'правый указательный',
        'правый средний', 'правый безымянный', 'правый мизинец'
    ]
    fing_d_qwerty = dict(zip(fing, qwerty_finger_load))
    fing_d_vyzov = dict(zip(fing, vyzov_finger_load))

    # === Создание окна ===
    root = tk.Tk()
    root.title("Анализ клавиатурных раскладок")
    root.geometry("720x780")
    root.minsize(600, 600)
    root.configure(bg="#f0f0f0")  # Светлый фон окна

    # Используем современную тему ttk
    style = ttk.Style()
    if "clam" in style.theme_names():
        style.theme_use("clam")

    # Заголовок
    title_label = ttk.Label(
        root,
        text="Анализ эргономики раскладок на основе «Война и мир»",
        font=("Segoe UI", 16, "bold"),
        background="#f0f0f0",
        foreground="#2c3e50",
        anchor="center"
    )
    title_label.pack(pady=(15, 10))

    # Основной контейнер с прокруткой
    canvas = tk.Canvas(root, bg="#f0f0f0", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=20, pady=(0, 20))
    scrollbar.pack(side="right", fill="y")

    # === Блок: ЙЦУКЕН ===
    qwerty_frame = ttk.Frame(scrollable_frame)
    qwerty_frame.pack(fill="x", padx=10, pady=(0, 20))

    ttk.Label(
        qwerty_frame,
        text="Раскладка ЙЦУКЕН",
        font=("Segoe UI", 13, "bold"),
        foreground="#2980b9"
    ).pack(anchor="w", padx=10, pady=(10, 8))

    # Статистика в виде карточек
    stats_frame = tk.Frame(qwerty_frame, bg="white")
    stats_frame.pack(fill="x", padx=15, pady=5)

    for label, value, color in [
        ("Левая рука", f"{left_qwerty}%", "#d6eaf8"),
        ("Правая рука", f"{right_qwerty}%", "#d6eaf8"),
        ("Штрафы", str(penalties_qwerty), "#aed6f1")
    ]:
        box = tk.Frame(stats_frame, bg=color, relief="flat", highlightbackground="#85c1e9", highlightthickness=1)
        box.pack(side="left", padx=8, ipadx=14, ipady=10)
        tk.Label(box, text=value, font=("Segoe UI", 14, "bold"), bg=color, fg="#1a5276").pack()
        tk.Label(box, text=label, font=("Segoe UI", 9), bg=color, fg="#2874a6").pack()

    # Нажатия пальцами
    tk.Label(qwerty_frame, text="Нажатия пальцами:", font=("Segoe UI", 10, "bold"), bg="white", anchor="w", padx=15).pack(anchor="w", padx=15, pady=(10, 0))
    text_qwerty = tk.Text(
        qwerty_frame, height=10, font=("Consolas", 10),
        bg="#fafafa", relief="flat", padx=15, pady=10
    )
    text_qwerty.pack(fill="x", padx=15, pady=(0, 10))
    text_qwerty.insert("1.0", format_finger_data(fing_d_qwerty))
    text_qwerty.config(state="disabled")

    # === Блок: ВЫЗОВ ===
    vyzov_frame = ttk.Frame(scrollable_frame)
    vyzov_frame.pack(fill="x", padx=10, pady=(0, 20))

    ttk.Label(
        vyzov_frame,
        text="Раскладка ВЫЗОВ",
        font=("Segoe UI", 13, "bold"),
        foreground="#8e44ad"
    ).pack(anchor="w", padx=10, pady=(10, 8))

    stats_frame2 = tk.Frame(vyzov_frame, bg="white")
    stats_frame2.pack(fill="x", padx=15, pady=5)

    for label, value, color in [
        ("Левая рука", f"{left_vyzov}%", "#f4ecf7"),
        ("Правая рука", f"{right_vyzov}%", "#f4ecf7"),
        ("Штрафы", str(penalties_vyzov), "#e8daef")
    ]:
        box = tk.Frame(stats_frame2, bg=color, relief="flat", highlightbackground="#d2b4de", highlightthickness=1)
        box.pack(side="left", padx=8, ipadx=14, ipady=10)
        tk.Label(box, text=value, font=("Segoe UI", 14, "bold"), bg=color, fg="#7d3c98").pack()
        tk.Label(box, text=label, font=("Segoe UI", 9), bg=color, fg="#6c3483").pack()

    tk.Label(vyzov_frame, text="Нажатия пальцами:", font=("Segoe UI", 10, "bold"), bg="white", anchor="w", padx=15).pack(anchor="w", padx=15, pady=(10, 0))
    text_vyzov = tk.Text(
        vyzov_frame, height=10, font=("Consolas", 10),
        bg="#fafafa", relief="flat", padx=15, pady=10
    )
    text_vyzov.pack(fill="x", padx=15, pady=(0, 10))
    text_vyzov.insert("1.0", format_finger_data(fing_d_vyzov))
    text_vyzov.config(state="disabled")

    # Поддержка прокрутки колесом мыши
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    root.mainloop()

if __name__ == "__main__":
    main()
