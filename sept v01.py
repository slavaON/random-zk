# Исходные данные в формате "дата имя"
data = [
    # Вставьте ваши данные сюда
]

# Преобразование данных в список кортежей (дата, имя)
data_tuples = [(entry.split()[0], entry.split()[1]) for entry in data]

# Сортировка данных по дате
sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])

# Создание словаря, где ключ - дата, значение - список имен
date_to_names = {}
for date, name in sorted_data_tuples:
    if date not in date_to_names:
        date_to_names[date] = [name]
    else:
        date_to_names[date].append(name)

# Группировка данных
groups = []
current_group = []
current_dates = set()

for date, names in date_to_names.items():
    if not current_dates.intersection(set([date])) and len(current_group) < 4:
        current_group.extend([(date, name) for name in names])
        current_dates.add(date)
    else:
        if current_group:
            groups.append(current_group)
        current_group = [(date, name) for name in names]
        current_dates = {date}

# Добавление последней группы
if current_group:
    groups.append(current_group)

# Вывод групп
for i, group in enumerate(groups, start=1):
    print(f"Группа {i}:")
    for date, name in group:
        print(f"{date} {name}")
    print()
