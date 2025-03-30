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

print('\n\tPRACTICE - ')