from operator import truediv

number = 0
while number <= 10:
    print(number ** 2)
    number += 1

print('\n\tWHAT IS FOR?')
for number in 6,7,2,9,10:
    print(number ** 2)

print('\t WHO IS WINNER?')
winners = 0
for ticket in 345, 19, 87, 1020, 421, 555:
    if ticket % 5 == 0:
        print("Ticket winner:", ticket)
        winners +=1
print('Number of attendants:', winners)

print("\n\tPRACTICE - IF IT DIVIDES TO 3, THAT IS GOOD")
for place in 100, 90, 95, 87, 102:
    if place % 3 == 0:
        print(place, 'good place')
    else:
        print(place, " isn't good")

print("\n\tPRACTICE - NUMBERS **2, **3 **4")
for calculation in 3, 7, 5, 6, 4:
    print(calculation**2, calculation ** 3, calculation ** 4)

print("\n\tPRACTICE - ")
winner_numbers = 0
for win_number in 345, 19, 87, 1020, 421, 555, 505:
    if win_number % 5 == 0 and 99 < win_number < 1000:
        print('You win:', win_number)
        winner_numbers += 1
    else:
        print('Fu:', win_number)
print('Number of winners:', winner_numbers)

print('\n\tFOR IN RANGE')
print('\twhile:')
text = 'Python'
words_count = 0
while words_count < 5:
    print(text)
    words_count += 1
print('\tfor in range:')
for words_count in range(5):
    print(text)
    print(words_count)

for square in range(11):
    print('Squares 1-10:', square**2)


# total_months = int(input('How many months you need to collect money?: '))
# summ = 0
# for month in range(total_months):
#     print('Month:', month)
#     money = int(input('How much to collect?: '))
#     summ += money
# print('In', total_months, 'months you will collect:', summ)


print('\n\tPRACTICE - KY-KY several times')
# total_kykys = int(input('How many times to say Ky-ky?: '))
# kyky = 'Ky-ky'
# for kykys in range(total_kykys):
#     print(kyky)
#
# for second_grade in range(21):
#     print('All numbers from 0-20 in square:', second_grade ** 2)


print('\n\tRANGE SPECIFIC CASES')
# begin_num = int(input('Enter number: '))
# end_num = int(input('Enter greater one: '))
# for number_pow in range(begin_num, end_num + 1):
#     print(number_pow**2)

print('\tHOW MANY CALORIES DID YOU EAT + SLEEP HOURS')
# wake_up = int(input('When did you wake up?: '))
# awake_hours = 0
# calories_sum = 0
# for hour in range(wake_up, 23):
#     print('Right now', hour, 'hour')
#     calories = int(input('How much did you eat recently?: '))
#     calories_sum += calories
#     if calories_sum > 2000:
#         print('You ate good, now time to sleep!')
#         break
#     awake_hours += 1
# print('You ate', calories_sum, 'calories during the day')
# print('You did not sleep', awake_hours)

print('\n\tPRACTICE - NUMBER**3')
for number_cube in range(1, 11):
    print(number_cube**3)

print('\n\tPRACTICE - SUM BETWEEN RANGE 5-10 = 5+6+7+8+9+10')
# first_num = int(input('Enter first numb: '))
# second_num = int(input('Enter second lower numb: '))
# sum_numb = 0
# for numbers_collection in range(first_num, second_num + 1):
#     sum_numb += numbers_collection
# print(sum_numb)

print('\n\tPRACTICE - HOW MANY HOURS YOU ARE AWAKE')
# start_day = int(input('When did you wake up?(0-22): '))
# awake_hours = 0
# calories_sum = 0
# for hour in range (start_day, 23):
#     calories = int(input('How many calories did you eat?: '))
#     calories_sum += calories
#     if calories_sum > 2000:
#         print('Too much food, time to sleep now')
#         break
#     awake_hours += 1
# print('Total calories:', calories_sum)
# print('You did not sleep for:', awake_hours)


print('\n\tAlgorithms with FOR RANGE')
# number = 27644437 # int(input('Enter number: '))
# isPrime = True
# for divider in range(2, number):
#     if number % divider == 0:
#         isPrime = False
#         break
# if isPrime:
#     print('Prime number')
# else:
#     print('sostavnoe:')

print('\tPRACTICE - POSITIVE AND EVEN')

those_numbers = 0
for positive_even in -14, 10, 4, -12, 3, 5, 12, -10:
    if (positive_even % 2 == 0) and (positive_even > 0):
        print('your number is:', positive_even)
        those_numbers += 1
    else:
        print('is odd or negative: ', positive_even)

print('Positive and even numbers from list:', those_numbers)

print('\tPRACTICE - AVERAGE SALARY')
# counter_salary = 0
# for salary in range(12):
#     monthly_salary = int(input('Enter monthly salary: '))
#     counter_salary += monthly_salary
# print(counter_salary/12)

print('\tPRACTICE - FACTORIAL(N!)') # n! = 1*2*3*n
# factorial_total = 1
# range_factorial = int(input('Give me factorial(n): '))
# for facts in range(range_factorial):
#     facts += 1
#     factorial_total *= facts
#     print('number sequence:', facts, 'factorial until number:', factorial_total)
# print(factorial_total)


print('\tPRACTICE - 5, 4, 3 SCORE MORE?')
# students = int(input('How many students?: '))
# five = 0
# four = 0
# three = 0
# for scores in range(students):
#     which_score = int(input('Please enter a score(5-4-3): '))
#     if which_score == 5:
#         five += 1
#     elif which_score == 4:
#         four += 1
#     elif which_score == 3:
#         three += 1
#     else:
#         print('Please enter only 5-4-3')
# print('Number of all attendants:', students)
# if five > four and five > three:
#     print('Students with 5 are more:', five)
# elif four > five and four > three:
#     print('Students with 4 more:', four)
# elif three > four and three > five:
#     print('Students with 3 more:', three)
# else:
#     print('There is an equal number of scores or something wrong...')

# N = int(input('Enter number until: '))
# total = N*(N+1)//2 # arithmetic progression geometric sn=a1(1-r^n)/1-r
# for number_total in range(1, N + 1):
#     num = int(input('What did you choose?: '))
#     total -= num
# else:
#     print('We lost this one:', total)

print('Algorithms with for in range')
print('Prime number')
# isPrime = True
# number = int(input('Enter number: '))
# for divider in range(2, number):
#     if number % divider == 0:
#         isPrime = False
#         break
# if isPrime:
#     print('Number is Prime')
# else:
#     print('Number is ordinary')
print('\n\tPRACTICE - ENTER FROM 1 TO N AND FIND WHICH ONE YOU DID NOT TYPE')
sum_numb = 0
enter_dif = 1
numbers_have_sum = 0
for number_sum in range(1,5):

    number_add = int(input('Choose number: '))
    numbers_have_sum += number_add
    enter_dif += number_sum + 1
    print('enter_dif', enter_dif)

print('The hidden number:', enter_dif - numbers_have_sum)
print('I GOT IT OOOOOOOOOOOOOOOOOOOOOOOO')




