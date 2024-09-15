while True:
    action = input("Type add, show, edit, complete, exit: ").strip()

    match action:
        case 'add':
            task = input("Enter the task: ") + '\n'

            file = open('Files/task_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(task)

            file = open('Files/task_list.txt', 'w')
            file.writelines(todo_list)
            file.close()

        case 'show':
            file = open('Files/task_list.txt', 'r')
            todo_list = file.readlines()
            file.close()

            for index, task in enumerate(todo_list):
                print(f"{index + 1}-{task.strip('\n')}")

        case 'exit':
            break