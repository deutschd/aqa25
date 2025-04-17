from base64 import a85decode
from stringprep import b1_set, b3_exceptions

print('\tNESTED LOOPS')
a = 10
for b in range(1,10):
    print(a, '+', b, '=', a * b)

print('nested loop:')
for a in range(1, 10):
    for b in range(1, 10):
        print(a, '*', b, '=', a * b)
    print()

print('''TABLE 0 1 2 3
      1 2 3 4
      2 3 4\n''')
for row in range(0, 6, 2):
    for col in range(0, 6, 3):
        print(row + col, end =' ')
    print()

for row in range(1, 10):
    for col in range(1, 10):
        print(row * col, end='\t')
    print()

number = 6 # int(input('Enter number: '))
for row in range(number):
    for col in range(number):
        print(row + col, end = ' ')
    print()

for row in range(9):
    for col in range(1, -9, -1):
        print(row + col, end = '\t')
    print()

for row in range(1, 5, 1):
    for col in range(1, 5):
        if col % 2 == 0:
            print(col, end=' ')
        if row % 2 == 0:
            print(row, end=' ')
    print()

print('\n\tIF IN NESTED LOOPS')
print('Matrix')
size = 5 # int(input('Enter size of table: '))
for row in range(1, size + 1):
    for col in range(1, size + 1):
        if row % 2 == 0:
            print(row, end=' ')
        else:
            print(col, end=' ')
    print()

for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end= '')
        elif col == 25:
            print('|', end= '')
        else:
            print(' ', end= '')
    print()

print('\n\tPRACTICE - MATRIX 5')
size = 5
for row in range(1, size+1, 1):
    for col in range(1, size+1, 1):
        if row % 2 == 0:
            print(row, end= ' ')
        else:
            print(col, end= ' ')
    print()

print('\n\tPRACTICE - Black Box')
# size = int(input('Enter size of matrix: '))
# for row in range(1, size + 1, 1):
#     for col in range(1, size + 1, 1):
#         if col % 3 == 0:
#             print(col, end=' ')
#         elif row % 3 == 0:
#             print(row, end=' ')
#
#         else:
#             print(row, end=' ')
#     print()

for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end='')
        elif col == 25:
            print('|', end='')
        else:
            print(' ', end='')
    print()

size = 5 # int(input('Enter size of matrix: ')
for row in range(size):
    for col in range(size):
        if row < col:
           print(0, end= ' ')
        elif row > col:
            print(2, end =' ')
        else:
            print(1, end =' ')
    print()

for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end='')
        elif col == row + 29:
            print('\\', end = '')
        elif col == -row + 19:
            print('/', end='')
        elif col == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print()

print('\n\tPRACTICE - GATES')
for row in range(20):
    for col in range(30):
        if row == 0:
            print('-', end='')
        elif col == 0 or col == 29:
            print('|', end='')
        else:
            print(' ', end='')
    print()

print('\n\tPRACTICE - GATES')
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end='')
        elif col == -row + 19:
            print('/', end='')
        elif col == row +29:
            print("\\", end='')
        elif col == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print()

print('\n\tPRACTICE - Diagonal')
size = 5 # int(input('Enter size of matrix: '))
for row in range(size):
    for col in range(size):
        if row + col == size - 1:
            print(1, end=' ')
        elif row + col > size - 1:
            print(2, end=' ')
        else:
            print(0, end=' ')

    print()
# a5 b1
# a4 bz
# a3 b3
# a2 base64
# 5-1 4-2 3-3 2-4 1-5

print('\n\t10.4 - SOLVE TASKS')
people = 3 # int(input('Enter people: '))
for hour in range(people + 1):
    print('Hour left:', hour)
    for num in range(hour, people):
        print('Number in queue', num)
    print()
print('END!')

print('\n\tFIND NUMBER - HOW MANY TIMES IN SEQUENCE')
seqNum = 5 # int(input('Enter: '))sequence of numbers
numeral = 2 # what number we should find
while numeral < 0 or numeral > 9:
    numeral = int(input('Number should be between 0 and 9. Enter new one: '))
numeralCount = 0
for num in range(seqNum):
    print('Enter', num, 'number: ', end='')
    number = int(input(''))
    while number > 0:
        if number % 10 == numeral:
            numeralCount += 1
        number //= 10
print('Number', numeral, 'in sequence', numeralCount)



