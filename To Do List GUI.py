import tkinter as tk
from tkinter import messagebox
import json
import os

# Initialize an empty dictionary to store tasks
tasks = {}
task_id_counter = 1  # Counter to assign unique IDs to tasks

# Load tasks from a file if it exists
def load_tasks():
    global task_id_counter
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file)
            global tasks
            tasks = data["tasks"]
            task_id_counter = data["task_id_counter"]
            refresh_task_list()

# Save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump({"tasks": tasks, "task_id_counter": task_id_counter}, file)

# Function to add a new task
def add_task():
    global task_id_counter
    description = description_entry.get()
    priority = priority_entry.get().lower()
    if description and priority:
        tasks[task_id_counter] = {
            "description": description,
            "priority": priority,
            "status": "pending"
        }
        task_listbox.insert(tk.END, f"ID: {task_id_counter} | {description} | Priority: {priority} | Status: pending")
        task_id_counter += 1
        description_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        save_tasks()  # Save after adding
    else:
        messagebox.showwarning("Input Error", "Please enter both a description and priority level.")

# Function to complete a task
def complete_task():
    try:
        task_id = int(task_id_entry.get())
        if task_id in tasks:
            tasks[task_id]["status"] = "completed"
            refresh_task_list()
            save_tasks()  # Save after completing
            messagebox.showinfo("Success", f"Task {task_id} marked as completed.")
        else:
            messagebox.showerror("Error", "Task ID not found.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid task ID.")

# Function to update a task
def update_task():
    try:
        task_id = int(task_id_entry.get())
        if task_id in tasks:
            description = description_entry.get()
            priority = priority_entry.get().lower()
            if description:
                tasks[task_id]["description"] = description
            if priority:
                tasks[task_id]["priority"] = priority
            refresh_task_list()
            save_tasks()  # Save after updating
            messagebox.showinfo("Success", f"Task {task_id} updated.")
        else:
            messagebox.showerror("Error", "Task ID not found.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid task ID.")

# Function to delete a task
def delete_task():
    try:
        task_id = int(task_id_entry.get())
        if task_id in tasks:
            del tasks[task_id]
            refresh_task_list()
            save_tasks()  # Save after deleting
            messagebox.showinfo("Success", f"Task {task_id} deleted.")
        else:
            messagebox.showerror("Error", "Task ID not found.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid task ID.")

# Function to display all tasks
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task_id, details in tasks.items():
        task_listbox.insert(tk.END, f"ID: {task_id} | {details['description']} | Priority: {details['priority']} | Status: {details['status']}")

# Initialize GUI window
root = tk.Tk()
root.title("To-Do List")

# Task Description
tk.Label(root, text="Description:").grid(row=0, column=0)
description_entry = tk.Entry(root, width=30)
description_entry.grid(row=0, column=1)

# Priority
tk.Label(root, text="Priority (low, medium, high):").grid(row=1, column=0)
priority_entry = tk.Entry(root, width=30)
priority_entry.grid(row=1, column=1)

# Task ID
tk.Label(root, text="Task ID:").grid(row=2, column=0)
task_id_entry = tk.Entry(root, width=30)
task_id_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Task", command=add_task).grid(row=3, column=0, pady=5)
tk.Button(root, text="Complete Task", command=complete_task).grid(row=3, column=1, pady=5)
tk.Button(root, text="Update Task", command=update_task).grid(row=4, column=0, pady=5)
tk.Button(root, text="Delete Task", command=delete_task).grid(row=4, column=1, pady=5)
tk.Button(root, text="Refresh List", command=refresh_task_list).grid(row=5, column=0, pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=80, height=10)
task_listbox.grid(row=6, column=0, columnspan=2)

# Load tasks on startup
load_tasks()

# Run the GUI
root.mainloop()
