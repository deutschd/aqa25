# `````````````````Дз / gpt```````````````````````#
# N = 9  # Задайте значение N
# number = 1
# while number <= N:
#     cube = number ** 3
#     print(cube)
#     number += 1

# `````````````````Дз```````````````````````#
# number = 0
# while number >= 0 :
#     number += 1
#     cube = number ** 3
#     if number >= 9 :
#         break
#     print(cube)

# `````````````````Дз```````````````````````#
# name = input("Введите ваше имя :")
# debt = 13250
#
# print("Здравствуйте" , name , "Ваш долг составляет : " , debt)
#
#
# while debt > 0 :
#     deposit = int(input("Какую сумму желаете внести? :"))
#     debt -= deposit
#     if debt > 0 :
#         print("Оставшийся долг :", debt)
#     else :
#         print("Поздравляем" , name , "Ваш долг погашен , хорошего дня ! ")

# ````````````Дз на пополам с gpt````````````#
# number = int(input("Введите ваше число :"))
# ttl_digit = 0
#
# if number == 0:
#     ttl_digit = 1
# else:
#     while number > 0:
#         number //= 10
#         ttl_digit += 1
#
# print(ttl_digit)

# ````````````Дз на пополам с gpt````````````#
# number = int(input("Введите число: "))
#
# positive_numbers = 0
# negative_numbers = 0
#
# while number != 0:
#     if number > 0:
#         positive_numbers += 1
#     elif number < 0:
#         negative_numbers += 1
#
#     number = int(input("Введите число: "))
#
# print("Кол-во положительных чисел:", positive_numbers)
# print("Кол-во отрицательных чисел:", negative_numbers)

# ````````````Дз на пополам с gpt````````````#
# print("Начался восьмичасовой рабочий день.")
#
# work_hour = 1
# total_tasks = 0
# calls = 0
#
# while work_hour <= 8:
#     print(f"{work_hour}-й час")
#
#     tasks = int(input("Сколько задач решит Максим? "))
#     total_tasks += tasks
#
#     while True:
#         call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#         if call == 0 or call == 1:
#             break
#         else:
#             print("Ошибка ввода! Введите только 1 — да, 0 — нет.")
#
#     if call == 1:
#         calls += 1
#
#     work_hour += 1
#
# print("Рабочий день закончился. Всего выполнено задач:", total_tasks)
#
# if calls > 0:
#     print("Нужно зайти в магазин.")

# ````````````Дз на пополам с gpt````````````#
# deposit = 100000
# percent = 17
# expectations = 500000
#
# years = 0
#
# while deposit < expectations:
#     deposit += int(deposit * (percent / 100))
#     years += 1
#
# print("Вы накопите желаемую сумму через :", years, "лет")

# ````````````Дз на пополам с gpt````````````#
# attempt = 0
# digit = 6
#
# while True:
#     number = int(input("Введите ваше число :"))
#     attempt += 1
#
#     if number < digit:
#         print("Число меньше, чем нужно. Попробуйте ещё раз!")
#     elif number > digit:
#         print("Число больше, чем нужно. Попробуйте ещё раз!")
#     else:
#         print("Вы угадали! Число попыток:", attempt)
#         break

# `````````````````Дз```````````````````````#
# min = 1
# max = 100
#
# while True:
#     mid = (min + max) // 2
#
#     print("Твоё число равно, меньше или больше, чем число:", mid, "?")
#     answer = int(input("Введите одно из трёх чисел : 1 — равно, 2 — больше, 3 — меньше"))
#     if answer == 1:
#         print("Весёлая игра , давай ещё раз ?")
#         break
#     elif answer == 2:
#         min = mid + 1
#         print("Текущее число :", min)
#     else:
#         max = mid - 1
#         print("Текущее число :", max)

# `````````````````Дз```````````````````````#
# for meters in (100,90,95,87,102):
#  if meters % 3 == 0:
#    print(meters, 'Подходит')
#  else:
#    print(meters, 'Не подходит')

# `````````````````Дз```````````````````````#
# for number in (15, 258, 547, 220, 647, 330, 907, 256, 86, 23) :
#     if 99 < number < 1000 and number % 5 == 0 :
#         print(number , "выигрышный билет")

# `````````````````Дз```````````````````````#
# for square in range( 0 , 11) :
#     print(square ** 2)

# `````````````````Дз```````````````````````#
# time = int(input("Который час? "))
#
# for time in range( 0 , time) :
#     print("Ку-ку!")

# `````````````````Дз```````````````````````#
# for square in range (0 , 20) :
#     print(2 ** square)

# `````````````````Дз```````````````````````#
# for cube in range (1 , 11) :
#     print(cube ** 3)

# `````````````````Дз```````````````````````#
# num_1 = int(input("Введите первое число :"))
# num_2 = int(input("Введите второе число :"))
# sum = 0
#
# for nums in range (num_1 , num_2+1) :
#     sum += nums
#     print(sum)

# `````````````````Дз```````````````````````#
