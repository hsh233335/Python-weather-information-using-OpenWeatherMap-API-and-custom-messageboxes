# Python-weather-information-using-OpenWeatherMap-API-and-custom-messageboxes

# Description
Shows the current weather information using OpenWeatherMap API and tkinter messagebox.

# What it does:
- Sends you a custom-made messageboxes about the current weather.
- Shows an error when something goes wrong.
- Has 2 temperature types to choose from: **Celsius and Fahrenheit**.
- Has a custom-made (Made by me) messageboxes using `customtkinter`.
- The custom-made (Made by me) messageboxes includes the Fredoka One font.
- Warning: ***Celsius goes with metric input and Fahrenheit goes with imperial input***.
- ***Optional: Has an AI to chat. (using Ollama and requires windows 10 or later)***

# Requirements
Python 3 and above.

# How do I run this code?
## Step 1:
Download the Python files, and the Fredoka One font file. <br> ***IMPORTANT! (Please put the Fredoka One font file in the same directory as your Python file.)*** <br>
***The one to run is the weather.py file and NOT the pythoncustomsgbox.py.*** <br> <br>
Using:
```
git clone https://github.com/hsh233335/Python-weather-information-using-OpenWeatherMap-API
```
or **if you don't have git, press the green code button and the top and click "Download ZIP".
After that, extract the file and follow the steps below. (I would recommend moving the downloaded and extracted file to Desktop, get the python file out of the extracted folder.)**
## Step 2 (Optional (to use Ollama AI mentioned above):
Go to https://ollama.com/download
## Step 3 (Optional (to use Ollama AI mentioned above):
Download the installation file depending on your operating system, and follow instructions on-screen.
## Step 4 (Optional (to use Ollama AI mentioned above):
Run this in your terminal:
```
pip install ollama
```
and this:
```
ollama pull llama3
```
After that uncomment line 23-38.
## Step 5 (Required from now on):
Go to https://home.openweathermap.org/users/sign_up, and **create an account**. **If you already have an account**, go to https://home.openweathermap.org/api_keys, and copy the API Key.
## Step 6:
Replace the API Key at the **YOUR API KEY** text in code line 56.
## Step 7 IMPORTANT!:
Run 
```
pip install requests
```
## Step 8 IMPORTANT!:
Run 
```
pip install customtkinter
```
## Step 9:
Run 
```
python weather.py
```
or without terminal view run:
```
pythonw weather.py
```
## Step 10:
Enjoy!

# Example Usage (Exit):
The first page: <br> <br>
![Screenshot 2025-07-02 161650](https://github.com/user-attachments/assets/a38eece4-43ac-4587-9ebc-75008a8bf2eb) <br> <br>
Type exit into the prompt: <br> <br>
![Screenshot 2025-07-02 161844](https://github.com/user-attachments/assets/2ac083a7-3c94-439e-8341-303f7e8c22fd) <br> <br>
After you click ok, you will be greeted this page. <br> <br>
![Screenshot 2025-07-02 161952](https://github.com/user-attachments/assets/66386884-586e-489a-ad18-03df281ee095) <br> <br>
***If you click ok, the program will close, if cancel, the program will return you to the previous page.***

# Example Usage (Weather):
The first page (with city name): <br> <br>
![Screenshot 2025-07-02 163940](https://github.com/user-attachments/assets/a039a623-d405-411d-882c-eeecd233177f) <br> <br>
Click OK and you will be prompted these 2 more screens you have to enter. <br> <br>
![image](https://github.com/user-attachments/assets/8fc99bc8-0a1b-41ed-b304-61e3a5e16138) <br> <br>
![Screenshot 2025-07-02 164021](https://github.com/user-attachments/assets/723741dd-c61e-4235-9e0e-758bac4d9d6c) <br> <br>
The result (In celsius): <br> <br>
![Screenshot 2025-07-02 162620](https://github.com/user-attachments/assets/898da752-7689-47e6-84bd-2ad23f5b6e77) <br> <br>
The results above are also saved in a log (notepad txt file) named as weatherlog.txt <br> <br>
![Screenshot 2025-07-02 162736](https://github.com/user-attachments/assets/62fccbf1-ac0e-42f6-9ad3-04c949c844b5) <br> <br>
You will then be asked by another screen, to ask if you want to delete the log file. <br> <br>
![Screenshot 2025-07-02 162836](https://github.com/user-attachments/assets/5fac326d-57f1-4a1b-9aaf-09760537e1be) <br> <br>
If you do click yes, this will happen, or if no, it will return you to the first page. <br> <br>
![Screenshot 2025-07-02 162913](https://github.com/user-attachments/assets/2c5a1cc2-6e5e-4f0b-a57c-6764c799778f)
If you click OK, it will return you to the first page.

# Example Usage (AI Optional: must have Ollama installed):
The first page, type ai. <br> <br>
![Screenshot 2025-07-02 163125](https://github.com/user-attachments/assets/71481471-29cb-43c8-a90d-93c5c8092632) <br> <br>
The next page will ask you what do  you like to ask AI? In my case I asked it, **what foods are good for a diet?** <br> <br>
![Screenshot 2025-07-02 163308](https://github.com/user-attachments/assets/6946e1c6-6c26-4558-afcd-51c8d1189259) <br> <br>
AI then responds with this format (might take a few seconds): <br> <br>
![Screenshot 2025-07-02 163416](https://github.com/user-attachments/assets/db7d3572-6a90-4db3-9a12-384c4de58604) <br> <br>
You can scroll to access overflowed sections of the text. <br>
If you click OK, you will return to the first page.

# Example Usage (Using the red exit cross button):
The first page (with mouse hovering over red cross): <br> <br>
![Screenshot 2025-07-02 163624](https://github.com/user-attachments/assets/a596c22c-4935-4134-979d-ff449f2745c6) <br> <br>
If you click the red cross button, or the cancel button, you will be asked this screen. <br> <br>
![Screenshot 2025-07-02 163826](https://github.com/user-attachments/assets/5053a5b1-69e9-4035-b103-155e5c44693c) <br> <br>
If you click Yes, the program will close, or if No, it will return you to the first page.

***Note: All of the pictures above are in Windows 10.***
