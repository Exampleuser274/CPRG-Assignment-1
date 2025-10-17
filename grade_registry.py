'''
Names: Ryan Dezall
Description: This program allows users to enter a student's name and however many grades they want to for that person and
get the overall GPA. It allows the user to do this for multiple students at a time. It runs until told to stop and once it's stopped
in prints out the students names with their grades alongside them

Parameters
continue_program : input
    Gets input by the user to continue the Grade Registry Program or to stop it

num : float
    Stores a temporary value for grade to add it to total grade for student

student_name: dictionary
    Write what it does here

'''# We are trying to figure out the gpa for multiple students
# Each student will have one name and multiple grades
# Ask to enter grades until the user types "-1"

#Initial question to get true or false value to run
#Initial value section
print("Welcome to the Grade Registry Program")
continue_program = input("Would you like to add a new student? y(yes),n(no)\n")
grade = 0
student_names = {}
    
#major while loop
# the in from the for loop for the while loop
# .lower so that no matter input put in it would change it to lowercase and allow program to run as long as word or letter was the same.
while continue_program.lower() in ("yes", "y"):
    name = input("Enter student's name; \n")
    sum = 0
    count = 0
    num = 0
    print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")

    while num != -1:
        count += 1
        sum += num
        num = float(input(""))  # float instead of int for none whole numbers
    if sum > 0:
        count -= 1
        gpa = sum / count
    else:
        gpa = 0

    student_names[name] = gpa #this links them together
    continue_program = input("Would you like to add a new student? y(yes), n(no) \n")

    #while loop at end to determine if it continues or not
    while continue_program.lower() not in ("yes", "y") and continue_program.lower() not in ("no", "n"):
        print("Incorrect Input, please enter y(yes), n(no)")
        continue_program = input("Would you like to add a new student? y(yes), n(no) \n")
    if continue_program.lower() in ("no", "n"):
        break
    

print("This is the list of students in the system, and their corresponding accumulative GPA")
#I orginally did something else but changed it to dictionary as per the instructions
#I used .items because there is a potential fault in not linking the gpa and names together as I did before
#If a name was deleted it would mess up values
#I changed it so the names link together with their values
for name, gpa in student_names.items(): 
    print(f"{name} {gpa:.2f}")
