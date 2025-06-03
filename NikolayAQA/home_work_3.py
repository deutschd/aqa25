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

