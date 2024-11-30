import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import os

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List App with Calendar")
root.geometry("400x500")

# Default credentials
DEFAULT_USERNAME = "user1"
DEFAULT_PASSWORD = "password"

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())

# Function to save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to show a specific frame
def show_frame(frame):
    frame.tkraise()

# Function to validate login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        open_home()  # Open the home frame if credentials are correct
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")

# Function to show the home page
def open_home():
    show_frame(home_frame)

# Function to open add task page
def open_add_task():
    show_frame(add_task_frame)
    update_task_listbox(task_listbox_add)

# Function to open delete task page
def open_delete_task():
    show_frame(delete_task_frame)
    update_task_listbox(tasks_listbox_delete)

# Function to open view tasks page
def open_view_tasks():
    show_frame(view_task_frame)
    filter_var.set("Today")  # Set dropdown to "Today"
    filter_tasks()  # Filter tasks to show only today's tasks

# Function to add a task with an optional date
def add_task():
    task = task_entry.get()
    selected_date = cal.get_date()
    if task:
        task_with_date = f"{task} (Due: {selected_date})"
        tasks.append(task_with_date)
        save_tasks()  # Save updated tasks to file
        update_task_listbox(task_listbox_add)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete selected tasks
def delete_task():
    selected_indices = tasks_listbox_delete.curselection()
    if not selected_indices:
        messagebox.showwarning("Selection Error", "Please select at least one task to delete.")
        return

    # Confirm deletion
    if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected task(s)?"):
        for index in reversed(selected_indices):  # Reverse to avoid re-indexing issues
            tasks.pop(index)
        save_tasks()  # Save updated tasks to file
        update_task_listbox(tasks_listbox_delete)

# Function to update a task listbox with current tasks
def update_task_listbox(listbox, filter_func=None):
    listbox.delete(0, tk.END)
    sorted_tasks = sort_tasks_by_date(tasks, filter_func)  # Sort tasks by date
    for task in sorted_tasks:
        listbox.insert(tk.END, task)

# Function to filter tasks in the view task page based on selected filter
def filter_tasks():
    selected_filter = filter_var.get()
    today_date = datetime.now().strftime("%Y-%m-%d")
    if selected_filter == "Today":
        update_task_listbox(task_listbox_view, filter_func=lambda task: f"Due: {today_date}" in task)
    else:  # All
        update_task_listbox(task_listbox_view)

# Function to close the app
def close_app():
    save_tasks()  # Save tasks to file before closing
    root.quit()

# Helper function to sort tasks by date
def sort_tasks_by_date(tasks, filter_func=None):
    # Extract date from task and sort
    def get_task_date(task):
        try:
            date_str = task.split("Due: ")[1].strip(")")
            return datetime.strptime(date_str, "%Y-%m-%d")
        except (IndexError, ValueError):
            return datetime.max  # If date parsing fails, put it at the end

    # Filter tasks if filter_func is provided
    filtered_tasks = [task for task in tasks if filter_func is None or filter_func(task)]
    # Sort tasks by extracted date
    return sorted(filtered_tasks, key=get_task_date)

# Initialize task list and load tasks from file
tasks = []
load_tasks()

# Define frames
login_frame = tk.Frame(root)
home_frame = tk.Frame(root)
add_task_frame = tk.Frame(root)
delete_task_frame = tk.Frame(root)
view_task_frame = tk.Frame(root)

# Layout all frames in the same location
for frame in (login_frame, home_frame, add_task_frame, delete_task_frame, view_task_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Login Frame
login_label = tk.Label(login_frame, text="Login", font=("Arial", 16))
login_label.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=10)

# Home Frame
home_label = tk.Label(home_frame, text="Welcome to the To-Do List App", font=("Arial", 16))
home_label.pack(pady=20)

add_task_button = tk.Button(home_frame, text="Add Tasks", command=open_add_task, width=20)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(home_frame, text="Delete Tasks", command=open_delete_task, width=20)
delete_task_button.pack(pady=5)

view_task_button = tk.Button(home_frame, text="View Tasks", command=open_view_tasks, width=20)
view_task_button.pack(pady=5)

close_button = tk.Button(home_frame, text="Close App", command=close_app, width=20)
close_button.pack(pady=20)

# Add Task Frame
add_task_label = tk.Label(add_task_frame, text="Add Task", font=("Arial", 16))
add_task_label.pack(pady=10)

task_entry = tk.Entry(add_task_frame, width=40)
task_entry.pack(pady=5)

# Calendar widget to select task date
cal = Calendar(add_task_frame, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=10)

add_task_action_button = tk.Button(add_task_frame, text="Add Task", command=add_task)
add_task_action_button.pack(pady=5)

home_button_from_add = tk.Button(add_task_frame, text="Home", command=open_home)
home_button_from_add.pack(pady=5)

# Task listbox in Add Task frame to display current tasks
task_listbox_add = tk.Listbox(add_task_frame, width=40, height=10)
task_listbox_add.pack(pady=10)

# Delete Task Frame
delete_task_label = tk.Label(delete_task_frame, text="Delete Task", font=("Arial", 16))
delete_task_label.pack(pady=10)

# Listbox with multiple selection mode enabled
tasks_listbox_delete = tk.Listbox(delete_task_frame, width=40, height=15, selectmode="multiple")
tasks_listbox_delete.pack(pady=10)

delete_task_button_action = tk.Button(delete_task_frame, text="Delete Selected Task(s)", command=delete_task)
delete_task_button_action.pack(pady=5)

home_button_from_delete = tk.Button(delete_task_frame, text="Home", command=open_home)
home_button_from_delete.pack(pady=5)

# View Task Frame
view_task_label = tk.Label(view_task_frame, text="View Tasks", font=("Arial", 16))
view_task_label.pack(pady=10)

# Dropdown for selecting task filter
filter_var = tk.StringVar(value="Today")
filter_dropdown = tk.OptionMenu(view_task_frame, filter_var, "Today", "All", command=lambda _: filter_tasks())
filter_dropdown.pack(pady=5)

# Listbox to display tasks based on filter
task_listbox_view = tk.Listbox(view_task_frame, width=40, height=15)
task_listbox_view.pack(pady=10)

home_button_from_view = tk.Button(view_task_frame, text="Home", command=open_home)
home_button_from_view.pack(pady=5)

# Show the login frame initially
show_frame(login_frame)

# Start the main event loop
root.mainloop()