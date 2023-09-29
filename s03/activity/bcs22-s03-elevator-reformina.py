#Instructions: Create an elevator program using python in array
floorLevels = [0, 1, 2, 3, 4, 5, 6, 7]
floor = 0

def elevatorStart():
    userFloor = int(input("Which floor would you like to go to (0 to 7)? "))
    floorInput(userFloor)

def floorInput(userFloor):
    global floor
    if userFloor not in floorLevels:
        print("The floor you inputted doesn't exit, try again")
        return elevatorStart()
    else:
        print(f"We will now bring you to floor {userFloor}")
        while floor is not userFloor:
            print(f"You are currently in floor {floor}")
            if floor < userFloor:
                floor = floor + 1
            elif floor > userFloor:
                floor = floor - 1
            if floor == userFloor:
                print(f"You are now in your destination: floor {floor}")

while(True):
    elevatorStart()
