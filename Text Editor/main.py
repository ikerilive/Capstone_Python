from tkinter import *
from tkinter import filedialog

# ---------------------------- FUNCTIONS ------------------------------- #

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            text.delete(1.0, END)
            text.insert(END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text.get(1.0, END))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Text Editor")
window.config(padx=50, pady=50)

text = Text(window, wrap="word", width=80, height=20)
text.pack()

open_button = Button(text="Open", command=open_file)
open_button.pack(side=LEFT, padx=5)

save_button = Button(text="Save", command=save_file)
save_button.pack(side=RIGHT, padx=5)

window.mainloop()
