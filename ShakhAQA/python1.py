print("helloworld")

# BASIC
# Variables

text = '\nPython!'
print(text*5)


# Input

# text_input = input("What text to Display?: ")
# print("There's your text: " + text_input)
# text_input2 = input("What will be the second name?: ")
# print("There's the second text: " + text_input2)


# String Concatenation

# name = input("What's your name?: ")
# print('Hi,', name, ". I'm Shah:)")
print('Well ' + 'Done')
# a = input('Enter first word: ')
# b = input('Enter second word: ')
# c = a + ' <-first & second-> ' + b
# print(c)


# Variables Features

name = 'Shakhzod'
surname = 'Ismailov'
first_number = '1'
temp = "Temporary data"
a, b, c = 'well', "it's", 'good'
print(a, b, c)



# Homework from info Above

# a = input("Enter 1st word: ")
# b = input("Enter 2nd word: ")
# print(a,b)
# c = a
# a = b
# b = c
# # a, b = b, c
# print(a,b)


# Numbers and Arithmetic Operations

print(3 / 2)
print(2 ** 5)
print(pow(2, 5))
a = 5
b = -40000
c = a + b
print(c)
print('Hi', 2)


# Arithmetic Priority 1st () -> ^ -> */

print(2 * 3 ** (3 - 1))
print((2 ** 3) ** 2)


# Enter number from Keyboard

# a = int(input('Enter number: '))
# d = '12'
# f = '23'
# c = int(d+f) + a
# print(c)


# divide = int & remainder

apples = 41
boxes = 3
full_boxes = apples // boxes
apples_left = apples - full_boxes * boxes
apples_left_1 = apples % boxes  # remainder
print("Number of boxes with apples: ", full_boxes)
print("Left apples without boxes: ", apples_left)
print("Left apples without boxes(with % formula): ", apples_left_1)
print(52 // 10)
print(52 % 10)
print(149 // 10)
print(149 % 10)


# += -= *= //= /= %=

products = 0
products += products + 100
print("New value:", products)
products += 10
print("New value:", products)
products += 15
print("New value:", products)
products += 15
print("New value:", products)