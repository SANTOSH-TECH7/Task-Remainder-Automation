
# Friday Task Reminder

This project is a Python-based Task Reminder application with a graphical user interface (GUI) built using `tkinter`. 
The application allows users to add, view, and listen to their daily tasks. It also provides voice announcements of tasks when the application starts.

## Features

- **Task Management**: Add and view tasks easily within the GUI.
- **Voice Announcement**: Tasks are read aloud automatically when the application starts, using the `pyttsx3` library.
- **Persistent Storage**: Tasks are saved to a file (`tasks.txt`) for persistence.
- **User-Friendly Interface**: A modern, dark-themed GUI for a comfortable user experience.

## Requirements

- Python 3.x
- Libraries: `tkinter`, `pyttsx3`, `os`, `threading`

## File Structure

```
|-- tasks.txt               # File to store tasks persistently
|-- task_reminder.py        # Main Python script for the application
```

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python libraries if not already installed:
    ```bash
    pip install pyttsx3
    ```
3. Run the application using the following command:
    ```bash
    python task_reminder.py
    ```

## How to Use

1. Launch the application.
2. Add tasks using the input field and click the **Add Task** button.
3. Tasks will be displayed in the text box and saved to `tasks.txt`.
4. On every launch, the application will announce the tasks aloud.

## Screenshot

## Friday Task Reminder UI Preview

![Friday Task Reminder](images/Screenshot_2024-12-16.png)


## License

This project is licensed under the MIT License.

---
Developed by [Your Name].
