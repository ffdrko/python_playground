todo_list = []

while True:
    action = input("Type add, show or edit or exit: ").strip()

    match action:
        case 'add':
            task = input("Enter a task: ")
            todo_list.append(task)
        case 'show':
            for i in todo_list:
                print(i)
        case 'edit':
            todo_no = int(input("Enter the number of task for edit: "))
            todo_list[todo_no - 1] = input("Enter the edited task: ")
        case 'exit':
            break


print('End of Operation...')