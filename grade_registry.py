# We are trying to figure out the gpa for multiple students
# Each student will have one name and multiple grades
# Ask to enter grades until the user types "-1"

print("Welcome to the Grade Registry Program")
continue_program = input("Would you like to add a new student? y(yes),n(no))\n")
grade = 0
student_names = {}
    

while continue_program.lower() in ("yes", "y"):
    name = input("Enter student's name; \n")
    sum = 0
    count = 0
    num = 0
    print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")

    while num != -1:
        count += 1
        sum += num
        num = float(input(""))
    if sum > 0:
        count -= 1
        gpa = sum / count
    else:
        gpa = 0

    student_names[name] = gpa
    continue_program = input("Would you like to add a new student? y(yes), n(no) \n")
    while continue_program.lower() not in ("yes", "y") and continue_program.lower() not in ("no", "n"):
        print("Incorrect Input, please enter y(yes), n(no)")
        continue_program = input("Would you like to add a new student? y(yes), n(no) \n")
    if continue_program.lower() in ("no", "n"):
        break
    

print("This is the list of students in the system, and their corresponding accumulative GPA")
for name, gpa in student_names.items():
    print(f"{name} {gpa:.2f}")
    
    
'''if num > 4 or num < 0 and num != -1:
            print("Please enter a valid GPA between 0 and 4")
            count -= 1
            sum -= num'''
