#------------------------------------------------------------------#
# Topic 2.  Strings and concatenation. Task 3

# first = input("Please, enter first word: ")
# second = input("Please, enter second word: ")
# print(first + " " + second.lower())

#------------------------------------------------------------------#
# Topic 3. Operators, Expressions

# Task 3
# a = input("Enter the number: ")
# print(f"After the number {int(a)} comes the number {int(a) + 1}. \nUp to number {int(a)} comes the number {int(a)-1} ")

# Task 5
# m = input("Please, enter the number of minutes: ")
# hours = int(m) // 60
# min = int(m) % 60
# print(f"Hours: {hours}, minutes: {min}")

# Task 6
# n = input("Please, enter the first number: ")
# m = input("Please, enter the second number: ")
# print((int(n) % 100) + (int(m) % 100))

#------------------------------------------------------------------#
# Topic 6. Operator while

# 6.3 Task 1
# temperature = int(input("Enter the temperature: "))
# distance = 0
#
# while temperature > 15:
#     distance += 20
#     temperature -= 2
#     if temperature <= 15:
#         break
#     distance += 10
#
# print("Спортсмен прошел", distance, "метров.")

#------------------------------------------------------------------#
# Topic 7. Cycle for

# 7.6 Task 7

# First variant without any checks
# amount_of_cards = int(input("Please, enter the amount of cards: "))
# total_cards = sum(range(1, amount_of_cards + 1))
#
# for i in range(amount_of_cards - 1):
#     total_cards -= int(input("Enter the number of the remaining card: "))
# print(f" The missing card is: {total_cards}")









