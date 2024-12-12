import calendar
from tkinter import *

# ---------------------------- FUNCTIONS ------------------------------- #

def display_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())

    if not (1 <= month <= 12):
        result_label.config(text="Please enter a valid month (1-12)")
        return

    cal = calendar.monthcalendar(year, month)
    for i, week in enumerate(cal):
        for j, day in enumerate(week):
            day_label = day_labels[i][j]
            day_label.config(text=day if day != 0 else "")

    month_name = calendar.month_name[month]
    result_label.config(text=f"{month_name} {year}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Simple Calendar")
window.config(padx=20, pady=20)

# Input Fields
Label(text="Year:").grid(row=0, column=0)
year_entry = Entry(width=10)
year_entry.grid(row=0, column=1)

Label(text="Month:").grid(row=1, column=0)
month_entry = Entry(width=10)
month_entry.grid(row=1, column=1)

Button(text="Show Calendar", command=display_calendar).grid(row=2, column=0, columnspan=2, pady=10)

# Weekday Labels
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, day in enumerate(weekdays):
    Label(text=day, font=("Arial", 12, "bold")).grid(row=3, column=i)

# Day Labels
day_labels = [[Label(width=5, height=2, relief="solid", font=("Arial", 10)) for _ in range(7)] for _ in range(6)]
for i, week in enumerate(day_labels):
    for j, label in enumerate(week):
        label.grid(row=i + 4, column=j)

# Result Label
result_label = Label(text="", font=("Arial", 14, "bold"))
result_label.grid(row=10, column=0, columnspan=7, pady=10)


window.mainloop()
