import requests
from tkinter import *
from tkinter import messagebox

# ---------------------------- FUNCTIONS ------------------------------- #

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showinfo(title="Oops", message="Please enter a city name!")
        return

    API_KEY = "98604ad7e2437b5a677b0a3b46e182d1"  
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        response.raise_for_status()
        weather_data = response.json()
        temp = weather_data["main"]["temp"]
        weather = weather_data["weather"][0]["description"]
        messagebox.showinfo(title=city, message=f"Temperature: {temp}°C\nCondition: {weather.capitalize()}")
    except Exception as e:
        messagebox.showinfo(title="Error", message="City not found or API issue!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Weather App")
window.config(padx=50, pady=50)

# Labels
city_label = Label(text="City:")
city_label.grid(row=0, column=0)

# Entries
city_entry = Entry(width=30)
city_entry.grid(row=0, column=1)

# Buttons
search_button = Button(text="Get Weather", command=get_weather)
search_button.grid(row=1, column=0, columnspan=2)

# Run the application
window.mainloop()
