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
das