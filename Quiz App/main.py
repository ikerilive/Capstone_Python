import random
from tkinter import *

# ---------------------------- QUIZ DATA ------------------------------- #
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "What is 5 + 3?", "options": ["5", "7", "8", "10"], "answer": "8"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"}
]

# ---------------------------- FUNCTIONS ------------------------------- #

def load_question():
    global current_question
    current_question = random.choice(questions)
    question_label.config(text=current_question["question"])
    for i, option in enumerate(current_question["options"]):
        option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

def check_answer(selected_option):
    if selected_option == current_question["answer"]:
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Wrong! The correct answer was {current_question['answer']}.", fg="red")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Quiz App")
window.config(padx=50, pady=50)

question_label = Label(text="", font=("Arial", 14), wraplength=300)
question_label.pack(pady=20)

option_buttons = [Button(window, text="", width=20) for _ in range(4)]
for button in option_buttons:
    button.pack(pady=5)

feedback_label = Label(text="", font=("Arial", 12))
feedback_label.pack(pady=10)

load_question()
window.mainloop()
