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
# SHUTDOWN
def shutdown():
    speak("shutting down")
    sys.exit()



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


def alexa():
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
        
# OK GOT IT
def ok():
    speak("ok got it!")


def dk():
    speak("I don't understand what you said")

q2="hello" #global variable

def Temp():
    search ="today's weather"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_= "BNeawe").text
    print(temperature)
    speak(f"the tamperature is {temperature},Celsius")

#TIME TO SECONDS
def seconds(time):
    multi = 1
    nu = 0
    print(type(time))
    for word in time.split():
        if word.isdigit():
            num = word
            nu = nu + (int(word) * 3600) / multi
            multi = multi * 60
    return int(nu)

def alarm():

    speak("alarm set")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    while True:
        winsound.Beep(frequency, duration)

        if "ok got it" in query:
            break

    speak("ALARM CLOSED!")
    
if __name__ == "__main__":
    
    alexa()

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
                elif ' the time' in query:
                   Time = datetime.datetime.now().strftime("%I:%M %p")
                   print(Time)
                   speak("The time is" + Time)

                 elif 'on youtube' in query:
                       playcom = query.replace("play", "")
                       speak(playcom)
                       print(playcom)
                       pywhatkit.playonyt(playcom)

     #For Jokes
                elif 'joke' in query:
                     speak(pyjokes.get_joke())


    # SEARCH
                elif 'search' in query:
                      find = query.replace("search", "")
                      print(find)
                      pywhatkit.search(str(find))

                elif 'google' in query:
                    find = query.replace("google", "")
                    print(find)
                    pywhatkit.search(str(find))

    # SHUT DOWN
                elif 'shut down' in query  or 'shutdown' in query: 
                    shutdown()
                elif "what is the temperature" in query or "today's weather" in query or "today's temperature" in query:
                    Temp()


            elif "alarm" in query:
                speak("Enter The Time !:")
                try:
                    time = input("Enter the time !(THROUGH KEYBOARD)(hh:mm:ss)(24 HOUR FORMAT)")

                except Exception as e:
                    print("Your Input is in IMPROPER FORMAT")


                time = seconds(time)
                time_ac=datetime.datetime.now().time()
                current_time = time_ac.strftime("%H:%M:%S")
                current_time = seconds(current_time)
                ti = time-current_time
                zehar = threading.Timer(ti , alarm)
                ok()
                zehar.start()




            elif "what is " in query or "who is" in query or  "what's" in query or "tell me" in query:
                try :
                    pywhatkit.info(query.replace("tell me",""), lines = 2)

                except Exception as a:
                    print("Didn't get it")


                speak("here is what i found")

