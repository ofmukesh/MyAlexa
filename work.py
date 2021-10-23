import datetime
import wikipedia
import webbrowser
import os
import pyjokes
from data import *
from services import *


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak(name)


if __name__ == "__main__":
    wishMe()
    speak("How are you")
    query = takeCommand().lower()
    if "fine" in query:
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("Youtube ok")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("Google ok")
                webbrowser.open("google.com")

            elif 'goodbye alexa' in query:
                speak(f"goodbye {name}")
                break

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                os.system('cmd /k "code"')

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'father'&'my' in query:
                speak(f"{f_name}")

            elif 'mother'&'my' in query:
                speak(f"{m_name}")  

            elif 'my age' in query:
                speak(f"my dear your age is {age}")

            elif 'what'&'learn' in query:
                speak(f"you are learning {learn}")
    else:
        speak(f"Bye bye {name}")
        print("bye")