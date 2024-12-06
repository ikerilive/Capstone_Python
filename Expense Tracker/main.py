import json
from tkinter import *
from tkinter import messagebox


# ---------------------------- FUNCTIONS ------------------------------- #

# Load expenses from JSON file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save expenses to JSON file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense():
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()

    if not category or not amount:
        messagebox.showinfo(title="Oops", message="Category and amount cannot be empty!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showinfo(title="Error", message="Amount must be a number!")
        return

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    save_expenses()
    refresh_expenses()
    category_entry.delete(0, END)
    amount_entry.delete(0, END)


# Refresh expense list
def refresh_expenses():
    expense_listbox.delete(0, END)
    total_expenses = 0
    for category, amount in expenses.items():
        total_expenses += amount
        expense_listbox.insert(END, f"{category}: ${amount:.2f}")
    total_label.config(text=f"Total Expenses: ${total_expenses:.2f}")


# ---------------------------- UI SETUP ------------------------------- #

# Load existing expenses
expenses = load_expenses()

# Initialize main window
window = Tk()
window.title("Expense Tracker")
window.config(padx=50, pady=50)

# Labels
category_label = Label(text="Category:")
category_label.grid(row=0, column=0)
amount_label = Label(text="Amount:")
amount_label.grid(row=1, column=0)

# Entries
category_entry = Entry(width=30)
category_entry.grid(row=0, column=1, columnspan=2)
amount_entry = Entry(width=30)
amount_entry.grid(row=1, column=1, columnspan=2)

# Buttons
add_button = Button(text="Add Expense", command=add_expense)
add_button.grid(row=2, column=0, columnspan=3)

# Expense Listbox
expense_listbox = Listbox(height=10, width=50)
expense_listbox.grid(row=3, column=0, columnspan=3, pady=10)

# Total Label
total_label = Label(text="Total Expenses: $0.00")
total_label.grid(row=4, column=0, columnspan=3)

# Initial Load
refresh_expenses()

# Run the application
window.mainloop()
