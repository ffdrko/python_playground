while True:
    action = input("Type add, show, edit, complete, exit:").strip()

    match action:
        case 'add':
            task = input("Enter the task: ") + '\n'

            with open('file/task.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list.append(task)

            with open('file/task.txt', 'w') as file:
                file.writelines(todo_list)

        case 'show':
            with open('file/task.txt', 'r') as file:
                todo_list = file.readlines()

            for index, task in enumerate(todo_list):
                print(f"{index+1}-{task.strip('\n')}")

        case 'exit':
            break