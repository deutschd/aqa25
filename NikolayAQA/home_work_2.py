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