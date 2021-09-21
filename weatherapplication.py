import tkinter as tk
import requests
import time


def getWeather(box):
    city = textField.get()
    # API KEY
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    # created a variable to store data

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + \
        "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind)
    label1.config(text=final_info)
    label2.config(text=final_data)


# -------------------GUI CODE-------------------->
# ------------------------box------------------->
box = tk.Tk()
box.geometry("400x400")
box.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")


title = tk.Label(text="Enter the location")
title.pack()
textField = tk.Entry(box, justify='center', width=20, font=30)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(box, font=t)
label1.pack()
label2 = tk.Label(box, font=f)
label2.pack()


box.mainloop()
