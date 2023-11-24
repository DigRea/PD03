# JH - Джими Хендрикс - 27.11.1942
# OO - Оззи Осборн - 03.12.1948
# PM - Пол Маккартни - 18.06.1942
# EC - Эрик Клэптон - 30.03.1945
# BM - Брайан Мэй - 19.07.1947
# PC - Фил Коллинз - 30.01.1951
# VV - Вилле Вало - 22.11.1976
# JF - Джон Фогерти - 28.05.1945
# ST - Стив Тайлер - 26.03.1948
# JL - Джефф Линн - 30.12.1947

people = {'Джими Хендрикс':'27.11.1942', 'Оззи Осборн':'03.12.1948', 'Пол Маккартни':'18.06.1942', 'Эрик Клэптон':'30.03.1945', 'Брайан Мэй':'19.07.1947', 'Фил Коллинз':'30.01.1951', 'Вилле Вало':'22.11.1976', 'Джон Фогерти':'28.05.1945', 'Стив Тайлер':'26.03.1948', 'Джефф Линн':'30.12.1947'}
dates = {'двадцать седьмое ноября 1942':'27.11.1942', 'третье декабря 1948':'03.12.1948', 'восемнадцатое июня 1942':'18.06.1942', 'тридцатое марта 1945':'30.03.1945', 'девятнадцатое июля 1947':'19.07.1947', 'тридцатое января 1951':'30.01.1951', 'двадцать второе ноября 1976':'22.11.1976', 'двадцать восьмое мая 1945':'28.05.1945', 'двадцать шестое марта 1948':'26.03.1948', 'тридцатое декабря 1047':'30.12.1947'}

import random

while True:

    selection = random.sample(list(people.keys()), k=5)
    right = 0
    wrong = 0
    print()
    for i in range(len(selection)):
        person = input(f'Введите дату рождения следующего музыканта:\n{selection[i]}: ')
        if person != people.get(selection[i]):
            #answer =
            print('Неверно! Правильнвй ответ - ', )
            wrong += 1
        else:
            right += 1

    print()
    print('Количество правильных ответов: ', right)
    print('Количество неправильных ответов: ', wrong)

    if input('Хотите начать игру сначала? ') != 'да':
        break
