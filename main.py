# Make .txt file with all the todos
# add id based on the previous one, else if no other id, id = 0
# Simple functions that do one thing
# Id is the line the task is in the text file
# Should the tasks be just removed when finished, or marked as finished

import tkinter
from tkinter import BooleanVar, IntVar, StringVar, ttk

__todo_file__ = "todo.txt"


def read_from_file(line: int):
    try:
        with open(__todo_file__, 'r', 0, "UTF-8") as file:
            return file.readline(line)
    except PermissionError:
        return "Couldn't read from file, maybe it doesn't exist"


def write_to_file(name: str, description: str):
    try:
        with open(__todo_file__, 'a', 0, "UTF-8") as file:
            with open(__todo_file__, 'r', 0, "UTF-8") as fr:
                identification = len(fr.readlines())
            file.write(
                f"{identification}. {name.lower()}; {description.lower()}")
        return "Saved"
    except PermissionError:
        return "Couldn't save to file, maybe no permissions to do so"


def add_task(name: str, description: str):
    try:
        write_to_file(name, description)
        return "Task added"
    except PermissionError:
        return "Couldn't add task"


def remove_task(content: str):
    try:
        with open(__todo_file__, "r", 0, "UTF-8") as file:
            lines = file.readlines()
        with open(__todo_file__, "w", 0, "UTF-8") as file:
            for line in lines:
                if line.strip("\n") != content.lower():
                    file.write(line)
        return "Task removed"
    except PermissionError:
        return "Couldn't remove task"


def complete_task(content: str):
    try:
        remove_task(content)
        return "Task added"
    except PermissionError:
        return "Couldn't complete task"


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Pytodo")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    completed = BooleanVar()
    completed_label = ttk.Label(root, text='Completed')
    completed_label.grid(column=1, row=1)
    number = IntVar()
    number_label = ttk.Label(root, text='Number')
    number_label.grid(column=2, row=1)
    title = StringVar()
    title_label = ttk.Label(root, text='Title')
    title_label.grid(column=3, row=1)
    description = StringVar()
    description_label = ttk.Label(root, text='Description')
    description_label.grid(column=4, row=1)
