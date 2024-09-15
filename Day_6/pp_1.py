while True:
    action = input("Type add, show, edit, complete or exit: ").strip()

    match action:
        case 'add':
            file = open('File/task_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            task = input("Enter the task: ") + '\n'
            todo_list.append(task)

            file = open('File/task_list.txt', 'w')
            file.writelines(todo_list)
            file.close()
        case 'exit':
            break