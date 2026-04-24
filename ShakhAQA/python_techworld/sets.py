from ShakhAQA.python_techworld.lists import my_list

my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)


my_list = ["January", "February", "March", "January"]
my_list.remove("January")
print(my_list)