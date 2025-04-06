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