import itertools

# Ваши данные
data = [
    "01.авг acc17 + 2trx",
    "01.авг acc18 + 2trx",
    "01.авг acc19",
    "01.авг acc20",
    "01.авг acc21 + 2trx",
    "02.авг acc22",
    "02.авг acc23",
    "02.авг acc24 + 2trx",
    "02.авг acc42",
    "03.авг acc44  + 2trx",
    "03.сент acc48",
    "04.авг acc45   + 2trx",
    "04.авг acc50",
    "04.авг acc53 + 2trx",
    "04.авг acc54  + 2trx",
    "05.авг acc73",
    "05.авг acc76 + 2trx",
    "05.авг acc77 + 2trx",
    "05.авг acc78",
    "05.авг acc79 + light 2trx",
    "06.авг acc80  + light 2trx",
    "07.авг acc81",
    "07.авг acc82",
    "08.авг acc83 + 2trx",
    "10.авг acc55 + 2trx",
    "10.авг acc57 + 2trx",
    "10.авг acc84 + 2trx",
    "11.авг acc85 + 2trx",
    "12.авг acc86",
    "12.авг acc87 + 2 trx",
    "12.авг acc88",
    "12.авг acc89",
    "13.авг acc90",
    "14.авг acc91  + light 2trx",
    "14.авг acc92  + light 2trx",
    "16.авг acc29",
    "16.авг acc56  + light 2trx",
    "16.авг acc59 + 2trx",
    "16.авг acc60 + 2trx",
    "18.авг acc62 + 2trx",
    "18.авг acc65",
    "18.авг acc66 + 2trx",
    "18.авг acc67 + 2trx",
    "18.авг acc68  + 2trx",
    "19.июль acc31",
    "19.июль acc34",
    "20.авг acc51",
    "20.авг acc58 + trx",
    "20.авг acc61 + 2trx",
    "20.авг acc93 + 2trx",
    "20.авг acc94 + 2trx",
    "20.авг acc95",
    "21.авг acc35",
    "21.авг acc37",
    "21.авг acc63",
    "21.авг acc64  + 2trx",
    "21.авг acc69 + 2trx",
    "22.авг acc32",
    "22.авг acc52",
    "23.авг acc10",
    "23.авг acc25",
    "24.авг acc12",
    "24.авг acc22",
    "24.авг acc27 + 2trx",
    "24.авг acc28 + 2trx",
    "24.авг acc35",
    "25.авг acc7",
    "26.июль acc30 + 2trx",
    "27.июль acc33 + 2trx",
    "27.июль acc34",
    "27.авг acc65",
    "27.авг acc66 + 2trx",
    "27.авг acc67 + 2trx",
    "27.авг acc68  + 2trx",
    "27.авг acc69 + 2trx",
    "27.авг acc75",
    "28.авг max",
    "28.авг main",
    "28.авг acc15",
    "28.авг acc97 + 2trx",
    "29.июль acc32",
    "29.июль acc34",
    "29.авг acc65",
    "29.авг acc66 + 2trx",
    "29.авг acc67 + 2trx",
    "29.авг acc68  + 2trx",
    "29.авг acc69 + 2trx",
    "30.июль acc30 + 2trx",
    "30.июль acc40",
    "30.июль acc41",
    "30.июль acc42",
    "30.июль acc46",
    "30.июль acc70",
    "30.июль acc71",
    "30.июль acc72",
    "30.июль acc79 + light 2trx",
    "30.авг aleks",
    "30.авг petilo",
    "30.авг khamidova",
    "30.авг acc6",
    "30.авг acc13",
    "30.авг acc16",
    "30.авг acc25",
    "31.авг aza",
    "31.авг acc11",
    "31.авг hasanov",
    "31.авг acc17 + 2trx",
    "31.авг acc18 + 2trx",
    "31.авг acc19",
    "31.авг acc20",
    "31.авг acc21 + 2trx",
    "31.авг acc38",
    "31.авг acc39",
    "31.авг acc97 + 2trx",
]

# Функция для разделения данных на группы
def split_into_groups(data):
    # Сортировка данных по дате
    sorted_data = sorted(data, key=lambda x: x.split()[0])

    # Разделение данных на группы
    groups = []
    current_group = []
    for item in sorted_data:
        if not current_group:
            current_group.append(item)
        else:
            last_date = current_group[-1].split()[0]
            item_date = item.split()[0]
            if abs(int(last_date.split(".")[0]) - int(item_date.split(".")[0])) > 7:
                groups.append(current_group)
                current_group = [item]
            else:
                current_group.append(item)
    groups.append(current_group)
    
    return groups

# Вызов функции и вывод результатов
groups = split_into_groups(data)

# Вывод групп в формате YAML
for i, group in enumerate(groups):
    print(f"Группа {i + 1}:")
    for item in group:
        print(f"- {item}")
