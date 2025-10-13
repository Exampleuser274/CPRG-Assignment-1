# We are trying to figure out the gpa for multiple students
# Each student will have one name and multiple grades
# Ask to enter grades until the user types "done"

print("Welcome to the Grade Registry Program")
continue_program = "Yes"
grade = 0
student_names = []
gpas = []

while continue_program == "Yes":
    name = input("Please enter student name: \n")
    sum =0
    count =0
    num = 0
    print("Enter student GPA for each subject. Enter -1 to finish:")

    while num != -1:
        count += 1
        sum += num
        num = float(input(""))
        if num > 4 or num < 0 and num != -1:
            print("Please enter a valid GPA between 0 and 4")
            count -= 1
            sum -= num
    if sum > 0:
        count -= 1
        gpa = sum / count
    else:
        gpa = 0

    student_names.append(name)
    gpas.append(gpa)
    continue_program = input("Do you want to enter another student? Type Yes or No: \n")
    while continue_program != "Yes" and continue_program != "No":
        print("Please enter a valid response (Yes or No)")
        continue_program = input("Do you want to enter another student? Type Yes or No: \n")
    if continue_program == "No":
        break
    

for name, gpa in zip(student_names, gpas):
    print(name, gpa)


    
    

