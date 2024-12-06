import json
from tkinter import *
from tkinter import messagebox

# ---------------------------- FUNCTIONS ------------------------------- #

# Load contacts from JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not email or not phone:
        messagebox.showinfo(title="Oops", message="All fields must be filled!")
        return

    contacts[name] = {"email": email, "phone": phone}
    save_contacts()
    refresh_contacts()
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)

# Search for a contact
def search_contact():
    name = name_entry.get().strip()
    if not name:
        messagebox.showinfo(title="Oops", message="Please enter a name to search!")
        return

    if name in contacts:
        email = contacts[name]["email"]
        phone = contacts[name]["phone"]
        messagebox.showinfo(title="Contact Found", message=f"Name: {name}\nEmail: {email}\nPhone: {phone}")
    else:
        messagebox.showinfo(title="Not Found", message="Contact not found!")

# Refresh contact list
def refresh_contacts():
    contact_listbox.delete(0, END)
    for name, details in contacts.items():
        contact_listbox.insert(END, f"{name} - {details['email']} - {details['phone']}")

# ---------------------------- UI SETUP ------------------------------- #

# Load existing contacts
contacts = load_contacts()

# Initialize main window
window = Tk()
window.title("Contact Book")
window.config(padx=50, pady=50)

# Labels
name_label = Label(text="Name:")
name_label.grid(row=0, column=0)
email_label = Label(text="Email:")
email_label.grid(row=1, column=0)
phone_label = Label(text="Phone:")
phone_label.grid(row=2, column=0)

# Entries
name_entry = Entry(width=30)
name_entry.grid(row=0, column=1)
email_entry = Entry(width=30)
email_entry.grid(row=1, column=1)
phone_entry = Entry(width=30)
phone_entry.grid(row=2, column=1)

# Buttons
add_button = Button(text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0)
search_button = Button(text="Search", command=search_contact)
search_button.grid(row=3, column=1)

# Contact Listbox
contact_listbox = Listbox(height=10, width=50)
contact_listbox.grid(row=4, column=0, columnspan=2, pady=10)

# Initial Load
refresh_contacts()

# Run the application
window.mainloop()
