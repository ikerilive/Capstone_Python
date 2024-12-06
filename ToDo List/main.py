import json
from tkinter import *
from tkinter import messagebox


# ---------------------------- FUNCTIONS ------------------------------- #

# Load tasks from JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save tasks to JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showinfo(title="Oops", message="Task cannot be empty!")
        return

    if task in tasks:
        messagebox.showinfo(title="Error", message="Task already exists!")
        return

    tasks[task] = "Pending"
    save_tasks()
    refresh_tasks()
    task_entry.delete(0, END)


# Mark a task as completed
def complete_task():
    selected_task = task_listbox.get(ACTIVE)
    if not selected_task:
        messagebox.showinfo(title="Oops", message="No task selected!")
        return

    tasks[selected_task] = "Completed"
    save_tasks()
    refresh_tasks()


# Delete a task
def delete_task():
    selected_task = task_listbox.get(ACTIVE)
    if not selected_task:
        messagebox.showinfo(title="Oops", message="No task selected!")
        return

    tasks.pop(selected_task, None)
    save_tasks()
    refresh_tasks()


# Refresh the task list in the Listbox
def refresh_tasks():
    task_listbox.delete(0, END)
    for task, status in tasks.items():
        task_listbox.insert(END, f"{task} - {status}")


# ---------------------------- UI SETUP ------------------------------- #

# Load existing tasks
tasks = load_tasks()

# Initialize main window
window = Tk()
window.title("To-Do List Manager")
window.config(padx=50, pady=50)

# Labels
task_label = Label(text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)

# Entries
task_entry = Entry(width=40)
task_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Buttons
add_button = Button(text="Add Task", command=add_task, width=12)
add_button.grid(row=1, column=0, padx=5, pady=5)

complete_button = Button(text="Complete Task", command=complete_task, width=12)
complete_button.grid(row=1, column=1, padx=5, pady=5)

delete_button = Button(text="Delete Task", command=delete_task, width=12)
delete_button.grid(row=1, column=2, padx=5, pady=5)

# Task Listbox
task_listbox = Listbox(height=15, width=60)
task_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Initial Load
refresh_tasks()

# Run the application
window.mainloop()
