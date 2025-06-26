# `````````````````Дз```````````````````````#

# def count_additions():
#     print("Введите число в эксп. форме: ", end='')
#     s = input()
#
#     e_pos = -1
#     i = 0
#     for ch in s:
#         if ch == 'e':
#             e_pos = i
#         i += 1
#
#     valid = 0
#     if e_pos != -1:
#         i = 0
#         for ch in s:
#             if i == e_pos + 1 and ch == '-':
#                 valid = 1
#             i += 1
#
#     while valid == 0:
#         print("Неверный ввод. Пример: 1e-3")
#         print("Введите число в эксп. форме: ", end='')
#         s = input()
#
#         e_pos = -1
#         i = 0
#         for ch in s:
#             if ch == 'e':
#                 e_pos = i
#             i += 1
#
#         valid = 0
#         i = 0
#         for ch in s:
#             if i == e_pos + 1 and ch == '-':
#                 valid = 1
#             i += 1
#
#
#     mantissa_str = ""
#     i = 0
#     for ch in s:
#         if i == e_pos:
#             break
#         mantissa_str = mantissa_str + ch
#         i += 1
#
#
#     exponent_str = ""
#     i = 0
#     for ch in s:
#         if i > e_pos + 1:
#             exponent_str = exponent_str + ch
#         i += 1
#
#
#     mantissa = float(mantissa_str)
#     exponent = int(exponent_str)
#
#
#     power = 1.0
#     i = 0
#     while i < exponent:
#         power = power * 0.1
#         i = i + 1
#     N = mantissa * power
#
#
#     X = 1.0
#     additions = 0
#     while X <= 2.0:
#         X = X + N
#         additions = additions + 1
#
#     print("Кол-во прибавлений:", additions)
#
# count_additions()

# `````````````````Дз```````````````````````#

# def float_format():
#     x = float(input("Введите число: "))
#
#     if x <= 10:
#         print("Число должно быть больше 10")
#         return
#
#     b = 0
#     a = x
#
#     while a >= 10:
#         a /= 10
#         b += 1
#
#     print(f"Формат плавающей точки: x = {a} * 10 ** {b}")
#
# float_format()
