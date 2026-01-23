from numpy.ma.core import maximum

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
largest = 323 # int(input('Enter the largest number: '))
for _ in range(10):
    num = 12 # int(input('Enter a number: '))
    if num > largest:
        largest = num
print('Largest number =', largest)



total = 0
counter = 0
even = 0
greater_than_6 = 0
for i in range(10, 4, -1):
    total = total + i
    counter = counter + 1
    last = i
    if i % 2 == 0:
        even = even + 1
    if i < 6:
        greater_than_6 = greater_than_6 + 1
print('total =', total)
print('counter =', counter)
print('even =', even)
print('greater_than_6 =', greater_than_6)

print('Count length of words')
total_len = 0
for _ in range(3):
    word = '321' # input('Enter a word: ')
    total_len = total_len + len(word)
print('The length of word =', total_len)


print('Find a prime number')
#num = int(input('Enter a number: '))
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
if num == 1:
    print('It is 1')
elif flag == True:
    print('It is prime')
else:
    print('It is not prime')

a, b = 3, 4
a, b = a + b, 2 * a
print(a, b)

total = 0
for i in range(1, 10):
    if i % 2 == 1:
        total = total + i
print(total)
total = 0

for i in range(1, 6):
    total += i
    print(total, end='')

print()
a=1 #int(input('enter a number: '))
b=10 #int(input('enter another number: '))
counter = 0
for i in range(a,b+1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        counter = counter + 1
print(counter)

print('Sum of given numbers')
# counter = 0
# n = int(input('Enter a number: '))
# for i in range(1,n+1):
#     num = int(input('Enter a number: '))
#     counter += num
# print(counter)

formula = 0
n = 10#int(input('Enter a number: '))
for i in range(1,n+1):
    formula = formula + 1/i

print(formula-log(n))
formula = 0
num = 10 # int(input('Enter a number: '))
for i in range(1,num+1):
    if i **2 % 10 == 2 or i **2 % 10 == 5 or i **2 % 10 == 8:
        formula += i

print(formula)

print('Find Factorial')
# fact_rial = int(input('Enter a number: '))
# total = 0
# for i in range(1,fact_rial+1):
#     total = total + i
# print(total)

print('Multiply 10 numbers random')
# total = 1
# for i in range(1,11):
#     num = int(input())
#     if num != 0:
#         total = total * num
# print(total)

# total = 0
# num = int(input())
# for i in range(1,num+1):
#     if num % i ==0:
#         total = total + i
# print(total)

l=0
# for i in range(1,11):
#     num = int(input())
#     if num % 2 == 0:
#         l='YES'
#     else:
#         l='NO'
#         break
# print(l)
#
print('\nFormula to create 1-2+3-4...((-1)**n+1)*n')
# formula = 0
# n = 5 # int(input())
# for i in range(1,n+1):
#     formula = formula + ((-1)**(i+1))*i
#
# print(formula)
#
print('\nWhat is 1st and 2nd largest number?')
# how = int(input())
# largest = True
# second_largest = True
# for _ in range(1, how+1):
#     num = int(input())
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest:
#         second_largest = num
# print(second_largest)
# print(largest)

print('\nSORT THEN CHOOSE -2 and -1:')
# nums = []
# n = int(input())
# for i in range(n):
#     num = int(input())
#     nums.append(num)
# nums.sort()
# print(nums[-2])
# print(nums[-1])

print('Another example:')
# nums = [ int(input()) for _ in range(int(input())) ]
# nums.sort()
# print(nums[-2])
# print(nums[-1])

print('\nFibonacci series - simple')
# formula = 1
# n = int(input('Enter how many Fibonacci numbers you want to see: '))
# sum = 0
# another = 1
#
# if n == 1:
#     print(1)
# else:
#     print(1, 1, end =' ')
#     for i in range(1, n - 1):
#         sum = formula
#         formula = sum + another
#         another = sum
#         print(formula, end=' ')


i = 0
while i < 3:
    print('Hello')
    i += 1

print('\nShow the square of number before "-1" number comes')
# num = int(input('Enter a number: '))
# while num != -1:
#     print('Square of number:', num * num)
#     num = int(input('Enter a number: '))

for i in range(11):
    print(i)
i = 0
while i < 11:
    print(i)
    i += 1

for i in range(0, 10, 3):
    print(i)
i = 0
while i < 11:
    print(i)
    i += 3

print('\nSum until you reach the stop word')
# text = input('Enter a word: ')
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input('Enter a word: ')
# print('Sum is equal to:', total)

print('\nSum until the function is met')
# num = int(input('Enter a number: '))
# total = 0
# while abs(num) <= 5:
#     total += num
#     num = int(input('Enter a number: '))
# print(total)

print('\nWrite words until "END"')
# word = input('Enter a word: ')
# while word != 'END':
#     print(word)
#     word = input('Enter a word: ')

print('\nWrite words until "END" or "end"')
# word = input('')
# while word != 'END':
#     if word =='end':
#         word = 'END'
#     else:
#         print(word)
#         word = input('')

print('\nWrite words until "стоп","хватит","достаточно"')
# word = input()
# counter = 0
# while word not in ('стоп','хватит','достаточно'):
#     counter +=1
#     word = input()
# print(counter)

print('Before we meet number not divided by 7')
# number = int(input('Enter a number: '))
# while number%7 == 0:
#     print(number)
#     number = int(input('Enter a number: '))

print('Before we meet negative number show SUM of previous')
# num = False
# counter = 0
# while num >= 0:
#     counter += num
#     num = int(input())
# print(counter)

print('How many 5 students get (from 1-5 only allowed)')
# num = int(input())
# counter = 0
# while 1 <= num <= 5:
#     if num == 5:
#         counter = counter + 1
#         num = int(input())
#     else:
#         num = int(input())
# print(counter)

print('Until we met a word with without the symbol "_" - write this word')
# nick=input()
# word ='_'
# while word in nick:
#     nick = input()
# print(nick)

print('How many people between two people in queue')
# name1 = 'Александра'
# name2 = 'Левон'
# name = 0
# counter = 0
# counterAleksandra = 0
# while name != name2:
#     name = input()
#     counter += 1
#     if name == name1:
#         counterAleksandra = counter
#         print(counter)
#
# print(counter-counterAleksandra-1)



print('\nShow how many 25-10-5-1 coins can be in sum like 89')
# price = int(input("Enter amount: "))
# counter = 0
# counter += price // 25
# price %= 25
# counter += price // 10
# price %= 10
# counter += price // 5
# price %= 5
# counter += price
# print(counter)

# num = int(input())
# counter = 0
# while num >=25:
#     counter +=1
#     num -= 25
# while num>=10:
#     counter += 1
#     num -= 10
# while num>=5:
#     counter += 1
#     num -= 5
# while num>=1:
#     counter += 1
#     num -= 1
#
# print(counter)




print('Time from 13:41 to 13:45 -> 13:42, 13:43, 13:44')
# h1 = int(input())
# m1 = int(input())
# h2 = int(input())
# m2 = int(input())
#
# start = h1*60 + m1
# end = h2*60 + m2
#
# while start <= end:
#     h = start // 60
#     m = start % 60
#
#     if h < 10:
#         hh = '0' + str(h)
#     else:
#         hh = str(h)
#
#     if m < 10:
#         mm = '0' + str(m)
#     else:
#         mm = str(m)
#
#     print(hh + ':' + mm)
#     start += 1

print('\n7.6. is started - while + for usage in working with numbers')
# num = int(input('Enter a number: '))
# while num != 0:
#     last_digit = num % 10
#     ...
#     num = num // 10
#     print('The last digit of the number is:', last_digit)
#     print('Deleted number:', num)

print('Does number have 7')
# num = 1576
# has_seven = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven == True:
#     print('Yes')
# else:
#     print('No')

print('\nShow every number from left to right')
# num = int(input()) # 8619
# n = len(str(num))
# for i in range(1, n+1):
#     digit = num // 10 ** (n - i) % 10
#     print(i, 'the number is equal to: ', digit)

print('\nShow every number from right to left')
# num = 496
# while num != 0:
#     last_digit = num % 10
#     print(last_digit, end ='-')
#     num //= 10

print('\nShow number flipped/reflected 356 - 653')
# num = int(input())
# while num != 0:
#     last_digit = num % 10
#     first_digit = last_digit
#     print(first_digit, end='')
#     num //= 10

print('\nMax and Min number in number 2678319')
# num = 36782190
# last_digit = num % 10
# maximum = last_digit
# minimum = last_digit
# while num != 0:
#     last_digit = num % 10
#     if last_digit > maximum:
#         maximum = last_digit
#     if last_digit < minimum:
#         minimum = last_digit
#     num //= 10
# print(maximum, minimum)

print('''сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.''')
# num = int(input())
# lastnum = num % 10
# strnum = str(num)
# sumnum = 0
# collection = 0
# multiply = 1
# arithmetic = 0
# firstp = 1
# while num != 0:
#     numle = num % 10
#     sumnum += numle
#     multiply *= numle
#
#     collection += 1
#     firstp = num
#     num //= 10
#
# arithmetic = sumnum / len(strnum)
# sum = firstp + lastnum
# print(sumnum)
# print(collection)
# print(multiply)
# print(arithmetic)
# print(firstp)
# print(sum)

print('\nShow the 2nd number in number')
# num = int(input())
# strnum = str(num)
# collection = 0
# while num != 0:
#     numle = num % 10
#     collection += 1
#     if collection == len(strnum):
#         print(numle)
#     num //= 10

print('\nSHOW IF EVERY NUMBER IS EQUAL')
num = int(input('Enter a number: '))
strnum = str(num)
collection = 0
while num != 0:
    numle = num % 10
    num //= 10
    new = num % 10
    print('the numle is', new)
    if collection == len(strnum) - 1:
        new = numle


print('The collection is', collection)












