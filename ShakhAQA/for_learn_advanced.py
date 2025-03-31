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
print('Everybody is saying' + word + ', but you buy elephant!')

