todo_list = []

while True:
    action = input("Type add or show or exit: ")

    match action:
        case 'add':
            task = input("Enter the task: ")
            todo_list.append(task)
        case 'show':
            print(todo_list)
        case 'exit':
            break

print("Operation ends.....")