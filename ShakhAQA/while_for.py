print('while & for - beginning')
print('while:\n')

counter = 0
total = 0
while counter < 5:
    counter += 1
    total += counter
print("total:", total)
print("counter:", counter)

print("PASSWORD IN WINDOWS\n")
# secret_info = "Python is a C framework"
# password = "cat"
# user_input = ''
# while user_input != password:
#     user_input = input("Enter your password: ")
# print("Welcome! Secret info:", secret_info)

print("BALANCE MINUS UNTIL LIMIT IS REACHED\n")
# limit = 5000
# balance = 12000
# while balance > limit:
#     print('balance:', balance)
#     expense = int(input("How much? "))
#     balance -= expense
# print("Done, you have", balance, "left")

print('\tHOMEWORK - count sum before we enter "0"')
# number = int(input('Введите число: '))
# total = 0
# while number != 0:
#     total += number
#     number = int(input('Введите число: '))
# print('Total before we enter 0 as a number: ', total)
print('\tHOMEWORK - 7-14-21-28-...-98')
number = 0
while number < 97:
    number += 7
    print(number)

print('\tPROCESS STOPS AT EXACT NUMBER')
n = 6
total = 0
while n:
    print('process n', n)
    if n < 4:
        break
    total +=n
    n -= 1
print('total:', total)
print(n)

print('\tSUM OF EACH NUMBER(with break)')
number = 123456
nums_total = 0
while number:
    remainder = number % 10
    if remainder < 4:
        break
    nums_total += remainder
    number //= 10
print('nums_total:', nums_total)
print('number is reached:', number)

print("\t\nREAD(r) - REMEMBER(w) - QUIT(q)") #1
# memory = None
# while True: # 1
#     command = input('Command: ')
#     if command == 'r':
#         print('Memory:', memory)
#     elif command == 'w':
#         memory = input('Remember?: ')
#     elif command == 'q':
#         print('Bye!')
#         break
#     else:
#         print('Known commands: r, w, q (quit)')


print('\tHOMEWORK - Ask temperature and distance man can walk in it')
# temperature = int(input('Enter temperature: '))
# distance = 0
# while temperature >= 15:
#     distance += 20
#     print("Your distance:", distance)
#     temperature -= 2
#     print('Temperature right now:', temperature)
#     if temperature <= 15:
#         break
#     distance += 10
#
# print("Distance:", distance)
# print("Temperature:", temperature)


print('\t\nHOMEWORK - SUM BEFORE WE MEET "5"')
# code = int(input('Enter the code(only numbers): '))
# sum = 0
# while code:
#     slice_code = code % 10
#     if slice_code == 5:
#         print('5!:', slice_code)
#         break
#     sum += slice_code
#     code //= 10
#
# print('Your sum before 5:', sum)

code = 12345
coder = code // 10
print('12345 // 10:', coder)

print('\t\nHOMEWORK - READ UNTIL NEGATIVE NUMBER IS WRITTEN (+ SUM OF TRIES)')
# memory = None
# tries = 0
# while True:
#     command = int(input('What number?:'))
#     if command >= 0:
#         print('your number', command)
#     elif command < 0:
#         print('Your tries', tries)
#         break
#     else:
#         print("You're done")
#     tries += 1


print('\t\nHOMEWORK - IF 3 = you lose, if another you won 500$(1-6')
# first_money = int(input('Enter your budget: '))
# while  first_money != 0 or 10000 > first_money:
#     counter = int(input('Choose 1-6:'))
#     if counter == 3:
#         first_money = 0
#         print('You lose everything!')
#         break
#     elif 1 <= counter <= 6:
#         first_money += 500
#         print('Your balance:', first_money)
#     else:
#         print('Good, please enter number between 1-6')









