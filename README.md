
# ✅ To-Do CLI (Python)

## 👨‍💻 Author  
**Austin Carlson** (#growthwithcoding)

---

## 📖 Project Overview
This project is a **Command-Line To-Do List Application** built in Python. It was created to practice fundamental Python concepts such as lists, functions, control structures, file I/O, and error handling.

The application allows users to manage tasks interactively from the terminal. Tasks are stored in memory using a **Python list** and also saved to a plain text file (`tasks.txt`) so progress is retained between sessions. The CLI features **colorized output** for readability using the `colorama` library.

---

## 🎯 Assignment Objectives

- **🖥️ User Interface (UI) & Storage**
  - Build a simple CLI that welcomes users and displays a menu with options.
  - Store tasks in a **Python list** during runtime.
  - Persist tasks in a **text file (`tasks.txt`)** so they are saved after exiting.

- **⚡ Core Features**
  - ➕ Add tasks  
  - 👀 View tasks  
  - 🗑️ Delete tasks  
  - ❌ Quit the application  

- **🎮 User Interaction**
  - Use `input()` to capture user selections.
  - Validate user input to prevent errors.
  - Provide clear messages for invalid choices, empty lists, or invalid task deletions.

- **🛡️ Error Handling**
  - Use `try`, `except`, `else`, and `finally` for robust error handling.
  - Handle invalid input and missing tasks gracefully.

- **📂 Code Organization**
  - Use functions with descriptive names.
  - Include comments and docstrings for clarity.

- **🔍 Testing & Debugging**
  - Test with edge cases (empty lists, invalid input, invalid deletions).
  - Ensure the app works as expected in a command-line environment.

---

## ✨ Features

- 🎉 Welcome banner with **colorful CLI interface**
- 📝 **Add tasks** with an **importance level** (High, Medium, Low)
- 📋 **View tasks** sorted **High → Medium → Low**, with colored labels (**🔴 High**, **🟡 Medium**, **🟢 Low**)
- 🗑️ **Delete tasks** by displayed number (matches the sorted view), with validation
- ↩️ Cancel options and **retries** on invalid input
- 💾 **Persistent storage** in `tasks.txt`
- 🚀 On startup, the app **automatically shows your tasks** (with a friendly empty-state message if none exist)

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd python_todo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the app:
```bash
python todo_app.py
```

---

## 💾 Data Storage

- Tasks are stored in memory as a **list** while the app runs.
- Tasks are saved to **`tasks.txt`** in the format:
  ```
  IMPORTANCE|Task description
  ```
- Example:
  ```
  HIGH|Finish project report
  MEDIUM|Practice Python exercises
  LOW|Water the plants
  ```

---

## 🛠️ Tech Stack

- 🐍 **Python 3.9+**
- 🎨 **colorama** (for terminal colors)

---

## 🎥 Demo & Submission

To complete the assignment, I will:
- 🎬 Record a **5–10 minute demo** of the application showing all functionality, **or**
- 🗣️ Present it in a **live Q&A session** / **1-on-1 with an SSM**
- 🔗 Submit the GitHub repository link on **Google Classroom**

---

## 📚 Works Cited

- [📖 Python Official Documentation — Built-in Types (lists)](https://docs.python.org/3/library/stdtypes.html#list)  
- [🐍 Python Official Documentation — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)  
- [📝 Python Official Documentation — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)  
- [🎨 Colorama Documentation](https://pypi.org/project/colorama/)  
- [📰 Real Python: Python Exceptions — An Introduction](https://realpython.com/python-exceptions/)  
- [🌐 W3Schools Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)

---

✅ **Project by Austin Carlson (#growthwithcoding)**
