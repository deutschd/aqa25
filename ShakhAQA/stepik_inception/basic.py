delimiter = '+'
print('a', 'b', sep=delimiter)
print('YES', sep='!', end='#')
print('NO', sep='#', end='!')

print('\n\nArithmetic Progression:')
a1 = 1 # int(input())
d = 1 # int(input())
n = 10 # int(input())
print(a1 + d * (n - 1))
print(-123 // 10)
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)
b = 34 % a * 5
print(b)
print('\n\nGeometric Progression:')
b1 = 1 # int(input())
q = 2 # int(input())
n = 5 # int(input())
print(b1 * q**(n-1))
print('\nTest results:')
a=29 % 4 * 3
print(a)
print('\nAlgorithm to get exact number from position of it:') # example 1938211 we can get fifth number (2)
# Second number: (num // 10 ** (n - 2)) % 10
# First number: num // 10 ** (n - 1)
print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')

print("Told you not to worry", "But maybe that's a lie", sep=' :) ')
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(8 * b)
a=17
b=4
print('*'*a)
print('*','*',sep=' '*(a-2))
print('*','*',sep=' '*(a-2))
print('*'*a)
print('SUM OF 1th and 4th = 2th-3th')
d=1614 # int(input())
c=d%10
f=d//100%10
a=d//100//10
b=d//10%10
x=a+c
l=f-b
if x==l:
    print('YES')
else:
    print('NO')

x=91#int(input())
if 0<x<=13:
    print('детство')
if 14<=x<=24:
    print('молодость')
if 25<=x<=59:
    print('зрелость')
if 60<=x:
    print('старость')

a=31
b=33
c=23
d=11

if a<=b and a<=c and a<=d:
    print(a)
if b<=a and b<=c and b<=d:
    print(b)
if c<=a and c<=b and c<=d:
    print(c)
if d<=a and d<=c and d<=b:
    print(d)


x=10#int(input())
if -30<x<=-2 or 7<=x<=25:
    print('Принадлежит')
else:
    print('Не принадлежит')

n=2020 # int(input())
if n%4==0 and (n%400==0 or n%100!=0):
    print('YES')
else:
    print('NO')

a,b,c,d=4,4,4,5
if a==c or b==d:
    print('YES')
else:
    print('NO')
print('Ход королём:')
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if abs(a - c) <= 1 and abs(b - d) <= 1:
#     print("YES")
# else:
#     print("NO")
print('EVERY EQUAL(3), TWO EQUAL(2), ONE(0)')
a, b, c = 1,2,3 #int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)
angle = 89

if angle < 90:
    print('Меньше 90')
elif angle > 180:
    print('Больше 180')
elif angle < 270:
    print('Меньше 270')
angle = 11

if angle < 15:
    print('Меньше 15')
if angle > 45:
    print('Больше 45')
elif angle < 75:
    print('Меньше 75')
print('\nAdding colors')
a='красный' #input()
b='зеленый' #input()
if (a=='красный' and b=='синий') or (b=='красный' and a=='синий'):
    print('фиолетовый')
elif (a=='красный' and b=='желтый') or (b=='красный' and a=='желтый'):
    print('оранжевый')
elif (a=='синий' and b=='желтый') or (b=='синий' and a=='желтый'):
    print('зеленый')
else:
    print('ошибка цвета')
print('\n2 line segments:')
a1 = 3 # int(input())
b1 = 5 # int(input())
a2 = 1 # int(input())
b2 = 3 # int(input())
if a1==a2 and b1==b2:
    print(a1, b1)
elif a1<a2 and b1<a2:
    print('пустое множество')
elif a2<a1 and b2<a1:
    print('пустое множество')
elif a1<a2 and b1==a2:
    print(b1)
elif a2<a1 and b2==a1:
    print(b2)
elif a1<=a2<b1<=b2:
    print(a2,b1)
elif a2<=a1<b2<=b1:
    print(a1,b2)
elif a1<a2<b2<b1:
    print(a2,b2)
elif a2<a1<b1<b2:
    print(a1,b1)
elif a1==a2 and b1<b2:
    print(a1, b1)
elif a1==a2 and b2<b1:
    print(a2, b2)
else:
    print('пустое множество')
print('\n2 squares of a chessboard match:')
a=1 #int(input())
b=1 #int(input())
c=2 #int(input())
d=6 #int(input())
if a==b and c==d:
    print('YES')
elif (a+b)%2==0 and (c+d)%2==0:
    print('YES')
elif (a+b)%2!=0 and (c+d)%2!=0:
    print('YES')
else:
    print('NO')

