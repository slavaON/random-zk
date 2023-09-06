# Исходные данные в формате "дата имя"
data = {
    "max": "28.авг",
    "aleks": "30.авг",
    "aza": "31.авг",
    "acc7": "25.авг",
    "acc11": "31.авг",
    "acc12": "24.авг",
    "main": "28.авг",
    "hasanov": "31.авг",
    "demys": "31.авг",
    "petilo": "30.авг",
    "achmedova": "31.авг",
    "khamidova": "30.авг",
    "acc 6": "30.авг",
    "acc 8": "31.авг",
    "acc 9": "31.авг",
    "acc 10": "23.авг",
    "acc13": "30.авг",
    "acc14": "31.авг",
    "acc15": "28.авг",
    "acc16": "30.авг",
    "acc17": "01.авг",
    "acc18": "31.авг",
    "acc19": "31.авг",
    "acc20": "31.авг",
    "acc21": "31.авг",
    "acc22": "02.авг",
    "acc23": "02.авг",
    "acc24": "02.авг",
    "acc25": "02.авг",
    "acc26": "23.авг",
    "acc27": "30.авг",
    "acc28": "24.авг",
    "acc29": "16.авг",
    "acc30": "27.авг",
    "acc31": "19.июль",
    "acc32": "22.авг",
    "acc33": "27.июль",
    "acc34": "29.июль",
    "acc35": "24.авг",
    "acc36": "28.авг",
    "acc37": "21.авг",
    "acc38": "31.авг",
    "acc39": "31.авг",
    "acc40": "30.июль",
    "acc41": "30.июль",
    "acc42": "30.июль",
    "acc43": "02.авг",
    "acc44": "03.авг",
    "acc45": "04.авг",
    "acc46": "30.июль",
    "acc47": "01.авг",
    "acc48": "03.сент",
    "acc49": "19.июль",
    "acc50": "04.авг",
    "acc51": "20.авг",
    "acc52": "22.авг",
    "acc53": "04.авг",
    "acc54": "04.авг",
    "acc55": "10.авг",
    "acc56": "16.авг",
    "acc57": "10.авг",
    "acc58": "20.авг",
    "acc59": "16.авг",
    "acc60": "16.авг",
    "acc61": "20.авг",
    "acc62": "18.авг",
    "acc63": "21.авг",
    "acc64": "21.авг",
    "acc65": "21.авг",
    "acc66": "27.авг",
    "acc67": "27.авг",
    "acc68": "21.авг",
    "acc69": "27.авг",
    "acc70": "21.авг",
    "acc71": "30.июль",
    "acc72": "30.июль",
    "acc73": "05.сент",
    "acc74": "04.авг",
    "acc75": "27.авг",
    "acc76": "04.авг",
    "acc77": "05.авг",
    "acc78": "05.авг",
    "acc79": "05.авг",
    "acc 80": "06.авг",
    "acc 81": "07.авг",
    "acc 82": "07.авг",
    "acc 83": "08.авг",
    "acc 84": "10.авг",
    "acc 85": "11.авг",
    "acc 86": "11.авг",
    "acc 87": "12.авг",
    "acc 88": "12.авг",
    "acc 89": "12.авг",
    "acc 90": "12.авг",
    "acc 91": "13.авг",
    "acc 92": "14.авг",
    "acc 93": "18.авг",
    "acc 94": "20.авг",
    "acc 95": "20.авг",
    "acc 96": "20.авг",
    "acc 97": "28.авг"
}


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
