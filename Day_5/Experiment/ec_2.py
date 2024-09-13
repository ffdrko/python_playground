todo_list = []

while True:
    action = input("Type add or show or edit or complete or exit: ").strip()

    match action:
        case 'add':
            task = input("Enter the task: ")
            todo_list.append(task)

        case "show":
            for index, item in enumerate(todo_list):
                print(f"{index + 1}-{item}")

            print(f"The length of the list is {len(todo_list)}")
            print("End of list...")

        case 'edit':
            task_no = int(input("Enter the task number: "))
            todo_list[task_no - 1] = input("Enter the edited task: ")

        case 'complete':
            task_no = int(input("Enter the task number: "))
            print(f'{todo_list[task_no -1]} is done')
            todo_list.pop(task_no - 1)

        case 'exit':
            break

print("End of Operations...")