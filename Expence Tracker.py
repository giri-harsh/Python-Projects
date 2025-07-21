import json
from datetime import datetime
import os
import matplotlib.pyplot as plt

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Transport): ").strip()
        date_str = input("Enter date (YYYY-MM-DD) [leave blank for today]: ").strip()
        date = date_str if date_str else datetime.now().strftime("%Y-%m-%d")
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added successfully.")
    except ValueError:
        print("❌ Invalid amount. Please try again.")

def view_summary(expenses):
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    category_summary = {}
    total = 0
    for exp in expenses:
        category = exp["category"]
        amount = exp["amount"]
        total += amount
        category_summary[category] = category_summary.get(category, 0) + amount

    print("\n📊 Expense Summary:")
    for cat, amt in category_summary.items():
        print(f"  {cat}: ₹{amt:.2f}")
    print(f"  Total: ₹{total:.2f}")

    
    try:
        plt.figure(figsize=(6, 4))
        plt.bar(category_summary.keys(), category_summary.values(), color='skyblue')
        plt.title("Expense Summary by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("⚠️ Couldn't show chart:", e)

def view_expenses_over_time(expenses):
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    time_summary = {}
    for exp in expenses:
        date = exp["date"]
        time_summary[date] = time_summary.get(date, 0) + exp["amount"]

    print("\n📅 Spending Over Time:")
    for date, amt in sorted(time_summary.items()):
        print(f"  {date}: ₹{amt:.2f}")

def delete_expense(expenses):
    view_all_expenses(expenses)
    idx = int(input("Enter the expense number to delete: ")) - 1
    if 0 <= idx < len(expenses):
        removed = expenses.pop(idx)
        save_expenses(expenses)
        print(f"✅ Deleted: ₹{removed['amount']} on {removed['date']} ({removed['category']})")
    else:
        print("❌ Invalid index.")

def view_all_expenses(expenses):
    print("\n📄 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['date']}")

def main_menu():
    expenses = load_expenses()
    while True:
        print("\n========= Personal Expense Tracker =========")
        print("1. Add Expense")
        print("2. View Summary by Category")
        print("3. View Spending Over Time")
        print("4. View All Expenses")
        print("5. Delete an Expense")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            view_expenses_over_time(expenses)
        elif choice == '4':
            view_all_expenses(expenses)
        elif choice == '5':
            delete_expense(expenses)
        elif choice == '6':
            print("👋 Exiting. Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

    
if __name__ == "__main__":
    main_menu()
