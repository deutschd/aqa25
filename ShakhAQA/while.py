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
# while True:
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


print('\t\nContinue in while')
# counter = 0
#
# while counter < 10:
#     counter += 1
#     if counter % 3 != 0:
#         squared = counter * counter
#         print(counter, 'squared =', squared)
#
# counter = 0
# while counter < 10:
#     counter += 1
#     if counter % 3 == 0:
#         print('Skip', counter)
#         continue
#     squared = counter * counter
#     print(counter, 'squared =', squared)
#
# counter = 0
#
# while True:
#     counter += 1
#     if counter > 10:
#         break
#     if counter % 3 == 0:
#         print('skipped', counter)
#         continue
#     square = counter * counter
#     print(counter, 'squared =', square)

print('\tINFINITY CYCLE. LOGiCAL variables')
print('\tPRACTICE - timer for phone')
count = 10
while count <= 10:
    print('count number:', count)
    if count == 0:
        print('Время вышло!')
        break
    count -= 1

print('\t\nPRACTICE - ASK 1/0 = GO/STOP?')
# answer = None
# while True:
#     answer = int(input('Continue?(1/0): '))
#     if answer == 1:
#         print("Ok, we'll continue!")
#     elif answer == 0:
#         print("We'll close app...")
#         break
#     else:
#         print("You can only choose 1 or 0")
# print('The app is closed')


print('\t\nPRACTICE - VIRUS, ENTER CODE UNTIL IT\'S CORRECT')
# answer = None
# while True:
#     answer = int(input('WHAT THE CODE?: '))
#     if answer == 505:
#         break
#     elif answer == 0:
#         print('It cannot be ZERO!')
#     else:
#         print('IT IS WRONG!')
# print("You're right...Good job, the code is correct!")


print('\tWHILE WITH COUNTER')
print('\tPRACTICE - HOW MANY TIMES I SHOULD SAY SO?')
# counter = int(input('HOW MANY TIMES I SHOULD SAY "HELLO WORLD?: '))
# while 0 <= counter:
#     if counter == 0:
#         break
#     counter -= 1
#     print('HELLO WORLD')

print("\tPRACTICE - WHAT'S THE WEIGHT OF ALL PRODUCTS?")
# weight = 0
# weight_sum = 0
# number_of_weights = int(input('How many weights do you have?: '))
# while 0 <= number_of_weights:
#     if number_of_weights >= 1:
#         weight = int(input('Enter weight: '))
#         weight_sum += weight
#
#     else:
#         break
#     number_of_weights -= 1
#
# print('Total weight:', weight_sum)

print("\tPRACTICE - 1...N in pow(3)")
# counter = int(input('Enter number: '))
# while counter != 1:
#     squared = counter ** 3
#     print(counter, 'in ** 3 =', squared)
#     counter -=1


print('\t\nPRACTICE - ENTER CORRECT NUMBER OR MORE')
# answer = None
# while True:
#     answer = int(input('HOW MUCH DID YOU TAKE?: '))
#     if answer >= 100:
#         break
#     else:
#         print('Are you out of your mind?')
# print('Thank you! You are done')

print('\t\nPRACTICE - HOW MANY NUMBERS IN THE SEQUENCE?')
# answer = int(input('Enter the number: '))
# counter = 1
# while True:
#     answer //= 10
#     if answer == 0:
#         break
#     else:
#         counter += 1
# print('How many numbers: ', counter)

print('\t\nPRACTICE - HOW MANY NEGATIVE/POSITIVE NUMBERS?')
# counter = 0
# counter_negative = 0
# while True:
#     answer = int(input('Enter the number: '))
#     if answer > 0:
#         counter += 1
#     if answer < 0:
#         counter_negative +=1
#     elif answer == 0:
#         break
# print('How many + numbers: ', counter)
# print('How many - numbers: ', counter_negative)

print('\t\nPRACTICE - HOW MANY TASKS AND CALLS FROM WIFE DID YOU GET?')
# tasks = None
# wifecalls = None
# hours = 3
# tasksum = 0
# while hours >= 1:
#     tasks = int(input('How many tasks for 1h?: '))
#     wifecalls = int(input('Did your wife called you?(1/0): '))
#     print('Hour:', hours, 'Tasks:', tasks, 'Wife calls:', wifecalls)
#     tasksum += tasks
#     hours -= 1
# if wifecalls > 0:
#     print('Buy the milk')
# print('TASKS TOTAL', tasksum)

print('\t\nPRACTICE - BANK = AFTER HOW MANY YEARS X WILL INCREASE TO Y')
# budget = 1000
# percentage = 25
# year = 1
# aim = 2000 # int(input('What is your aim?: '))
# while aim >= budget:
#     budget = int(budget + budget*0.25)
#     print('Budget:', budget)
#     if budget >= aim:
#         break
#     year += 1
# print('Years:', year)

print('\t\nPRACTICE - TELL ME THE NUMBER = HIGHER & LOWER')
# number = 9 # int(input('Choose the number between 1 - 10: '))
# tries = 0
# while number:
#     choose = int(input('Choose the number between 1 - 10: '))
#     if choose == number:
#         print('Congrats! Number is:', number)
#         break
#     elif choose > number:
#         print('The given number is lower...')
#     else:
#         print('The given number is higher...')
#     tries += 1
# print('Tries:', tries)

print('\t\nPRACTICE - TELL ME THE NUMBER = HIGHER & LOWER')
N = (100 + 1) // 2
while True:
    print('Your number = > or <', N, '?')
    answer = int(input('1 - =, 2 - >, 3 = <: '))
    if answer == 1:
        print('I got it!')
        break
    elif answer == 2:
        N= int(N + (100 - N) // 2)
    else:
        N = int((100 - N) // 2 - N)





