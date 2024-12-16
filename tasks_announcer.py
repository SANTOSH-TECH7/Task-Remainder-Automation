import tkinter as tk
import os
import pyttsx3
import threading  # For concurrent execution of tasks

# Path to the tasks file
tasks_file = r"D:\Task_remainder\tasks.txt"

# Function to read tasks from the file
def read_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            tasks = file.read().strip()
        return tasks if tasks else "No tasks found for today!"
    return "No tasks found for today!"

# Function to announce tasks using pyttsx3 in a separate thread
def announce_tasks():
    tasks = read_tasks()

    def announce():
        engine = pyttsx3.init()
        engine.setProperty('rate', 140)  # Calm and composed tone
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Female voice
        engine.say(f"Hello Sir. This is Friday reporting. Today's tasks are: {tasks}")
        engine.runAndWait()

    threading.Thread(target=announce).start()

# Function to handle adding a new task
def handle_add_task():
    new_task = task_entry.get().strip()
    if new_task:
        with open(tasks_file, "a") as file:
            file.write(f"{new_task}\n")
        update_task_display()
        task_entry.delete(0, tk.END)
    else:
        task_status_label.config(text="Please enter a valid task!", fg="red")

# Function to update the task display in the GUI
def update_task_display():
    tasks = read_tasks()
    task_display.config(state=tk.NORMAL)
    task_display.delete("1.0", tk.END)  # Clear the current text
    task_display.insert(tk.END, tasks)
    task_display.config(state=tk.DISABLED)

# Create the GUI window
root = tk.Tk()
root.title("Friday Task Reminder")
root.geometry("600x450")
root.config(bg="#1e1e2f")  # Cyber-dark background

# Title Label
title_label = tk.Label(
    root, text="Friday Task Reminder", font=("Courier New", 20, "bold"), bg="#1e1e2f", fg="#33ff99"
)
title_label.pack(pady=10)

# Task Display Area
task_display = tk.Text(
    root, height=10, width=60, wrap="word", font=("Consolas", 14), bg="#1e1e2f", fg="#33ccff", bd=0, state=tk.DISABLED
)
task_display.pack(pady=10)
update_task_display()  # Initial display of tasks

# Task Entry Field
task_entry = tk.Entry(root, width=40, font=("Consolas", 14), bg="#262626", fg="#ffffff", insertbackground="white")
task_entry.pack(pady=5)

# Task Status Label
task_status_label = tk.Label(root, text="", font=("Consolas", 12), bg="#1e1e2f", fg="#33ff99")
task_status_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame, text="Add Task", font=("Consolas", 12), bg="#4caf50", fg="white", command=handle_add_task
)
add_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(
    button_frame, text="Exit", font=("Consolas", 12), bg="#f44336", fg="white", command=root.quit
)
exit_button.grid(row=0, column=1, padx=10)

# Automatically announce tasks and update display when the GUI starts
root.after(1000, lambda: [announce_tasks(), update_task_display()])  # Delay for initialization

# Run the GUI
root.mainloop()
