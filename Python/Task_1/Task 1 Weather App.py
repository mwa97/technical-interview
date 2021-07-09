# Tkinter is a Python binding to the Tk GUI toolkit to displlay the Weather App canvas/UI
import tkinter as tk
import requests
import time


def getWeather(app):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    # passing api
    json_d = requests.get(api).json()

    # extracting data in json form from api
    condition = json_d['weather'][0]['main']
    temp = int(json_d['main']['temp'] - 273.15)
    min_temp = int(json_d['main']['temp_min'] - 273.15)
    max_temp = int(json_d['main']['temp_max'] - 273.15)
    pressure = json_d['main']['pressure']
    humidity = json_d['main']['humidity']
    wind = json_d['wind']['speed']

    # Connecting strings to our GUI and setting up how we want them displayed
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Minimum Temp: " + str(min_temp) + "°C" + "\n" + "Maximum Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind)
    # attach final info and data to labels
    l1.config(text=final_info)
    l2.config(text=final_data)


# This makes the inittal TK funticon and we set the main title of the app and its size
# Initialisez a blank window
app = tk.Tk()

# establishes size of window we want
app.geometry("700x450")
# establishes title of the app/app window
app.title("Weather App")

# choosing how we want our letters to look
f = ("words", 14, "bold")
t = ("words", 30, "bold")

# This text box allows the user to input a city which then connects you to search the city which displays the results
textField = tk.Entry(app, justify='center', width=25, font=t)
# Padding between the top of window and the text box
textField.pack(pady=25)

# User friendly practice allows user to enter city without using any other components
textField.focus()
#
textField.bind('<Return>', getWeather)
# these labels show the data that is pulled from API
l1 = tk.Label(app, font=t)
l1.pack()
l2 = tk.Label(app, font=f)

# adds and places element on app window
l2.pack()

# Main lopp holds the view in place, open/close. Gui grounding.
app.mainloop()
