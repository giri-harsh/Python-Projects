# 📋 Personal To-Do List Application

<div align="center">

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*Stay organized. Stay productive. All with Python.* 🚀

</div>

---

## 🎯 **About The Project**

A **lightweight, CLI-based personal productivity tool** designed to help you manage your daily tasks efficiently. Built with pure Python and featuring persistent data storage, this application offers a clean, intuitive interface for organizing your to-do items without the complexity of databases or web frameworks.

Perfect for developers who want a simple yet powerful task management solution that works right from the terminal.

### ✨ **Key Highlights**
- 🔄 **Persistent Storage** - Your tasks survive program restarts
- 🏷️ **Smart Categorization** - Organize by Work, Personal, Urgent, etc.
- 📱 **Clean CLI Interface** - Beautiful terminal-based user experience
- 🎯 **Zero Dependencies** - Uses only Python standard library
- 💾 **JSON Data Format** - Human-readable and portable

---

## 🛠️ **Built With**

- **Language**: Python 3.6+
- **Data Storage**: JSON file format
- **Modules**: `json`, `os` (Standard Library)
- **Architecture**: Object-Oriented Programming

---

## 🚀 **Features**

| Feature | Description | Status |
|---------|-------------|--------|
| ➕ **Add Tasks** | Create new tasks with title, description, and category | ✅ Complete |
| 👀 **View Tasks** | Display all tasks with completion status | ✅ Complete |
| ✔️ **Mark Complete** | Mark tasks as done with visual indicators | ✅ Complete |
| 🗑️ **Delete Tasks** | Remove unwanted tasks from your list | ✅ Complete |
| 🏷️ **Categorization** | Organize tasks by custom categories | ✅ Complete |
| 💾 **Data Persistence** | Automatic save/load functionality | ✅ Complete |
| 🎨 **Clean Interface** | User-friendly menu-driven experience | ✅ Complete |

---

## 📁 **Project Structure**

```
todo_app/
│
├── 📄 todo.py           # Main application logic
├── 📊 tasks.json        # Task data storage
├── 📖 README.md         # Project documentation
└── 📸 screenshots/      # Demo images (optional)
```

---

## 🏃‍♂️ **Getting Started**

### **Prerequisites**
- Python 3.6 or higher installed on your system

### **Installation & Usage**

1. **Clone the repository**
   ```bash
   git clone https://github.com/giri-harsh/personal-todo-app.git
   cd personal-todo-app
   ```

2. **Run the application**
   ```bash
   python todo.py
   ```

3. **Start managing your tasks!**
   - The app will automatically create `tasks.json` if it doesn't exist
   - Your previous tasks will be loaded on startup

---

## 💻 **Sample Output**

```
🎯 Personal To-Do List Manager
=============================

📋 Your Tasks:
1. [❌ Pending] Finish Python Project | Work
   Complete the final report and documentation

2. [✔️ Done] Grocery Shopping | Personal
   Buy vegetables, fruits, and dairy products

3. [❌ Pending] Study for Exam | Education
   Review chapters 5-8 for tomorrow's test

Choose an option:
1. Add Task
2. View Tasks  
3. Mark Task as Completed
4. Delete Task
5. Exit
```

---

## 🏗️ **Technical Implementation**

### **Object-Oriented Design**
```python
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
```

### **Data Persistence**
- **Format**: JSON for easy reading and portability
- **Auto-save**: Tasks are automatically saved after each operation
- **Auto-load**: Previous tasks are restored when the program starts

### **User Interface**
- Interactive menu system with numbered options
- Clear visual indicators for task status
- Error handling for invalid inputs

---

## 🔮 **Future Enhancements**

- [ ] 📅 **Due Dates** - Add deadline tracking with reminders
- [ ] 🔍 **Search & Filter** - Find tasks by keyword or category
- [ ] ⚡ **Priority Levels** - High, Medium, Low priority system
- [ ] 📊 **Progress Analytics** - Task completion statistics
- [ ] 🎨 **GUI Version** - Tkinter-based graphical interface
- [ ] 🔄 **Task Sorting** - Sort by date, priority, or alphabetically
- [ ] 📱 **Export Options** - Export to CSV, PDF formats

---

## 🧑‍💻 **About the Developer**

<div align="center">

**Harsh Giri**  
*BTech CSE (Data Science) | AKGEC | Batch 2028*

[![GitHub](https://img.shields.io/badge/GitHub-giri--harsh-black?style=flat&logo=github)](https://github.com/giri-harsh)
[![Skills](https://img.shields.io/badge/Skills-Python%20|%20C%2B%2B%20|%20Data%20Science%20|%20ML-blue)](https://github.com/giri-harsh)

🎸 Guitar Enthusiast | 🏀 Basketball Player | 📷 Photography Lover

</div>

---

## 🤝 **Contributing**

Contributions are what make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 **License**

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 **Acknowledgments**

- Built with ❤️ using Python
- Inspired by the need for simple, effective task management
- Thanks to the Python community for excellent documentation

---

<div align="center">

**⭐ Don't forget to star this repo if you found it helpful! ⭐**

*"Because even coders forget their to-dos sometimes."* 😄

</div>
