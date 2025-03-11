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

print("\t\nREAD(r) - REMEMBER(w) - QUIT(q)")
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



