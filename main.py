""" Write code that asks the user to provide a score for an exam as input, and checks what grade the score is
associated with. (Example: a score higher than 90 is an A.)"""

# gather input from the user
grade = int(input("enter a grade:\n"))

# checking my work to see if the proper data type is set which is confirmed set to int
print(type(grade))

# here i will create my conditions to group grades
if grade >= 90:
    print("you have an A")
elif grade >= 80:
    print("you have a B")
elif grade >= 70:
    print("you have a C")
elif grade >= 60:
    print("you have a D")
elif grade >= 0 or grade <= 59:
    print("you have a F")
else:
    print("enter a valid input")
    exit()
