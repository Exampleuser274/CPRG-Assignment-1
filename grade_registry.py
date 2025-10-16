# We are trying to figure out the gpa for multiple students
# Each student will have one name and multiple grades
# Ask to enter grades until the user types "-1"

print("Welcome to the Grade Registry Program")
continue_program = "yes"
grade = 0
student_names = []
gpas = []

while continue_program == "yes":
    name = input("Please enter student name: \n")
    sum =0
    count =0
    num = 0
    print("Enter student GPA for each subject. Enter -1 to finish entering GPA.")

    while num != -1:
        count += 1
        sum += num
        num = float(input(""))
    if sum > 0:
        count -= 1
        gpa = sum / count
    else:
        gpa = 0

    student_names.append(name)
    gpas.append(gpa)
    continue_program = input("Do you want to enter another student? Type yes or no: \n")
    while continue_program != "yes" and continue_program != "no":
        print("Please enter a valid response (yes or no)")
        continue_program = input("Do you want to enter another student? Type yes or no: \n")
    if continue_program == "no":
        break
    

print("This is the list of students in the system, and their corresponding accumulative GPA")
for name, gpa in zip(student_names, gpas):
    print(name, gpa)


    
    
'''if num > 4 or num < 0 and num != -1:
            print("Please enter a valid GPA between 0 and 4")
            count -= 1
            sum -= num'''
