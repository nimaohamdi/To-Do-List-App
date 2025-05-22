import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        tasks.remove(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")
root.config(bg="#fafafa")

# Entry field
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Add button
add_btn = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_btn.pack(pady=5)

# Task list
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

# Delete button
delete_btn = tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white")
delete_btn.pack(pady=5)

root.mainloop()
