def z1():
    a = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон",
         "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
         "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София",
         "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
         "Северная Македония": "Скопье", "Сербия": "Белград"}

    print(a)
    x = input(str("Введите страну: "))
    if x in a:
        print("Столица - ", a[x])
        for key in sorted(a):
            print(key, '- Столица', a[key])


def z2():
    alph = {
        "авеинорст": 1,
        "дклмуп": 2,
        "бгёья": 3,
        "йы": 4,
        "жзхцч": 5,
        "шэю": 8,
        "фщъ": 10
    }
    s = 0
    word = input("Введите слово: ")
    for i in word:
        for key, value in alph.items():
            if i in key:
                s += value

    print("Сумма: ", s)


def z3():
    from random import randint

    group = {"Пахомов": [],
             "Шарин": [],
             "Капитонов": [],
             "Николаев": [],
             "Иванов": [], }
    lang = ['Якутский', 'Английский', 'Русский', 'Китайский', 'Французский', 'Японский']
    for student in group:  # для переменной в словаре студентов
        randstudent = randint(0, 4)  # вычисляем рандомное число
        for i in range(randstudent):  # для индекса ай - 0 1 2 3 4
            randlang = randint(0, 5)
            if lang[randlang] not in group[student]:  # Проверка на уникальнос;'[ть значений в списке языков студента
                group[student].append(lang[randlang])  # Добавление языка в список
    print(group)  # весь цикл для того, чтобы заполнить словарь случайными значениями из списка
    s = []
    student_counter = 0  # добавление счетчика
    for language in lang:
        for student in group:
            if language in group[student] and language not in s:
                s.append(language)
    print(f"Различные языки: {sorted(s)}")
    print(f'Количество языков: {len(s)}')
    ch = []
    for student in group:
        if 'Китайский' in group[student]:
            ch.append(student)
    print("Студенты, знающие китайский: ", ch)


z1()
z2()
z3()