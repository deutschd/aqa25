#2.1 Переменные

#t = "Hello world!"
#print(t)

#`````````````````ДЗ````````````````````````#
#first = "Моя первая переменная!"
#second = "И не последняя !"
#print(first)
#print(second)
#+++++++++++++++++++++++++++++++++++++++++++#

#2.2 Оператор ввода input

#name = input("Введите имя ")
#print("Привет")
#print(name)
#name2 = input("Введите второе имя ")
#print("Привет, ")
#print(name2)

#`````````````````ДЗ````````````````````````#
#name = input("Введите ваше имя :")
#color = input("Ваш любимый цвет : ")
#sport = input("Каким спортом вы занимаетесь ? :")
#print("Привет",name)
#print("Твой любимый цвет это" ,color , "?")
#print("А занимаешься ты " , sport)
#`````````````````ДЗ2```````````````````````#
#name_1 = input("Введите первое имя :")
#name_2 = input("Введите второе имя :")
#print("Привет ,")
#print(name_1)
#print("Привет ,")
#print(name_2)
#`````````````````ДЗ3```````````````````````#
#sur_name = input('Введите фамилию: ')
#print('Ваша фамилия - ')
#print(sur_name)

#+++++++++++++++++++++++++++++++++++++++++++#

#2.3 Строки и конкатенация

#name = input("Введите имя ")
#print("Привет", name, "I'm - computer")

#Конкатинация#

#print("Торговая "+" Площадь")

#a = input("Введите первое слово: ")
#b = input("Введите второе слово: ")
#c = a + " середина " + b
#print(c)
#`````````````````ДЗ1```````````````````````#
#surname = input("Ваша фамилия ? :")
#print("HI", surname )
#`````````````````ДЗ2```````````````````````#
#wirbs_1 = input("Введите первое слово :")
#wirbs_2 = input("Введите второе слово :")
#print(wirbs_1  +  wirbs_2)
#`````````````````ДЗ3```````````````````````#
#animal_1 = "заяц"
#animal_2 = "черепаха"
#print(animal_1 +  " спит, " +animal_2 + " идёт")
#`````````````````ДЗ4```````````````````````#
#first_name = input('Введите имя пользователя: ')
#greeting = 'Утро доброе!'
#print(greeting, first_name)
#intro = "К сожалению, у Вас нет доступа к системе."
#info = "Пожалуйста, обратитесь к системному администратору."
#print(intro , info)
#`````````````````ДЗ5```````````````````````#
# where_from = input("Откуда вылетаете ?:")
# where_for = input("Куда летите ?:")
# print(where_from + " - " + where_for)
#`````````````````ДЗ6```````````````````````#
# user = input("Введите имя пользователя :")
# new_file = input("Введите имя файла :")
# print("Путь к файлу " +"C/:"+user+"/docs/folder/"+new_file+".txt" )
#+++++++++++++++++++++++++++++++++++++++++++#

#2.4 Особенности работы с переменными

#name1, naem2, name3 = "Саша","Маша","Паша"
#print(name1,naem2,name3)
#`````````````````Д1```````````````````````#
# a = input('Введите первое слово: ')
# b = input('Введите второе слово: ')
# print(a, b)
# a , b = b , a
# print(a, b)

#+++++++++++++++++++++++++++++++++++++++++++#

#3.2 Числа и арифметические операции с ними

#print(10+20)
#print(30/15)
#print(99-72)
#print(4**7)

#a = 12
#b = 13
#c = a + b
#print(c)
#or
#print(a + b)
#print("HI", c)

#+++++++++++++++++++++++++++++++++++++++++++#

#3.3 Приоритет арифметических операций

#+++++++++++++++++++++++++++++++++++++++++++#

#3.4 Ввод числа с клавиатуры

#a = int(input("Введите первое число :"))
#b = int(input("Введите второе число :"))
#c = a + b
#print(c)

#a = "123"
#b = "432"
#c = a + b
#d = int(c)*2
#print(d)

#+++++++++++++++++++++++++++++++++++++++++++#

#3.5 Деление нацело и с остатком

# mango = 98
# boxes = 11
# full_boxes = mango // boxes
# print("Полных ящиков :" ,full_boxes)
# rest_mango = mango % boxes
# print("Неполных ящиков :" , rest_mango)

# "//" - деление нацело (Показывает только целое число при делении)
# "%" - деление с остатком (Показывает только остаток от числа при делении)

#+++++++++++++++++++++++++++++++++++++++++++#

#3.6 Сокращённые операторы

# product = 0
# product = product + 200
# print("Итоговая сумма :" , product)
# product = product + 327
# print("Итоговая сумма :" , product)
# product += 450
# print("Итоговая сумма :" , product)

#+++++++++++++++++++++++++++++++++++++++++++#

#4.2 Условный оператор

# count = int(input("Загадай число от 1 до 10 :"))
# my_number = 8
# if count == my_number:
#      print("Ты молодец!")
# else:
#     print("В следующий раз повезёт :)")

#+++++++++++++++++++++++++++++++++++++++++++#

#5.2 Вложенные условия

# bank = int(input("К оплате :"))
# if bank > 40000:
# 	bank -= 40000
# 	print("Покупка успешно совершена")
# 	if bank < 2000:
# 		bank+=500
# 		print("Применена скидка")
# else:
# 	print("Недостаточно средств :(")
# print("На счету осталось " , bank)
# print("Хорошего дня!")



# product = int(input("Сумма чека :"))
# delivery = int(input("Сумма доставки :"))
# discout = 0
# if product > 7500:
# 	print("Поздравляем , доставка вдвое дешевле")
# 	delivery /=2
# 	if product %2 == 0:
# 		print("Вам положен подарок")
# 		discout = 500
# price = product + delivery - discout
# print("Всего к оплате:", price)

#+++++++++++++++++++++++++++++++++++++++++++#

#5.3 Цепочки условий if-elif-else

# profit = int(input("Размер взноса :"))
# if profit < 9700:
# 	tax = profit * 13 / 100
# 	print("Сумма налога 13% ", tax)
# elif profit < 63000:
# 	tax = profit * 20 / 100
# 	print("Сумма налога 20% ", tax)
# else:
# 	tax = profit * 30 / 100
# 	print("Сумма налога 30% ", tax)

#+++++++++++++++++++++++++++++++++++++++++++#