import this # The Zen of Python
print('72/7 =', 72/7)
print('72//7 =', 72//7)
print('72%7 =', 72%7)

print(f"10 days are {10 * 24 * 60} minutes")

# Variables
to_seconds = 24 * 60 * 60
name_of_unit = "seconds"
print(f"10 days are {10 * to_seconds} {name_of_unit}")
print(f"30 days are {30 * to_seconds} seconds")
print(f"20 days are {20 * to_seconds} seconds")

# Functions + their parameters
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
