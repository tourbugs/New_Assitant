import sys
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
from playsound import playsound
import webbrowser
import os
import winsound
import pywhatkit
import pyjokes
import threading
import requests
from bs4 import BeautifulSoup #FOR WEB SCRAPING

engine = pyttsx3.init()
voices = engine.getProperty('voices')



# VOICE
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 150)  # 120 is the best
# engine.setProperty('pitch', 180)

# SPEAK
def speak(audio):
    if engine._inLoop:
        engine.endLoop()

    engine.say(audio)
    engine.runAndWait()



# INTRODUCTION PART
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    speak("Hello I am alex  , How may i help you")
