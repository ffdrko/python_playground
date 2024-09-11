todo_list = []

while True:
    action = input("Type add or show or exit: ").strip()

    match action:
        case 'add':
            task = input("Enter the task: ")
            todo_list.append(task)
        case 'show' | 'display':
            for task in todo_list:
                print(task)
        case 'exit':
            break
        case _:
            print("Wrong input!!!")

print("Operation ends.....")