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


def alex():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    wishme()


def takecommand():
   
    r = sr.Recognizer()


    try:
        with sr.Microphone() as source:
            print("Listening ...")
            r.pause_threshold = 1  # 1 sec break will not complete the sentence
            r.energy_threshold = 800  # energy threshold for backround noise
            audio = r.listen(source)

            try:
                print("Recognizing ...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said : {query}\n")

            except Exception as e:
                # print("e")
                print("Say that again please")
                return "None"
            return query
    except Exception as e:
        print("Didn't found Micro Phone")
        
    
if __name__ == "__main__":
    
    alex()

    while True:
                query = takecommand().lower()

                if 'wikipedia' in query :
                    speak('Searching Wikipedia ... ')
                    query = query.replace("who is", "").replace("what is","").replace("tell me","")
                    try:
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
        
                    except Exception as e:
                        speak("No result found!")
                        print("No result Found!")
                    print(results)
                    speak(results)

                elif 'alex' in query:
                    sys.exit()

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")
