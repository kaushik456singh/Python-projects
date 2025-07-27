def show_tasks():
    with open("todo.txt", "r") as f:
        print(f.read())
def add_task(task):
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
while True:
    choice = input("1. Add Task 2. Show Tasks 3. Exit: ")
    if choice == '1':
        add_task(input("Enter task: "))
    elif choice == '2':
        show_tasks()
    else:
        break