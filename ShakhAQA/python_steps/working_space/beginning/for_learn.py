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

print('\tAlgorithms with for in range')
print('\tPrime number')
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
# sum_numb = 0
# enter_dif = 1
# numbers_have_sum = 0
# for number_sum in range(1,5):
#
#     number_add = int(input('Choose number: '))
#     numbers_have_sum += number_add
#     enter_dif += number_sum + 1
#     print('enter_dif', enter_dif)
# print('The hidden number:', enter_dif - numbers_have_sum)
# print('I GOT IT OOOOOOOOOOOOOOOOOOOOOOOO')


print('\n\tFOR LEARN - HARD LVL. ALERT!')
print('\n\tFOR LEARN - HARD LVL. ALERT!!')
print('\n\tFOR LEARN - HARD LVL. ALERT!!!')
print('\tENTER FROM 1 TO N AND FIND ONE YOU DID NOT')
# total_cards = int(input('Enter total card number: '))
# #  if it was math -> total_sum = (1+total_cards)/2 * total_cards
# total_sum = 0
# remaining_sum = 0
# for card in range(1, total_cards + 1):
#     total_sum += card
# for card in range(total_cards - 1):
#     remaining_card = int(input('Number of card: '))
#     remaining_sum += remaining_card
# print('Number of lost one:', total_sum - remaining_sum)


print('\n\tALGORITHMIC FOR')
number = 1
while number <= 10:
    print(number ** 3)
    number += 1

n = 10
for number in range(1, (n//2) + 1):
    # if number % 2 == 0:
    number *= 2
    print(number, '** 3 =', number ** 3)


print('\n\tDIVIDING CELLS')
total_hours = 15 # int(input)
cells = 1
for hour in range(1, total_hours // 3 + 1):
    cells *= 2
    print('hour', hour * 3)
    print('number of cells', cells)
    print('hours left', total_hours - hour * 3)
    print()
print('experiment end')

print('\tPRACTICE - ONLY EVEN ** 3')
n = 9
for number in range(1, n//2 + 1):
    number *= 2
    print(number,'number in ^3:', number ** 3)

print('\tPRACTICE - DIVIDING CELLS')
total_hours = 30 # int(input)
cells = 1
print('Total hours:', total_hours)
for hour in range(1, total_hours //3 + 1):
    cells *= 2
    print('hours spent:', hour * 3)
    print('number pf cells:', cells)
    print('hours left:', total_hours - hour * 3)
    print()
print('The end.')

# random_number = 1234 # int(input('Enter number: '))
# last_number = random_number % 10
# random_number = random_number // 10
# print('last_number:', last_number)
# print('random_number:', random_number)
#
# n = 130
# n_hours = 130//60
# n_minutes = n - n_hours * 60
# print('hours:', n_hours, 'minutes:', n_minutes)

print('\tPRACTICE - ODD NUMBER ^ 2 (only with for)')
n = 10
for number_cube in range(1, n//2 + n % 2+ 1):
    number_cube = number_cube * 2 - 1
    print(number_cube, 'in ^2:', number_cube ** 2)
    # print(number_cube, 'in ^2:', number_cube ** 2)
    # number += 2

print('\t\nFOR IN RANGE + START/STOP/STEP')
for number in range(1, n, 2): # 1-start n-stop 2-step
    print(number, '** 2 =', number ** 2)

# wake_up = 8
# water = 0
# calories_sum = 0
# for hour in range(wake_up, 23, 3):
#     water += 1
#     print('Went to eat in', hour, 'hours')
#     calories = int(input('how much food did you consume? '))
#     calories_sum += calories
# print('You drank:', water, 'l of water')
# print('You ate:', calories_sum, 'calories')

print('\tPRACTICE - 1^3, 3^3, 5^3... in start,stop,step')
for number in range(1,10,2):
    print(number, '** 3 =:', number ** 3)

sum = 0
print('\tPRACTICE - every 5th sum')
for number in range(1, 22, 5):
    print('number:', number)
    sum += number
print('sum of every 5th, from 1 to 22:', sum)

print('\tPRACTICE - every 3h calories + water consumtion')
# calories_sum = 0
# water = 0
# for wake_up in range(13, 23, 3):
#     water += 1
#     calories = int(input('how much calories did you consume?: '))
#     calories_sum += calories
# print('calories sum:', calories_sum)
# print('water you drank:', water)

print('\n\tMINUS range with start,stop,step')
seconds = 12
for sec in range(seconds, -1, -1):
    print('microwave sec left:', sec)
print('wow')

# total_soldiers = 9
# total_rules = 120 # how many rules in law
# push_ups = 0
# for soldier in range(total_soldiers, 0, -4):
#     soldier_rules = int(input('Tell the number of rules?: '))
#     if total_rules != soldier_rules:
#         print('Bad..', 10 * soldier, 'push ups!')
#         push_ups += 10 * soldier
# print('Total push ups:', push_ups)

print('\n\tPRACTICE - hide & seek 5-4-3-2-1')
total_sec = 5
for hide in range(total_sec, 0, -1):
    print(hide)
print("I'll find you!")

print('\tPRACTICE - SOLDIER PUSH UPS')
total_soldiers = 3
question = 1
push_ups = 0
for soldier in range(total_soldiers-4, 0, -4):
    if total_soldiers <=3:
        break
    soldier_rules = int(input('answer!: '))
    if question != soldier_rules:
        print('you do:', push_ups * 10)
        push_ups += 10 * soldier
print('total push ups:', push_ups)

print('\tPRACTICE - hide & seek upgrade')
seconds_count = 10
for hidden in range(seconds_count + seconds_count % 2, 0, -2):
    print('hidden time left:', hidden)

step = 3
for number in range(5, 10, step):
    print(number, "** 2 =", number ** 2)

print('\n\tPRACTICE END FOR')
print('\tPRACTICE - Month to survive with food')
months = 0
for cosmic_food in range(100, 0, -4):
    months+= 1
print('months to survive:', months)

print('\tPRACTICE - every 5 and sum')
# number_of_people = 20
# every_5_to_call = 5
# money = 0
# for people_to_call in range(0, number_of_people, every_5_to_call):
#     how_much = int(input('HOW MUCH MONEY YOU HAVE?: '))
#     money += how_much
#     print('guy to have money #:', people_to_call)
#     print('ALL MONEY:', money)
# print('we have...', money, 'of money')

print('\tPRACTICE - MICROWAVE timer')
# reverse_timer = int(input('Enter microwave time: '))
# allocated_time = 0
# for timer in range(reverse_timer, -1, -1):
#     response = int(input('Take food?(1=yes, no=0): '))
#     if response == 1:
#         print('Your food is ready!')
#         print('Timer is frozen on:', timer)
#         break
#     elif response == 0:
#         print('Oh, it is not...ok')
#     else:
#         print('please enter only 1 or 0')
#     print('Time left:', timer)

print('\tPRACTICE - a,b,c = all numbers from a to b - c')
a = 1
b = 5
c = 10
a_b_line = 0
if a >= b:
    for line in range(b, a + 1, 1):
        print('line:', line)
        a_b_line += line
else:
    for line in range(b, a - 1, -1):
        print('line:', line)
        a_b_line += line
print('line(a to b)=', a_b_line)
print('line - c    =', a_b_line - c)

print('\tPRACTICE - ')
a = -2
b = 2
reverse = a
if a>b:
    a, b = b, a
else:
    print('continue')
for line in range(b, a - 1, -1):
    x = line
    y = (x ** 3) + (2 * (x ** 2)) - (4 * x) + 1
    print('x    =', x)
    print('y(x) =', y)
    print()
print()

scholarship = 10000
expenses = 12000
inflation = 0.03
difference_sum = 0
for life_in_uni in range(10):
    difference = expenses - scholarship
    difference_sum += difference
    print('expenses:', int(expenses), "you don't have:", int(difference_sum))
    expenses *= 1+inflation

    print('life expenses:', life_in_uni)
print('ask', int(difference_sum), 'from parents')

print('\tPRACTICE - sum from formula')
# number_n = int(input('Enter number from 1 to N: '))
# sum = 0
# for n in range (0, number_n, 1):
#     formula = ((-1) ** n) * (1 / (2 ** n))
#     print(n)
#     print('from formula:', formula)
#     sum += formula
#     print('sum go:', sum)
# print('sum is equal:', sum)

print('\tPRACTICE - Cinema')
# boys = int(input('Enter boys number: '))
# girls = int(input('Enter girls number: '))
# answer = ''
# if boys > 2 * girls or girls > 2 * boys:
#     print('No answer')
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range(k):
#         answer += 'BGB'
#     for bg in range(girls - k):
#         answer += 'BG'
# else:
#     k = girls - boys
#     for gbg in range(k):
#         answer += 'GBG'
#     for gb in range(girls - k):
#         answer += 'GB'
# print(answer)