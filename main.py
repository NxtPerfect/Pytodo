# Make .txt file with all the todos
# add id based on the previous one, else if no other id, id = 0
# Simple functions that do one thing
# Id is the line the task is in the text file
# Should the tasks be just removed when finished, or marked as finished

import tkinter
from tkinter import BooleanVar, IntVar, StringVar, ttk


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data '{target_node_data}' wasn't found")


LinkedList.__doc__ = "Main class used to operate on nodes storing tasks data"
LinkedList.add_first.__doc__ = "Adds element on the first position"
LinkedList.add_last.__doc__ = "Adds element on the last position"
LinkedList.remove_node.__doc__ = "Removes node with provided data"


class Node:
    data = ''
    next = None

    def __init__(self, __title="Title", __description="Description") -> None:
        self.data = "\\Title// " + __title + "\\Description// " + __description
        self.next = None


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
