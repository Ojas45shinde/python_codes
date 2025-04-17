import tkinter as tk
from tkinter import messagebox
import json
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.filename = 'todo.json'
        self.tasks = self.load_tasks()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.list_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.save_tasks()
            self.list_tasks()
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = self.task_entry.get()
            if new_task:
                index = selected_index[0]
                self.tasks[index]['task'] = new_task
                self.save_tasks()
                self.list_tasks()
                self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.save_tasks()
            self.list_tasks()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = True
            self.save_tasks() 
            self.list_tasks()

    def list_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = '✓' if task['completed'] else '✗'
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
