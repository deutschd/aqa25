#9.2 Сравнение строк

# password = (input("Введите пароль :"))
#
# while password != "bsae124531" :
#     print("Не верный пароль!")
#     password = (input("Повторите попытку"))
# print("Добро пожаловать!")

# +++++++++++++++++++++++++++++++++++++++++++#

# author = ("Имя автора произведения?"))
# bad_answer = 0

# while author != "Пушкин" :
#     author = ("Имя автора произведения?"))
#     bad_answer += 1
# print("Молодец , пятёрка")
# print("У нас в классе" , bad_answer , "учиников")

# +++++++++++++++++++++++++++++++++++++++++++#

# bad_answer = 0
# for student in range (5):
#     answer = (input("Имя автора произведения?"))
#     if (answer == "Пушкин") or (answer == "пукшкин"):
#         print("Молодец , пятёрка")
#         break
#     print("Не правильно 2 !")
#     bad_answer += 1
# print("Кол-во двоек :" , bad_answer)

#9.3 Цикл for итерирование по строке

# +++++++++++++++++++++++++++++++++++++++++++#

# for symbol in "Python":
#     print(symbol)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = input("Введите слово :")
# for symbol in word:
#     print(symbol)

# +++++++++++++++++++++++++++++++++++++++++++#

# word = input("Введите слово :")
# for symbol in word:
#     print(symbol * 3)
#     print("_" * 4)

# +++++++++++++++++++++++++++++++++++++++++++#

#9.4 Дополнительные возможности функции print

# text = input("Введите текст:")
# new_sym = ""
#
# for symbol in text:
#     new_sym += symbol + ""
# print(new_sym)

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input("Введите текст:")
#
# for symbol in text:
#     print(symbol , end = " ")

# +++++++++++++++++++++++++++++++++++++++++++#

# text = input("Введите текст:")
#
# for symbol in text:
#     print(symbol , end = "@ , \n")

# +++++++++++++++++++++++++++++++++++++++++++#

# number = int(input("Введите число:"))
# step = int(input("Введите шаг:"))
# summ = 0
#
# print("IP-адерес:", end = " ")
# for count in range(3):
#     print(number , end = '.')
#     summ += number
#     number += step
# print(summ)

#9.5 Типовые алгоритмы работы со строками

# text = input("Введите текст")
# summ = 0
#
# print("\nОтфильтрованный текст" , end = " ")
# for symbol in text:
#     if symbol == "1" or symbol == "9":
#         summ += int(symbol)
#     else :
#         print(symbol , end = " ")
# print("\nСумма :" , summ)

# +++++++++++++++++++++++++++++++++++++++++++#

# string = input("Введите строку :")
# prevSym = ""
# equalSym = False
#
# for letter in string:
#     if prevSym == letter:
#         equalSym == True
#         break
#     else:
#         prevSym == letter
#
# if equalSym:
#     print("Есть две одиноковые буквы подряд")
# else:
#     print("Нет двух одиноковые букв подряд")