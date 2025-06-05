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
