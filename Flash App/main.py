import random
from tkinter import *

# ---------------------------- FLASHCARD DATA ------------------------------- #

flashcards = {
    "Python": "A high-level programming language.",
    "HTML": "A markup language for creating web pages.",
    "CSS": "A language for styling web pages.",
    "JavaScript": "A programming language for the web.",
    "SQL": "A language for managing databases."
}

# ---------------------------- FUNCTIONS ------------------------------- #

def show_next_card():
    global current_term
    current_term = random.choice(list(flashcards.keys()))
    term_label.config(text=current_term)
    definition_label.config(text="")

def show_definition():
    definition = flashcards[current_term]
    definition_label.config(text=definition)

# ---------------------------- UI SETUP ------------------------------- #

# Initialize main window
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50)

# Flashcard Labels
term_label = Label(text="", font=("Arial", 24, "bold"))
term_label.pack(pady=20)
definition_label = Label(text="", font=("Arial", 18))
definition_label.pack(pady=20)

# Buttons
next_button = Button(text="Next Card", command=show_next_card)
next_button.pack(pady=10)
show_button = Button(text="Show Definition", command=show_definition)
show_button.pack(pady=10)

# Start with the first card
show_next_card()

# Run the application
window.mainloop()
