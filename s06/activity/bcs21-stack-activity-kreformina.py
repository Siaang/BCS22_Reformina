class TaskManager:
    def __init__(self):
        self.stack = []

    def mytasks(self):
        option = input("1. Add tasks 〢 2. Mark tasks 〢 3. Display all tasks 〢 What would you like to do? ")

        if option == "1":
            self.add()
            self.use()

        elif option == "2":
            self.mark_task()
            self.use()

        elif option == "3":
            self.display()
            self.use()

        else:
            print("> Invalid input. Please try again.")
            self.mytasks()

    def add(self):
        print("> Please add a title and description of your task.")
        title = input("Title: ")
        desc = input("Description: ")
        task = {"Title": title, "Description": desc, "Status": False}
        print("> Successfully added to task list")
        self.stack.append(task)

    def mark_task(self):
        self.display()
        if not self.stack:
            print("> No tasks available to mark as completed.")
            return

        mark_task = int(input("> Which task would you like to mark as completed? ")) - 1
        if 0 <= mark_task < len(self.stack):
            task = self.stack.pop(mark_task)
            task["Status"] = True
            print("> This task has been marked as completed.")
            self.stack.insert(mark_task, task)
        else:
            print("> Invalid input, please try again.")

    def display(self):
        print("─── ⋆⋅☆⋅⋆ ───Your Current Tasks─── ⋆⋅☆⋅⋆ ───")
        for taskList, task in enumerate(self.stack, start=1):
            status = "Completed" if task["Status"] else "Incomplete"
            print(f"{taskList}. Title: {task['Title']}\n  Description: {task['Description']}\n  Status: {status}")

    def use(self):
        question = input("> Do you want to use the Task Manager again? ")

        if question.lower() == "yes":
            self.mytasks()
        elif question.lower() == "no":
            print("> Exiting task manager...")
        else:
            print("> Invalid input. Please try again.")
            self.use()

program = TaskManager()
print("─── ⋆⋅☆⋅⋆ ────── ⋆⋅☆⋅⋆ ───Welcome to Task Manager─── ⋆⋅☆⋅⋆ ────── ⋆⋅☆⋅⋆ ───")
program.mytasks()
