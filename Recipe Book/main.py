import json
from tkinter import *

# ---------------------------- FUNCTIONS ------------------------------- #

def load_recipes():
    try:
        with open("recipes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_recipes():
    with open("recipes.json", "w") as file:
        json.dump(recipes, file, indent=4)

def add_recipe():
    name = name_entry.get().strip()
    ingredients = ingredients_entry.get().strip()
    instructions = instructions_entry.get().strip()

    if not name or not ingredients or not instructions:
        messagebox.showinfo(title="Oops", message="All fields must be filled!")
        return

    recipes[name] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes()
    refresh_recipes()
    name_entry.delete(0, END)
    ingredients_entry.delete(0, END)
    instructions_entry.delete(0, END)

def show_recipe():
    selected_recipe = recipe_listbox.get(ACTIVE)
    if selected_recipe:
        details = recipes[selected_recipe]
        recipe_label.config(text=f"Ingredients:\n{details['ingredients']}\n\nInstructions:\n{details['instructions']}")

def refresh_recipes():
    recipe_listbox.delete(0, END)
    for recipe in recipes:
        recipe_listbox.insert(END, recipe)

# ---------------------------- UI SETUP ------------------------------- #

recipes = load_recipes()

window = Tk()
window.title("Recipe Book")
window.config(padx=50, pady=50)

name_label = Label(text="Recipe Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(width=30)
name_entry.grid(row=0, column=1)

ingredients_label = Label(text="Ingredients:")
ingredients_label.grid(row=1, column=0)
ingredients_entry = Entry(width=30)
ingredients_entry.grid(row=1, column=1)

instructions_label = Label(text="Instructions:")
instructions_label.grid(row=2, column=0)
instructions_entry = Entry(width=30)
instructions_entry.grid(row=2, column=1)

add_button = Button(text="Add Recipe", command=add_recipe)
add_button.grid(row=3, column=0, columnspan=2)

recipe_listbox = Listbox(height=10, width=50)
recipe_listbox.grid(row=4, column=0, columnspan=2)
recipe_listbox.bind("<<ListboxSelect>>", lambda e: show_recipe())

recipe_label = Label(text="", wraplength=400, justify=LEFT)
recipe_label.grid(row=5, column=0, columnspan=2, pady=10)

refresh_recipes()
window.mainloop()
