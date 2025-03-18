import os

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

print(f"{GREEN}Welcome to this app\nUse 1 to list all todos\nUse 2 to add a todo\nUse 3 to delete a todo\nUse 4 to edit a todo\nType 'exit' to quit{RESET}")

file_path = './todo-list.txt'
#Check file exists
if not os.path.exists(file_path):
    open(file_path, 'w').close()
#Show todo list
def list_todos(file_path):
    """ Lists all todos from the file. """
    if not os.path.exists(file_path):
        print(f"{RED}No todos found!{RESET}")
        return []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            print(f"{RED}No todos found!{RESET}")
            return []
        for index, line in enumerate(lines):
            print(f"{YELLOW}{index + 1}. {line.strip()}{RESET}")
        return lines
#delete todo
def delete_todo(todo, todos):
    """ Deletes a specific todo by its index. """
    try:
        todo = int(todo) - 1
        if todo < 0 or todo >= len(todos):
            print(f"{RED}Invalid line number. Please try again.{RESET}")
            return
        with open(file_path, 'w') as file:
            for index, line in enumerate(todos):
                if index != todo:
                    file.write(line)
        print(f"{GREEN}Line {todo + 1} has been removed.{RESET}")
        list_todos(file_path)
    except ValueError:
        print(f"{RED}Invalid input. Please enter a valid number.{RESET}")
#edit todo
def edit_todo(todo,todos):
    """ Edits a specific todo by its index. """
    try:
        todo = int(todo)-1
        if todo < 0 or todo >= len(todos):
            print(f"{RED}Invalid line number. Please try again.{RESET}")
            return
        print(f"{GREEN}Enter the new text for this todo:{RESET}")
        new_todo = input().strip()
        if not new_todo:
            print(f"{RED}Todo cannot be empty.{RESET}")
            return
        todos[todo] = new_todo + "\n"
        with open(file_path, 'w') as file:
            file.writelines(todos)
        print(f"{GREEN}Line {todo + 1} has been updated.{RESET}")
        list_todos(file_path)
    except ValueError:
        print(f"{RED}Invalid input. Please enter a valid number.{RESET}")
# Get Valid Input
def get_valid_input(prompt, validation_fn):
    """ Repeatedly prompts for input until it passes the validation function. """
    while True:
        user_input = input(prompt)
        if validation_fn(user_input):
            return user_input
        else:
            print(f"{RED}Invalid input. Please try again.{RESET}")

# Validation Functions
def is_valid_number(num_str, max_value):
    """ Checks if the input is a valid number within the range of todos. """
    try:
        num = int(num_str)
        if 1 <= num <= max_value:
            return True
    except ValueError:
        pass
    return False
#start program
while True:
    command = input(f"\n{YELLOW}Enter a command: {RESET}")

    if command == "" or command.lower() == "exit":
        break
    elif command == "1":
        list_todos(file_path)
    elif command == "2":
        todo = input(f"{GREEN}Enter your todo: {RESET}").strip()
        if todo:
            with open(file_path, 'a') as file:
                file.write(todo + "\n")
            print(f"{GREEN}Your todo has been added to the list.{RESET}")
            list_todos(file_path)
        else:
            print(f"{RED}Todo cannot be empty.{RESET}")
    elif command == "3":
        todos = list_todos(file_path)
        if todos:
            todo = get_valid_input(f"{GREEN}Which line do you want to delete? Enter the number: {RESET}", 
                                   lambda x: is_valid_number(x, len(todos)))
            delete_todo(todo, todos)
    elif command == "4":
        todos = list_todos(file_path)
        if todos:
            todo = get_valid_input(f"{GREEN}Which todo do you want to edit? Enter the number: {RESET}", 
                                   lambda x: is_valid_number(x, len(todos)))
            edit_todo(todo, todos)

