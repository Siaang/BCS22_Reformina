class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def menu(self):
        while True:
            # shows the options that can be used on the program
            self.option = int(input("Palindrome Checker = 1 | Exit = 2\nWhat would you like to do?: "))

            if self.option == 1:
                # asks user to input a sentence
                user_input = input("Enter a sentence: ")

                self.top = None

                for char in user_input:
                    # pushes the input onto the stack
                    self.push(char)

                if self.is_palindrome(user_input):
                    # output when the sentence is a palindrome
                    print(f"Cleaned sentence: {self.checker(user_input)}")
                    print(f"Your sentence: {user_input} is a palindrome!")

                else:
                    # output when the sentence is not a palindrome
                    print(f"Cleaned sentence: {self.checker(user_input)}")
                    print(f"Your sentence: {user_input} is not a palindrome.")

            else:
                # exits the program
                print("Exiting program...")
                break

    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

    def checker(self, data):
        # compares the sentence you wrote from the reverse sentence
        check = ""
        for char in data:
            if char.isalpha():
                check += char.lower()
        return check

    def is_palindrome(self, data):
        # checks if the sentence is a palindrome
        check = self.checker(data)
        return check == check[::-1]

s = Stack()
# shows a welcome message
print("=" * 7 + "Welcome to the Palindrome Checker!" + "=" * 7)

# used to access the menu function
s.menu()
