import requests
import os
import tkinter as tk
import time
from pythoncustomsgbox import CustomMessageBox
from datetime import datetime
# from ollama import chat
# from ollama import ChatResponse

# Loop for the program.
while True:
    root = tk.Tk()
    root.withdraw()
    # Get user's input.
    location = CustomMessageBox.customTextBoxMsg("Location Information:", "Type exit or enter a city or talk to ai? just type ai:", "black", "white", "black", "white")
    if location is None:
        question0 = CustomMessageBox.customYesNoMsg("Question:", "Are you sure?", "black", "white", "black", "lightblue")
        if question0 is True:
            break
        else:
            continue
    elif location.lower() == "exit":
        exit_confirm = CustomMessageBox.customTextBoxMsg("Information", "Exiting confirmation after you type \"exit\"", "black", "white", "black", "white")
        if str(exit_confirm).lower() == "exit":
            break
        else:
            continue  
            
    # Ask Ai about anything mode. (Only uncomment when you want to ask ai.)
    # elif location.lower() == "ai":
    #     question = CustomMessageBox.customTextBoxMsg("Question:", "What do you like to ask ai?", "black", "white", "black", "white")
    #     if question is None:
    #         question1 = CustomMessageBox.customYesNoMsg("Question:", "Are you sure?", "black", "white", "black", "lightblue")
    #         if question1 is True:
    #             break
    #         else:
    #             continue
    #     answer: ChatResponse = chat(model= "llama3", messages= [
    #         {
    #             'role': 'user',
    #             'content': question,
    #         },
    #     ])
    #     CustomMessageBox.customMsgBoxWithScrBar("Ai's Response:", "Ai's Response:", answer.message.content, "black", "white", "black", "white", "black", False)
    #     continue
    location = str(location).strip("\n")

    measurement = CustomMessageBox.customTextBoxMsg("Measurement:", "Enter a measurement unit (metric/imperial):", "black", "white", "black", "white")
    if measurement is None:
        question2 = CustomMessageBox.customYesNoMsg("Question:", "Are you sure?", "black", "white", "black", "lightblue")
        if question2 is True:
            break
        else:
            continue
    unit = CustomMessageBox.customTextBoxMsg("Unit:", "Enter a unit (celsius/fahrenheit):", "black", "white", "black", "white")
    if unit is None:
        question3 = CustomMessageBox.customYesNoMsg("Question:", "Are you sure?", "black", "white", "black", "lightblue")
        if question3 is True:
            break
        else:
            continue

    # Get weather data from Openweathermap api.
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=YOURAPIKEY&units={measurement}")
        data = response.json()
    except (requests.exceptions.ConnectionError, ConnectionError):
        CustomMessageBox.customMsgBox("Error!", "Your Wi-Fi is currently not working. \n Please try again later. \n Exiting after you click OK...", "black", "red", "white", "red", True)
        break

    if response.status_code == 404:
        CustomMessageBox.customMsgBox("Error!", "City not found!", "black", "red", "white", "red", True)
        continue
    elif response.status_code == 502:
        CustomMessageBox.customMsgBox("Error!", "Bad Gateway \n Try again later.", "black", "red", "white", "red", True)
        continue
    elif response.status_code != 200:
        CustomMessageBox.customMsgBox("Error!", "Try again later, or you didn't enter anything in the text boxes.", "black", "red", "white", "red", True)
        continue
    elif response.status_code == 429:
        CustomMessageBox.customMsgBox("Error!", "Too many requests. \n Try again tommorow.", "black", "red", "white", "red", True)
        continue

    # Exception clause to handle user's input for the city name not found.
    try:
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        place = data['name']
        country = data['sys']['country']
        weather = data['weather'][0]['description']
        humid = data['main']['humidity']
        wind = data['wind']['speed']
        convertwind = int(wind)
        temp = data['main']['temp']
        temperaturefeelslike = data['main']['feels_like']
        converttemp = int(temperaturefeelslike)

        valid_combo = (unit == "celsius" and measurement == "metric") or (unit == "fahrenheit" and measurement == "imperial")
        if not valid_combo:
            CustomMessageBox.customMsgBox("Error!", "Unit and measurement do not match!\nUse celsius with metric and fahrenheit with imperial.", "black", "red", "white", "red", True)
            continue

        # Show the current weather information from Openweathermap api.
        current_datetime = datetime.now()
        CustomMessageBox.customMsgBox("Weather information:", 
            f"Time checked for weather information (your current time): {current_datetime.replace(microsecond= 0)} \n"
            f"Location: {place} \n"
            f"The location of your city is {place}, and the country is {country}.\n"
            f"The longitude of your city is {longitude}. \n"
            f"The latitude of your city is {latitude}. \n"
            f"The weather of your city is {weather}. \n"
            f"Your wind in your city is {convertwind} m/s. \n"
            f"The humidity of your city is {humid}%.\n"
            f"Your temperature is {temp}°{'C' if unit == 'celsius' else 'F'}.\n"
            f"Your temperature (feels like) is {converttemp}°{'C' if unit == 'celsius' else 'F'}.\n \n"
            "It is also saved as weatherlog.txt at the directory this Python file is in", "black", "white", "black", "white", False
        )

        # Creates a weatherlog.txt file after showing the current weather information.
        with open('weatherlog.txt', 'a', encoding= "utf-8") as weather_log:
            weather_log.writelines(["Weather information: \n"
            f"Time checked for weather information (your current time): {current_datetime.replace(microsecond= 0)} \n"
            f"Location: {place} \n"
            f"The location of your city is {place}, and the country is {country}.\n"
            f"The longitude of your city is {longitude}. \n"
            f"The latitude of your city is {latitude}. \n"
            f"The weather of your city is {weather}. \n"
            f"Your wind in your city is {convertwind} m/s. \n"
            f"The humidity of your city is {humid}%.\n"
            f"Your temperature is {temp}°{'C' if unit == 'celsius' else 'F'}.\n"
            f"Your temperature (feels like) is {converttemp}°{'C' if unit == 'celsius' else 'F'}. \n \n"])

        # Asks you if you want to delete the log file.
        time.sleep(0.5)
        question4 = CustomMessageBox.customYesNoMsg("Question:", "Do you want to delete the log file?", "black", "white", "black", "lightblue")
        if question4 is True:
            try:
                os.remove("weatherlog.txt")
                CustomMessageBox.customMsgBox("Information:", "Your weatherlog.txt file is successfully deleted.", "black", "white", "black", "green", False)
                continue
            except (FileNotFoundError, PermissionError):
                CustomMessageBox.customMsgBox("Error!", "The weather log file couldn't be deleted. \n Please check if your weatherlog.txt file is in the same directory and try again later.", "black", "red", "white", "red", True)
                continue
        else:
            continue

    except (KeyError, NameError):
        CustomMessageBox.customMsgBox("Error!", "City not found and information cannot be displayed! \n Or you didn't uncomment lines 23-38 for Ollama AI. \n If you don't have Ollama AI please look at how to install it in the github repository. \n If not, please don't use AI.", "black", "red", "white", "red", True)
        continue
    except ValueError:
        CustomMessageBox.customMsgBox("Error!", "Inputs you entered previously must be a string. \n Or did you use a wrong type of Ollama AI?", "black", "red", "white", "red", True)
        continue
    except ModuleNotFoundError:
        CustomMessageBox.customMsgBox("Error!", "Didn't you run pip install ollama?", "black", "red", "white", "red", True)
        continue
