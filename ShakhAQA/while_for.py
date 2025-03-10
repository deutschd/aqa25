print('while & for - beginning')
print('while:\n')

counter = 0
total = 0
while counter < 5:
    counter += 1
    total += counter
print("total:", total)
print("counter:", counter)

print("PASSWORD IN WINDOWS\n")
# secret_info = "Python is a C framework"
# password = "cat"
# user_input = ''
# while user_input != password:
#     user_input = input("Enter your password: ")
# print("Welcome! Secret info:", secret_info)

limit = 5000
balance = 12000
while balance > limit:
    print('balance:', balance)
    expense = int(input("How much? "))
    balance -= expense
print("Done, you have", balance, "left")
