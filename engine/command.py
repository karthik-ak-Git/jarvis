import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing and analysing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
        eel.DisplayMessage(query)
        time.sleep(1)
    except Exception as e:
        return ""
    return query.lower()


@eel.expose
def allCommands():
    try:
        query = takeCommand()

        if "open" in query:
            from engine.features import opencommand
            opencommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("not opening")

    except:
        print("error")
    eel.ShowHood()
