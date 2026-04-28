import datetime

user_input = input("enter your goal with a deadline separated by colon:\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]


deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.datetime.today()
calculation = deadline_date - current_date
hours_till = int(calculation.total_seconds() / 60 / 60)
# print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
# print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))


# calculate how many days from now till deadline



print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")

