import json
import os
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange

# 📁 Путь к файлам
folder_path = r"C:\"
input_file = os.path.join(folder_path, "september.json")
output_file = os.path.join(folder_path, "september_new.json")

# 🧠 Поддерживаемые форматы дат
date_patterns = [
    (re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$"), "%Y-%m-%d %H:%M"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "%Y-%m-%d"),
    (re.compile(r"^\d{4}-\d{2}$"), "%Y-%m"),
    (re.compile(r"^\d{2}\.\d{4}$"), "%m.%Y"),  # добавили MM.YYYY
]

# 📅 Безопасное добавление одного месяца
def safe_add_month(dt):
    year = dt.year
    month = dt.month + 1
    if month > 12:
        month = 1
        year += 1
    day = min(dt.day, monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)

# 🌀 Сдвиг строки с датой, если формат подходит
def shift_date_str(value):
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

# 🔁 Рекурсивное обновление
def update_dates(obj):
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

# 📥 Загрузка исходного JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# ⚙️ Обработка
updated_data = update_dates(data)

# 💾 Сохранение результата
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(updated_data, f, indent=4, ensure_ascii=False)

print(f"✅ Обновлённый файл сохранён в: {output_file}")