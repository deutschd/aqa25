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
print('\n2 squares of a chessboard match')
a = 4 # int(input())
b = 4 # int(input())
c = 5 # int(input())
d = 5 # int(input())
if a==c and b==d:
    print('YES')
elif (a+b)%2==0 and (c+d)%2==0:
    print('YES')
elif (a+b)%2!=0 and (c+d)%2!=0:
    print('YES')
else:
    print('NO')


a = 4 # int(input())
b = 4 # int(input())
c = 5 # int(input())
d = 5 # int(input())
if a-b==c-d:
    print('YES')
elif a+b==c+d:
    print('YES')
else:
    print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a==(c+2) and b==(d-1):
#     print('YES')
# elif a==(c+1) and b==(d-2):
#     print('YES')
# elif a==(c-1) and b==(d-2):
#     print('YES')
# elif a==(c-2) and b==(d-1):
#     print('YES')
# elif a==(c-2) and b==(d+1):
#     print('YES')
# elif a==(c-1) and b==(d-2):
#     print('YES')
# elif a==(c+1) and b==(d+2):
#     print('YES')
# elif a==(c+2) and b==(d+1):
#     print('YES')
# elif a==(c-1) and b==(d+2):
#     print('YES')
# else:
#     print('NO')
a=354
print(a//100, a//10%10, a%10)
a=126 # int(input()) # checks if 1+6 and 1-6 is equal
c= max(a//100, a//10%10, a%10) - min(a//100, a//10%10, a%10)
d= (a//100 + a//10%10 + a%10) - (max(a//100, a//10%10, a%10) + min(a//100, a//10%10, a%10))
if c == d:
    print('Число интересное')
else:
    print('Число неинтересное')

import math
from math import *
a = 1
b = 3
c = 4.7
print('floor(c) =',floor(c))
print('ceil(c) =',ceil(c))
print('sqrt(a) =',sqrt(a))
print('pow(a,b) =',pow(a,b))
print('log(a) =',log(a))
print('log10(a) =',log10(a))
print('log(a,b) =',log(a,b))
print('factorial(a) =',factorial(a))
print('degrees(a) =',degrees(a))
print('radians(a) =',radians(a))
print('cos(a) =',cos(a))
print('sin(a) =',sin(a))
print('tan(a) =',tan(a))
print('acos(a) =',acos(a))
print('asin(a) =',asin(a))
print('atan(a) =',atan(a))
print('atan2(a,b) =',atan2(a,b))
print('pi =', pi)
print('e =', e)
print('round(c) =',round(c))
print('round(c,2) =',round(c,2))

from math import *

a = -142 # float(input())
b = 100 # float(input())
c = -55 # float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    x = -(b / (2 * a))
    print(x)
elif D < 0:
    print('Нет корней')
else:
    x1 = (-b - sqrt(D)) / (2 * a)

    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 > x2:
        print(x2)
        print(x1)
    else:
        print(x1)
        print(x2)


for i in range(10):
    print('Hi', i)

for i in range(10,18):
    if i % 2 == 0:
        print(i)

for i in range(10,18,2):
    print(i)
for i in range(20,14,-1):
    print(i)

print('SHOW ODD NUMBERS:')
m = 4 # int(input())
n = -5 # int(input())

for i in range(m,n-1,-1):
    if 0 == (i - 1)%2:
        print(i)

a=6 # int(input())
for i in range(1,11):
    print(str(a)+' x '+ str(i)+' = '+str(a*i))

print('Enter the number, we know how many of them more than 10')
counter = 0
for _ in range(10):
    num = 12 # int(input())
    if num > 10:
        counter = counter + 1
print('You entered', counter, 'numbers more than 10')

counter1 = 0
counter2 = 0
# for _ in range(10):
#     num = int(input('Enter the number: '))
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('You entered', counter1, 'numbers more than 10')
# print('You entered', counter2, 'numbers which is 0')

print('How many numbers divided to 4:')
counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)

print('How many numbers more than 10, their sum')
total = 0
for _ in range(10):
    num = 3 # int(input('Enter a number: '))
    if num > 10:
        total = total + num
print('sum of numbers bigger than 10:', total)

print('sum of natural numbers from 1 to 100')
total = 0
for i in range(1,101):
    total = total + i
print('sum is equal to:', total)


print('hello')


print('Count how many numbers in input more than 10')
counter = 0
for _ in range(10):
    #num = int(input('Enter a number: '))
    if num > 10:
        counter = counter + 1
print('There are', counter, 'numbers in total more than 10')


print('How many numbers more than 10 and are 0')
counter1 = 0
counter2 = 0
for _ in range(10):
    #num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('There are', counter1, 'numbers in total more than 10')
print('There are', counter2, 'zero numbers in total')


counter = 0
for i in range(1,101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)


print('Count sum of numbers more than 10')
total = 0
for _ in range(10):
    #num = int(input())
    if num > 10:
        total = total + num
print('Sum of numbers more than 10 = ', total)


print('SUM of Natural numbers from 1 to 100')
total = 0
for i in range(1,101):
    total = total + i
print('Sum is equal to:', total)


print('10 numbers and their arithmetic mean')
total = 0
for _ in range(10):
    #num = int(input())
    total = total + num

average = total / 10
print('Average =', average)


print('Max and min')
print('The biggest number from 10 given')
largest = 0
for _ in range(10):
    num = int(input('Enter a number: '))
    if num > largest:
        largest = num
print('Largest number =', largest)















