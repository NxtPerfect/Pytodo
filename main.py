import tkinter
from tkinter import StringVar, Button, Frame, Label, Listbox, Scrollbar, Tk, Entry, END, BOTTOM, RIGHT, BOTH, LEFT, ANCHOR

TASKS_LIST = []

root = Tk()
root.title("PyToDo")
root.geometry("400x600+400+100")
root.resizable(False, False)


def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a', 1, "UTF-8") as taskfile:
            taskfile.write(f"\n{task}")
        TASKS_LIST.append(task)
        listbox.insert(END, task)


def delete_task():
    task = str(listbox.get(ANCHOR))
    if task in TASKS_LIST:
        TASKS_LIST.remove(task)
        with open("tasklist.txt", 'w', 1, "UTF-8") as taskfile:
            for task in TASKS_LIST:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)


def open_task_file():
    try:
        with open("tasklist.txt", 'r', 1, "UTF-8") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                TASKS_LIST.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        with open("tasklist.txt", 'w', 1, "UTF-8") as taskfile:
            file = taskfile
        file.close()


if __name__ == "__main__":
    # Top Text
    heading = Label(root, text="All tasks",
                    font="ubuntu 20 bold", bg="#aa6f73")
    heading.place(x=140, y=20)

    # Main
    frame = Frame(root, width=400, height=50, bg="white")
    frame.place(x=0, y=180)

    task = StringVar()
    task_entry = Entry(frame, width=18, font="ubuntu 20", bd=0)
    task_entry.place(x=10, y=7)
    task_entry.focus()

    button = Button(frame, text="Add", font="ubuntu 20 bold",
                    width=5, bg="#aa6f73", fg="#fff", bd=0, command=add_task)
    button.place(x=300, y=0)

    # Task List
    frame1 = Frame(root, bd=3, width=700, height=280, bg="#66545e")
    frame1.pack(pady=(230, 0))

    listbox = Listbox(frame1, font=('ubuntu', 12),
                      width=40, height=12, bg="#66545e", fg="white", cursor="hand2", selectbackground="#a39193")
    listbox.pack(side=LEFT, fill=BOTH, padx=2)

    scrollbar = Scrollbar(frame1)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    open_task_file()

    # Delete task
    delete = Button(root, text="Delete task",
                    font="ubuntu 20 bold", bg="#aa6f73", command=delete_task)
    delete.pack(side=BOTTOM, pady=13)

    root.mainloop()
