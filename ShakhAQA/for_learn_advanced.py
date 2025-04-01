from email.contentmanager import get_and_fixup_unknown_message_content

print('\tSTRING')
print('\tHOMEWORK from 8.0 GIRLS AND BOYS in THEATRE')
boys = 3 # int(input('Enter number of boys: '))
girls = 6 # int(input('Enter number of girls: '))
answer = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    print('no answer')
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girls - k):
        answer += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        answer += 'GBG'
    for gb in range(boys - k):
        answer += 'GBG'
print(answer)

print('\n\tCHECK PASSWORD')
# password = input('Enter password: ')
# while password != 'Python235':
#     print('Incorrect pass!')
#     password = input('Try again!: ')
# print('Correct password!')

print('\n\tLITERATURE SCORE IN CLASS')
# badGradeCount = 0
# for student in range(5):
#     answer = input('Who wrote this text?: ')
#     if answer == 'Pushkin' or answer == 'pushkin':
#         print('Correct!')
#         break
#     print('It is wrong...')
#     badGradeCount += 1
# print('Number of 2: ', badGradeCount)

print('\n\tPRACTICE - Literature. did u read?')
# students = 8
# badGradeCount = 0
# for student in range(students):
#     answer = input('Who wrote that?: ')
#     if answer == 'Pushkin' or answer == 'pushkin':
#         print('Correct')
#         break
#     print('It is wrong')
#     badGradeCount += 1
# print('Number of bad grades=', badGradeCount)

print('\n\tPRACTICE - What is the password?')
# i_expect = input('What is the password?: ')
# while i_expect != 'Gold':
#     print("Incorrect pass!")
#     i_expect = input('Try again: ')
# print('Well done!')

print('\n\tPRACTICE - What is the password?')

name = 'Shakh' # input('What is your name?: ')
print(name + ', buy elephant')
word = 'Okay, I will' # input('= ')
print('Everybody is saying ' + word + ', but you buy elephant!')

print('\n\tFOR IN STRIG:')
print('PYTHON EVERY LETTER IN new String')
phrase = 'Python' # int(input('Enter phrase: '))
for symbol in phrase:
    print(symbol * 3)
    print('=' * 10)

print('HOW MANY TIMES WE FACE EXACT LETTER')
# text = input('Enter text: ')
# first_sym = input('Enter the first letter: ')
# second_sym = input('Enter the second letter: ')
# firstSymCount = 0
# secondSymCount = 0
#
# for symbol in text:
#     if symbol == first_sym:
#         firstSymCount += 1
#     if symbol == second_sym:
#         secondSymCount += 1
# print('Number of letters', first_sym, '=', firstSymCount)
# print('Number of letters', second_sym, '=', secondSymCount)

print('\n\tPRACTICE - every letter in new line')
given_text = 'py2'
for text in given_text:
    print(text)

print('\n\tPRACTICE - text x 3 every letter')
given_text_2 = 'hiworld'
for text in given_text_2:
    print(text*3)
    print('-'*5)

print('\n\tPRACTICE - How many Ы an ы in text')
given = 'Прыг сколько - ещё не прыгнув  дал ответ'
countUpperCase = 0
countLowerCase = 0
for text in given:
    if text == 'Ы':
        countUpperCase += 1
    if text == 'ы':
        countLowerCase += 1
print('Количество Ы:', countUpperCase)
print('Количество ы:', countLowerCase)

print('\n\tADDITIONAL FUNCTIONS FOR PRINT')
phrase = 'python' # input('Phrase: ')
new_phrase = ''
for symbol in phrase:
    print(symbol, end = '\n\t')

print('IP ADDRESS')
# number = int(input('Enter first number: '))
# step = int(input('Enter step: '))
# summ = 0
#
# print('\nIP-ADRESS:', end = ' ')
# for count in range(3):
#     print(number, end = '.')
#     summ += number
#     number += step
# print(summ)

print('\nPRACTICE - Build a home')
print('-' * 10 + '\n' + '|OOOOOOOO|\n' * 5 + '-' * 10)

print('\nPRACTICE - IP ADDRESS with arith progression 192.213.234.639')
number = 192 # beginning of the ip
step = 21 # step = sum for each
summ = 0

for count in range(3): # only for: 192.213.234.
    print(number, end = '.')
    summ += number
    number += step
print(summ)

print('\n\tPRACTICE - Every 10th number add -=-')
goal = 0
print('-=- ', end='')
while goal != 50:
    print(goal, end = ' -=- ')
    goal += 10

print('\n\tALGORITHMS WITH STRING')
print('FIlt3er = filter + 3')
text = 'ex1ampl9e' # input('Enter text: ')
summ = 0
print(text)
print('filtered text:', end = ' ')
for symbol in text:
    if symbol == '1' or symbol == '9':
        summ += int(symbol)
    else:
        print(symbol, end ='')
print('\nSumm:', summ)

print('\n\tTWO LETTERS IN PAIR')
string = 'akdsjk' # input('Enter text: ')
prevSym = ''
equalSym = False
for letter in string:
    if prevSym == letter:
        equalSym = True
        break
    else:
        prevSym = letter
if equalSym:
    print('There are 2 letters together')
else:
    print('No 2 letters together')

print('\n\tPRACTICE - CREATE CREW FROM PEOPLE WHO SHOUT "HI"')
# word = 'HI'
# guys = 0
# for crew in range(10):
#     each_shout = input('What did you say?: ')
#     if each_shout == word:
#         guys += 1
# print('The crew consist of:', guys, 'members')

print('\n\tPRACTICE - FIND POSITION OF SYMBOL "*"')
text = 'THSisGo*od'
where_is_star = 0
for find in text:
    where_is_star += 1
    if find == '*':
        print('The place of * in:', where_is_star)

print('\n\tPRACTICE - THEATRE MOCKUP')
rows = 5
seats = 7
metres = 3
for theatre in range(rows):
    print('\t','='*seats, '*'*metres, '='*seats)

print('\n\tPRACTICE - CONTROLLER FOR WALL-E')
left_right = 14
top_bottom = 19
gameplay = False
print('Your location:', left_right,end='. ')
print(top_bottom)
while gameplay != True:
    movement = input('Enter movement: ')
    if movement == 'A' and 0 < left_right <= 15:
        left_right -= 1
    elif movement == 'D' and 0 < left_right <= 15:
        left_right += 1
    elif movement == 'W' and 0 < top_bottom <= 20:
        top_bottom += 1
    elif movement == 'S' and 0 < top_bottom <= 20:
        top_bottom -= 1
    elif movement == 'Q':
        break
    if left_right == 15:
        left_right -= 1
    if top_bottom == 21:
        top_bottom -= 1

    print('Your location:', left_right,',', top_bottom)

