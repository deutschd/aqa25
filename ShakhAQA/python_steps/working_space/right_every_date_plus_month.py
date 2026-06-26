# import json
# import os
# import re
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# from calendar import monthrange
#
# # 📁 Путь к файлам
# folder_path = r"D:\OCTOBANK\SPR_Tasks"
# input_file = os.path.join(folder_path, "53005050005092_new.json")
# output_file = os.path.join(folder_path, "53005050005092_new1.json")
#
# # 🧠 Поддерживаемые форматы дат
# date_patterns = [
#     (re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$"), "%Y-%m-%d %H:%M"),
#     (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
#     (re.compile(r"^\d{4}-\d{2}$"), "%Y-%m"),
#     (re.compile(r"^\d{2}\.\d{4}$"), "%m.%Y"),  # добавили MM.YYYY
# ]
#
# # 📅 Безопасное добавление одного месяца
# def safe_add_month(dt):
#     year = dt.year
#     month = dt.month + 1
#     if month > 12:
#         month = 1
#         year += 1
#     day = min(dt.day, monthrange(year, month)[1])
#     return dt.replace(year=year, month=month, day=day)
#
# # 🌀 Сдвиг строки с датой, если формат подходит
# def shift_date_str(value):
#     if not isinstance(value, str):
#         return value
#     for pattern, fmt in date_patterns:
#         if pattern.match(value):
#             try:
#                 dt = datetime.strptime(value, fmt)
#                 new_dt = safe_add_month(dt)
#                 return new_dt.strftime(fmt)
#             except Exception:
#                 return value
#     return value
#
# # 🔁 Рекурсивное обновление
# def update_dates(obj):
#     if isinstance(obj, dict):
#         return {
#             k: update_dates(
#                 shift_date_str(v) if (
#                     isinstance(v, str) and any(word in k.lower() for word in ["date", "period", "change"])
#                 ) else v
#             )
#             for k, v in obj.items()
#         }
#     elif isinstance(obj, list):
#         return [update_dates(item) for item in obj]
#     else:
#         return obj
#
# # 📥 Загрузка исходного JSON
# with open(input_file, "r", encoding="utf-8") as f:
#     data = json.load(f)
#
# # ⚙️ Обработка
# updated_data = update_dates(data)
#
# # 💾 Сохранение результата
# with open(output_file, "w", encoding="utf-8") as f:
#     json.dump(updated_data, f, indent=4, ensure_ascii=False)
#
# print(f"✅ Обновлённый файл сохранён в: {output_file}")





import json
import os
import re
from datetime import datetime
from calendar import monthrange

# GUI for choosing files + showing messages
import tkinter as tk
from tkinter import filedialog, messagebox


# 🧠 Поддерживаемые форматы дат
date_patterns = [
    (re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$"), "%Y-%m-%d %H:%M"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
    (re.compile(r"^\d{4}-\d{2}$"), "%Y-%m"),
    (re.compile(r"^\d{2}\.\d{4}$"), "%m.%Y"),  # MM.YYYY
]


def safe_add_month(dt: datetime) -> datetime:
    """Безопасно добавить один месяц, учитывая длину месяцев."""
    year = dt.year
    month = dt.month + 1
    if month > 12:
        month = 1
        year += 1
    day = min(dt.day, monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def shift_date_str(value):
    """Сдвигает дату в строке на +1 месяц, если формат поддерживается."""
    if not isinstance(value, str):
        return value
    for pattern, fmt in date_patterns:
        if pattern.match(value):
            try:
                dt = datetime.strptime(value, fmt)
                new_dt = safe_add_month(dt)
                return new_dt.strftime(fmt)
            except Exception:
                return value
    return value


def update_dates(obj):
    """Рекурсивно обходит JSON и сдвигает даты в ключах, содержащих date/period/change."""
    if isinstance(obj, dict):
        return {
            k: update_dates(
                shift_date_str(v) if (
                    isinstance(v, str) and any(word in k.lower() for word in ["date", "period", "change"])
                ) else v
            )
            for k, v in obj.items()
        }
    elif isinstance(obj, list):
        return [update_dates(item) for item in obj]
    else:
        return obj


def main():
    # Инициализация Tk (без лишнего окна)
    root = tk.Tk()
    root.withdraw()

    # Выбор входного файла
    input_file = filedialog.askopenfilename(
        title="📂 Выберите входной JSON",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if not input_file:
        messagebox.showwarning("Отмена", "Входной файл не выбран.")
        return

    # Предложить имя по умолчанию для сохранения
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    suggested_name = f"{base_name}_updated.json"

    # Куда сохранить результат
    output_file = filedialog.asksaveasfilename(
        title="💾 Сохранить обновлённый JSON как...",
        initialfile=suggested_name,
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")]
    )
    if not output_file:
        messagebox.showwarning("Отмена", "Файл для сохранения не выбран.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        messagebox.showerror("Ошибка чтения", f"Не удалось прочитать JSON:\n{e}")
        return

    try:
        updated_data = update_dates(data)
    except Exception as e:
        messagebox.showerror("Ошибка обработки", f"Ошибка при обновлении дат:\n{e}")
        return

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(updated_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Ошибка записи", f"Не удалось сохранить файл:\n{e}")
        return

    messagebox.showinfo("Готово", f"✅ Обновлённый файл сохранён:\n{output_file}")


if __name__ == "__main__":
    main()
