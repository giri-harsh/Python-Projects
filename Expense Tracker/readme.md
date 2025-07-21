# 🧾 Personal Expense Tracker using Python (CLI-Based)

## 📌 Introduction

The **Personal Expense Tracker** is a command-line based Python application that enables users to monitor and manage their daily financial transactions efficiently. It simplifies expense logging, provides insightful summaries, and stores data for long-term analysis. The project blends Python programming with real-world financial tracking, making it ideal for academic and personal use.

---

## 🎯 Objective

The goal is to build a **functional and persistent** expense tracking tool using Python. Key features include:

- Adding expenses with category and date
- Viewing summaries by category or date
- Storing/retrieving records via JSON files
- Optional bar chart visualization
- Managing and deleting entries

This helps users improve budgeting habits, analyze spending, and apply Python concepts such as:

- Data structures
- File handling
- Functions
- Optional data visualization

---

## 🛠️ Tools and Technologies Used

| Technology       | Purpose                                               |
| ---------------- | ----------------------------------------------------- |
| Python           | Core programming language                             |
| `json` module    | File handling and data storage in JSON format         |
| `datetime`       | Handling and formatting date entries                  |
| `os` module      | File existence and path checks                        |
| `matplotlib`     | *(Optional)* Visualize spending patterns via charts   |
| VS Code / Thonny | Code editor                                           |
| CLI (Terminal)   | Running and interacting with the script               |

---

## 📂 Project Structure
├── expense_tracker.py # Main Python script
├── expenses.json # Stores expense data
├── README.md # Project documentation
├── screenshots/ # Example outputs (optional)


---

## ⚙️ Functional Modules

### 1. Add Expense

- Enter amount, category (Food, Transport, etc.), and date (optional).
- Validates and stores data in a JSON file.

### 2. View Summary

- Displays total per category and overall spending.
- *(Optional)*: Visualize using a bar chart.

### 3. View Spending Over Time

- Groups expenses by date.
- Shows total spent per day.

### 4. View All Expenses

- Lists all entries with amount, category, and date.

### 5. Delete an Expense

- Select and delete any record by serial number.

---

## 🧠 Python Concepts Used

- **Lists & Dictionaries** for storing entries
- **Functions** for modular code design
- **File I/O** with JSON for persistence
- **Date Handling** using `datetime`
- **Error Handling** for smooth user input
- **Matplotlib** *(optional)* for data visualization

---

## 📊 Sample JSON Data

```json
[
  {
    "amount": 120.5,
    "category": "Food",
    "date": "2025-07-21"
  },
  {
    "amount": 75,
    "category": "Transport",
    "date": "2025-07-22"
  }
]

🔍 Use Case Scenario
A college student like Harsh records daily spending on food, stationery, travel, etc. At the end of the week/month, they run the script to view summaries and optionally visualize category-wise spending using bar charts.

🚀 Future Enhancements
 Edit Expense Records

 Set Monthly Budget Limits

 Add GUI (Tkinter/Streamlit)

 Sync with Firebase/Google Sheets

 User Login/Password Protection

 Export Reports as CSV/PDF

👨‍💻 Developer
Harsh Giri
B.Tech CSE (Data Science)
Ajay Kumar Garg Engineering College (AKGEC)

Passionate about Python, real-world problem solving, and personal development through coding, music, and basketball.



