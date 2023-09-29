'''Input:                                                            Output:
- Name                                                               - Name
_ Q1                                                                 - Q1
- Q2                                                                 - Q2
- Q3                                                                 - Q3
- Final Exam                                                         - Final Exam
- Class Participation                                                - Class Participation
- (Loop prompt) Do you want to enter a new student records? Y/N      - Final Grade (qTotal * 0.4) + CP * 0.2) + (FE * 0.4)
                                                                     - Status (Passes / Failed) (Pass if >= 0.75))'''
from tabulate import tabulate


student_grades = []

def userInput():
    while True:
        question = input("Do you want to enter a new student record?Y/N: \n")

        inputgrds = [None] * 8
        if question == "Y":
            print("Please input the following")
            inputgrds[0] = input("Name: ")
            inputgrds[1] = int(input("Q1: "))
            inputgrds[2] =  int(input("Q2: "))
            inputgrds[3] = int(input("Q3: "))
            inputgrds[4] = int(input("Final Exam: "))
            inputgrds[5] = int(input("Class Participation: "))
            inputgrds[6] = (inputgrds[1] + inputgrds[2] + inputgrds[3] * 0.4) + (inputgrds[5] * 0.2) + (inputgrds[4] * 0.4)
            inputgrds[7] =  "Passed" if inputgrds[6] >= 75 else "Failed"

            student_grades.append(inputgrds)

        elif question == "N":
            print(" ─────── ⋆⋅☆⋅⋆ ────── ⋆⋅☆⋅⋆ ───These are your grades─── ⋆⋅☆⋅⋆ ────── ⋆⋅☆⋅⋆ ───────")
            gradeTable(student_grades)
            break
        else:
            print("Invalid please try again!")
            userInput()

def gradeTable(student_grades):
    headers = ["Name", "Q1", "Q2", "Q3", "Final Exam", "Class Participation", "Final Grade", "Result"]
    print(tabulate(student_grades, headers=headers, tablefmt="pretty"))


userInput()
