import this # The Zen of Python
print('72/7 =', 72/7)
print('72//7 =', 72//7)
print('72%7 =', 72%7)

print(f"10 days are {10 * 24 * 60} minutes")

# variables
to_seconds = 24 * 60 * 60
name_of_unit = "seconds"
print(f"10 days are {10 * to_seconds} {name_of_unit}")
print(f"30 days are {30 * to_seconds} seconds")
print(f"20 days are {20 * to_seconds} seconds")

# functions + their parameters
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * to_seconds} {name_of_unit}")
    print(custom_message)
days_to_units(20, "Hello world")
days_to_units(10, "Great!")

# Scope
def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit) # global variable
    print(num_of_days) # local variable
    print(my_var)

scope_check(21)

print('\naccepting user input')
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * to_seconds} {name_of_unit}"
#
# my_var = days_to_units(20)
# print(my_var)
#
# user_input = int(input("Hey user, enter a number of days and I will convert it to seconds:\n"))
# calculated_value = days_to_units(user_input)
# print(calculated_value)

print('\nconditionals + boolean data type')
# def days_to_units(num_of_days):
#     print(type(num_of_days > 0))
#     if num_of_days > 0:
#         return f"{num_of_days} days are {num_of_days * to_seconds} seconds"
#     elif num_of_days == 0:
#         return "you entered 0"
#
# def validate_and_execute():
#     if user_input.isdigit():
#         user_input_number = int(user_input)
#         calculated_value = days_to_units(user_input_number)
#         print(calculated_value)
#     else:
#         print("Please enter a valid input.")
#
# user_input = (input("Hey user, enter a number of days and I will convert it to seconds:\n"))
# validate_and_execute()

print('\nnested if else')
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * to_seconds} seconds"
#
# def validate_and_execute():
#     if user_input.isdigit():
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered 0")
#     else:
#         return "your input is not a valid number. enter another one"
#
#
# user_input = (input("Hey user, enter a number of days and I will convert it to seconds:\n"))
# validate_and_execute()

print('\nerror handling with try/except')
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * to_seconds} seconds"
#
# def validate_and_execute():
#     try:
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered 0, enter a valid positive number")
#         else:
#             print("you entered a negative number, no conversion for you")
#
#     except ValueError:
#         print("your input is not a valid number. enter another one")
#
#
# user_input = (input("Hey user, enter a number of days and I will convert it to seconds:\n"))
# validate_and_execute()

print("\nwhile loops")
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * to_seconds} seconds"
#
# def validate_and_execute():
#     try:
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered 0, enter a valid positive number")
#         else:
#             print("you entered a negative number, no conversion for you")
#
#     except ValueError:
#         print("your input is not a valid number. enter another one")
#
# user_input = "input()"
# while user_input != "exit":
#     user_input = (input("Hey user, enter a number of days and I will convert it to seconds:\n"))
#     validate_and_execute()

print("\nlists & for loops")
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * to_seconds} seconds"
#
# def validate_and_execute():
#     try:
#         user_input_number = int(num_of_days_element)
#         # we want to do conversion only for positive integers
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("you entered 0, enter a valid positive number")
#         else:
#             print("you entered a negative number, no conversion for you")
#
#     except ValueError:
#         print("your input is not a valid number. enter another one")
#
# user_input = ""
# while user_input != "exit":
#     user_input = (input("Hey user, enter a number of days and I will convert it to seconds:\n"))
#     print(type(user_input.split(", ")))
#     print(user_input.split(", "))
#     for num_of_days_element in user_input.split(", "):
#         validate_and_execute()

print("\nsets")
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * to_seconds} seconds"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you")

    except ValueError:
        print("your input is not a valid number. enter another one")

user_input = ""
while user_input != "exit":
    user_input = (input("Hey user, enter a number of days and I will convert it to seconds:\n"))
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()

