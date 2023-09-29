"""Instructions: Write a python program that will compute for the bonus using the specifications stated
T & M group of companies gives loyalty bonus to its employee based on their number of years of service and their salary.
        Years of service
            5 = 5%,
            10 = 100%,
            15 = 150%,
            20 = 200%
"""

def userInput():
    print("To view your salary loyalty bonus please provide the need information below")
    salary = (int(input("Enter your salary to compute your bonus: ")))
    years = (int(input("Enter the number of years you have worked here: ")))

    if years < 5:
        print("You have not worked here long enough to receive a loyalty bonus")
    else:
        if years >= 5 and years < 10:
            salaryamnt = salary / 10
            bonus = salaryamnt / 2
            result(bonus,salary)

        if years >= 10 and years < 15:
            bonus = salary * 1
            result(bonus,salary)

        if years >= 15 and years < 20:
            bonus = salary * 2
            result(bonus,salary)

        if years >= 20:
            bonus = salary * 4
            result(bonus,salary)

def result(bonus, salary):
    total = bonus + salary
    print(f"The amount of loyalty bonus you will receive is PHP {bonus}")
    print(f"The total amount of salary you will receive is {total}")

userInput()

#This program's time complexity is 0(1)
