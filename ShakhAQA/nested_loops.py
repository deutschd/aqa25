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







