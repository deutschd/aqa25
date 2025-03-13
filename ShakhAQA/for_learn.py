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
    if win_number % 5 == 0 and 99< win_number < 1000:
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
total_kykys = int(input('How many times to say Ky-ky?: '))
kyky = 'Ky-ky'
for kykys in range(total_kykys):
    print(kyky)

for second_grade in range(21):
    print('All numbers from 0-20 in square:', second_grade ** 2)

