# `````````````````Дз```````````````````````#

# number = int(input("Введите число:"))
#
# print("-=-" , end = "")
# for digit in range(0, number + 10, 10):
#     print(digit , end = "-=-")

# `````````````````Дз```````````````````````#

# karamba_count = 0
# secret_word = "Карамба"
#
# for team in range(1, 10 + 1):
#     print(f"Кандидат номер {team} ", end=' ')
#     salut = input("введите слово:")
#     if salut == secret_word or salut == "карамба":
#         karamba_count += 1
#
# print(f"В команду попало {karamba_count}, человек(а) ")

# `````````````````Дз```````````````````````#

# text = input("Введите сообщение:")
# top = 0
#
# for symbol in text:
#     top += 1
#     if symbol == "*":
#         break
#
# print(f"Символ «*» стоит на позиции {top}")

# `````````````````Дз```````````````````````#

# row = int(input("Введите кол-во рядов: "))
# armchair = int(input("Введите кол-во кресел в ряду: "))
# empty_size = int(input("Введите расстояние между рядами (в сантиметрах): "))
#
# for i in range(row):
#     print("O " * armchair)
#     print(" " * empty_size)

# `````````````````Дз```````````````````````#

# width = 15
# height = 20
#
# x = width // 2
# y = height // 2
#
# steps = 10
#
# for Charley in range(steps):
#     print(f"Марсоход находится на позиции {x}, {y}, введите команду:")
#     command = input("W (север), S (юг), A (запад), D (восток)")
#
#     if command == "W":
#         if y < height:
#             y += 1
#     elif command == "S":
#         if y > 0:
#             y -= 1
#     elif command == "A":
#         if x > 0:
#             x -= 1
#     elif command == "D":
#         if x < width:
#             x += 1
#     else:
#         print("Неверная команда! Используйте W (север), S (юг), A (запад), D (восток).")

# `````````````````Дз```````````````````````#

# boys = int(input("Кол-во мальчиков:"))
# girls = int(input("Кол-во девочек:"))
# answer = ""
#
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print("Нет решения")
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range(k):
#         answer += "BGB"
#     for bg in range(girls - k):
#         answer += "BG"
# else:
#     k = girls - boys
# for gbg in range(k):
#     answer += "GBG"
# for gb in range(boys - k):
#     answer += "GB"
#
# print(answer)

# `````````````````Дз```````````````````````#

# ttlmilk = 0
#
# for cow in range(1, 11):
#     print(f"Стойло {cow}" )
#     asnwer =  input("Выберете вариант : a — свободное стойло, b — занятое")
#     if asnwer == "a":
#         cow += 1
#     else :
#         ttlmilk += cow * 2
#     print(f"получено молока: {ttlmilk}")
# print(f"всего получено молока сегодня:,{ttlmilk}")