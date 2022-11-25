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
    TASKS_LIST = []
    TASK_ID = 0
    COMPLETED_TASKS = 0
    while True:
        print(
            f"Welcome to PyToDo\nHere's your task list:{TASKS_LIST}")
        print(f"Today you managed to complete {COMPLETED_TASKS} tasks")
        print("What would you like to do?")
        print("1. Add new task")
        print("2. Complete existing task")
        user_input = input()
        match user_input:
            case '1':
                new_title = input("What's the task title?\t")
                new_description = input("What's the task description?\t")
                new_task = Task(False, new_title, new_description)
                TASK_ID = TASK_ID + 1
                TASKS_LIST.append(new_task)
            case '2':
                search_id = input("What's the task number?")
                try:
                    search_id = int(search_id)
                    TASKS_LIST[search_id].is_completed = True
                    COMPLETED_TASKS = COMPLETED_TASKS + 1
                except ValueError:
                    print("This task doesn't exist")
