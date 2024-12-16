
# Friday Task Reminder

**Friday Task Reminder** is a Python-based Task Reminder application designed to help you manage your daily tasks efficiently. This application features a user-friendly graphical user interface (GUI) built with `tkinter`, and it includes automatic voice announcements of tasks using the `pyttsx3` library. The tasks are saved persistently to a file, allowing users to view and hear reminders about their tasks every time they open the app.

## Features

- **Task Management**: Easily add and view your tasks through the intuitive GUI.
- **Voice Announcement**: When the application is launched, tasks are automatically read aloud using text-to-speech functionality.
- **Persistent Storage**: All tasks are saved to a file (`tasks.txt`), allowing tasks to be carried over between sessions.
- **User-Friendly Interface**: A modern, dark-themed interface with clear task listings and input fields for ease of use.

## Requirements

To run this project, you need to have the following:

- **Python 3.x**: Make sure Python is installed on your computer. If it is not installed, you can download and install it from the official Python website: https://www.python.org/downloads/.
- **Required Libraries**:
  - **`tkinter`**: A standard Python library for building GUIs. It comes pre-installed with most Python distributions.
  - **`pyttsx3`**: A text-to-speech library to announce tasks aloud.

You can install the `pyttsx3` library using `pip` as shown below.

## File Structure

The project consists of the following files:

```
|-- tasks.txt               # A file that stores tasks persistently
|-- task_reminder.py        # Main Python script that runs the Task Reminder application
|-- tasks_announcer.bat     # A batch file to run the Python script without using the command line
|-- voice_check.py          # Script that handles voice output and task announcements
```

- **`tasks.txt`**: This text file stores your tasks. When you add a task, it gets saved here, and when you restart the application, the tasks are automatically loaded.
- **`task_reminder.py`**: This is the main Python script that runs the application. It contains the logic for displaying tasks and speaking them aloud.
- **`tasks_announcer.bat`**: A batch file that simplifies running the Python script by automatically launching it when you double-click it.
- **`voice_check.py`**: A helper script used to manage and control the voice announcements for tasks.

## Installation Instructions

### Step 1: Clone or Download the Repository

Clone or download this repository to your local machine. You can clone the repository using Git by running the following command in your terminal:

```bash
git clone https://github.com/SANTOSH-TECH7/Task-Remainder-Automation.git
```

Alternatively, you can download the ZIP file of the repository directly from GitHub and extract it to your desired location.

### Step 2: Install Required Python Libraries

Before running the application, you need to install the required Python libraries. Follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the repository is located.
3. Install the necessary Python libraries using `pip`:

```bash
pip install pyttsx3
```

The `tkinter` library is included in most Python distributions, so there is no need to install it separately.

### Step 3: Running the Application

There are two ways to run the application: directly via Python or using the batch file.

#### Option 1: Running the Python Script Directly

1. Open a terminal or command prompt.
2. Navigate to the directory where the project is located.
3. Run the following command to launch the Python application:

```bash
python task_reminder.py
```

This will start the **Friday Task Reminder** application. You will be able to add and view tasks, and they will be announced aloud when the application starts.

#### Option 2: Running the Batch File (Recommended for Ease)

If you prefer to run the application without using the command line, you can use the included batch file:

1. Double-click the `tasks_announcer.bat` file located in the project folder.
2. This will automatically launch the **Friday Task Reminder** application in a separate window.

The batch file handles the execution of the Python script and ensures everything runs smoothly with just one click.

## How to Use

1. **Launch the Application**: 
   - You can launch the app by either running the Python script directly or using the batch file (`tasks_announcer.bat`).
   
2. **Add Tasks**:
   - Once the application is launched, you will see a GUI with an input field at the bottom and two buttons: **Add Task** and **Exit**.
   - To add a new task, type the task description into the input field and click the **Add Task** button.
   - The task will then appear in the list above the input field and will be saved to `tasks.txt`.

3. **View Tasks**:
   - The tasks you add will be displayed in the main window of the application. Each time the app is launched, it will read the tasks aloud, and you can view them in the GUI.

4. **Voice Announcement**:
   - As soon as the application starts, it will automatically read out all the tasks in the list using the `pyttsx3` library. This feature ensures that you are reminded of your tasks immediately.

5. **Exit the Application**:
   - To close the application, simply click the **Exit** button.

## Troubleshooting

- If you encounter issues with voice announcements not working, ensure that you have installed the `pyttsx3` library correctly using the `pip install pyttsx3` command.
- If the GUI is not displaying properly, make sure your Python installation includes the `tkinter` library (which is usually pre-installed with Python).

## License

This project is licensed under the MIT License.

---

**Developed by Santosh R.**

