course_name = "Python Programming"
print(len(course_name))        # 18
print(course_name[0])          # P
print(course_name[-1])         # g
print(course_name[0:3])        # Pyt
print(course_name[0:])         # Python Programming
print(course_name[:3])          # Python Programming
print(course_name[:])           # Python Programming


# string methods
course = "  Python \"Programming\""
print(course.upper())          # PYTHON "PROGRAMMING"
print(course.lower())          # python "programming"
print(course.title())          # Python "Programming"
print(course.strip())          # Python "Programming"
print(course.find("gram"))       # 13
print(course.replace("P", "J"))  # Jython "Jrogramming"
print("gram" in course)          # True
print("John" not in course)          # True
print('original string:', course)

# contatination
first = "John"
last = "Smith"
full_name = f"{len(first)} {last} {2 + 2}"
print(full_name)              # 4 Smith 4

# working with numbers
print(round(2.9))          # 3
print(abs(-2.9))           # 2.9

# # type conversion
# x = int(input("x: "))
# y = x + 1
# print(f"x: {x}, y: {y}")

# conditional statements
temperature = 15
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")
print("Enjoy your day")

# ternary operator
age = 12
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# logical operators
high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

# loops
for number in range(1, 10, 2):
    # Attempt 1 . , Attempt 2 .. , Attempt 3 ...
    print("Attempt", number, number * ".")

# for else
successful = True
for number in range(3):
    print("Attempt", number)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# iterables
for x in "Python":
    print(x)
for x in [1, 2, 3, 4, 5]:
    print(x)

# while loop
number = 100
while number > 0:
    print(number)
    number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# # infinite loop
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

print("even Numbers from 1 to 10")
count = 0
for number in range(2, 10, 2):
    print(number)
    count += 1
print(f"We have {count} even numbers")

for number in range(1, 10):
    if number % 2 == 0:
        print(number)

# functions


def greet_user(name):
    print("Hi there")
    print(f"Hi {name}:)")


greet_user("John")

# arguments and parameters


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet("John", "Smith")

# types of functions


def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("John")
print(message)

# keyword arguments


def increment(number, by):
    return number + by


print(increment(2, by=1))

# default arguments


def incremental(number, by=1):
    return number + by


print(incremental(2, 5))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
