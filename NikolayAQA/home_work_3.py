# import math
#
# size = int(input('Укажите размер файла для скачивания: '))
# speed = int(input('Какова скорость вашего соединения в МБ/с: '))
#
# downloaded = 0
# sec = 0
#
# while downloaded < size:
#     sec += 1
#     downloaded += speed
#     if downloaded > size:
#         downloaded = size
#     percent = math.ceil((downloaded / size) * 100)
#     print(f'Прошло {sec} сек. Скачано {downloaded} из {size} МБ ({percent}%)')
#
# print(f'Скачивание завершено за {sec} сек.')

# `````````````````Дз```````````````````````#

# import math
#
# size = int(input('Укажите размер файла для скачивания: '))
# speed = int(input('Какова скорость вашего соединения в МБ/с: '))
#
# total_seconds = math.ceil(size / speed)
#
# for sec in range(1, total_seconds + 1):
#     downloaded = speed * sec
#     if downloaded > size:
#         downloaded = size
#     percent = math.ceil((downloaded / size) * 100)
#     print(f'Прошло {sec} сек. Скачано {downloaded} из {size} МБ ({percent}%)')

# `````````````````Дз```````````````````````#

# x = float(input("Введите положительное действительное число X: "))
#
# fractional_part = x % 1
#
# first_decimal_digit = int(fractional_part * 10)
#
# print("Первая цифра после десятичной точки:", first_decimal_digit)

# `````````````````Дз```````````````````````#

# import math
#
# r = float(input("Введите радиус случайной планеты: "))
# v = (4 / 3) * math.pi * (r ** 3)
# earth_volume = 1.08321 * 10 ** 12
#
# ratio = earth_volume / v
#
# if ratio > 1:
#     print(f"Объём планеты Земля больше в {round(ratio, 3)} раз")
# else:
#     print(f"Объём планеты Земля меньше в {round(1 / ratio, 3)} раз")

# `````````````````Дз```````````````````````#

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# maximum = (a + b + abs(a - b)) // 2
#
# print("Наибольшее число:", maximum)

# `````````````````Дз```````````````````````#

# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#
#
# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting
#     print('Следующий.\n')

# `````````````````Дз```````````````````````#

# def que_sum():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
#
# print("Сколько мешков рыбы и мяса?")
# que_sum()
#
# print("Сколько буханок белого и чёрного хлеба?")
# que_sum()
#
# print("Сколько вёдер воды и молока?")
# que_sum()

# `````````````````Дз```````````````````````#

# def person():
#     print("Фамилия: Иванов")
#     print("Имя: Василий")
#     print("Улица: Пушкина")
#     print("Дом: 32")
#     print()
#
# person()
# person()
# person()
# person()

# `````````````````Дз```````````````````````#

# def wather(price):
# 	print('КлирВотер')
# 	print('ВодЗавод')
# 	print(price)
# 	print()
#
# wather('25')
# wather('30')
# wather('40')

# `````````````````Дз```````````````````````#

# import math
#
# radius = float(input("Введите радиус планеты: "))
#
# def sphereArea():
#     s = 4 * math.pi * (radius ** 2)
#     print(f"Площадь поверхности планеты: {s} км²")
#
# def sphereVolume():
#     v = (4 / 3) * math.pi * (radius ** 3)
#     print(f"Объём планеты: {v} км³")
#
# sphereArea()
# sphereVolume()

# `````````````````Дз```````````````````````#

# def isPrime(num):
#     if num < 2:
#         print(f"{num} — не простое число")
#     else:
#         i = 2
#         while i * i <= num:
#             if num % i == 0:
#                 print(f"{num} — не простое число")
#                 break
#             i += 1
#         else:
#             print(f"{num} — простое число")
#
# N = int(input("Сколько чисел вы хотите проверить? "))
#
# for _ in range(N):
#     number = int(input("Введите число: "))
#     isPrime(number)

# `````````````````Дз```````````````````````#

# def mid_num():
#     first_num = int(input('Введите левую границу: '))
#     second_num = int(input('Введите правую границу: '))
#
#     if first_num < second_num:
#         count = second_num - first_num + 1
#         total = (first_num + second_num) * count / 2
#         average = total / count
#         print('Среднее:', average)
#     else:
#         print('Ошибка: первое число должно быть меньше второго.')
#
# mid_num()

# `````````````````Дз```````````````````````#

# def mail(surname, name, country, town, street, home, door):
#     print('Фамилия:', surname)
#     print('Имя:', name)
#     print('Страна:', country)
#     print('Город:', town)
#     print('Улица:', street)
#     print('Дом:', home)
#     print('Квартира:', door)
#     print()
#
# mail('Пупкин', 'Вася', 'Бангладеш', 'Где-то', 'Ж', 10, 15)
# mail('Иванов', 'Пётр', 'Россия', 'Москва', 'Ленина', 5, 8)
# mail('Смирнова', 'Анна', 'Казахстан', 'Алматы', 'Абая', 21, 3)

# `````````````````Дз```````````````````````#

# import math
#
# def myDistance(x, y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print("Расстояние до точки от начала координат:", distance)
#
# def betweenDistance(x1, y1, x2, y2):
#     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     print("Расстояние между двумя точками:", distance)
#
# choice = int(input('Выберите действие:\n1 - расстояние до точки\n2 - расстояние между двумя точками\nВаш выбор: '))
#
# if choice == 1:
#     x = float(input('Введите координату x: '))
#     y = float(input('Введите координату y: '))
#     myDistance(x, y)
#
# elif choice == 2:
#     x1 = float(input('Введите координату x1: '))
#     y1 = float(input('Введите координату y1: '))
#     x2 = float(input('Введите координату x2: '))
#     y2 = float(input('Введите координату y2: '))
#     betweenDistance(x1, y1, x2, y2)
# else:
#     print('Ошибка ввода: выберите 1 или 2')
