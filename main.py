# Make .txt file with all the todos
# add id based on the previous one, else if no other id, id = 0
# Simple functions that do one thing
# Id is the line the task is in the text file
# Should the tasks be just removed when finished, or marked as finished


class Task:
    def __init__(self, is_completed: bool, title: str, description: str):
        try:
            if title.isalpha() and description.isalpha():
                self.is_completed = is_completed
                self.title = title
                self.description = description
        except (ValueError, TypeError, UnicodeError):
            pass


if __name__ == "__main__":
    tasks_list = []
    task_id = 0
    while True:
        print(
            f"Welcome to PyToDo\nHere's your task list:{tasks_list}")
        print("What would you like to do?")
        print("1. Add new task")
        print("2. Complete existing task")
        print("3. Remove completed tasks")
        user_input = input()
        match user_input:
            case '1':
                new_title = input("What's the task title?\t")
                new_description = input("What's the task description?\t")
                new_task = Task(False, new_title, new_description)
                task_id = task_id + 1
                tasks_list.append(new_task)
            case '2':
                search_id = input("What's the task number?")
                try:
                    search_id = int(search_id)
                    tasks_list.pop(int(search_id))
                except ValueError:
                    print("Search id isn't a valid number")
