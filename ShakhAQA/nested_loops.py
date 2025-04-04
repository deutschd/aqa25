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
