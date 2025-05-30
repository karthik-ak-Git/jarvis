import os
import re
import sqlite3
import webbrowser
from playsound import playsound
import eel
import pywhatkit as kit
from engine.command import speak
from engine.config import ASSISTANT_NAME
# playing assistant sound

# connection
con = sqlite3.connect('alexa.db')
cursor = con.cursor()


@eel.expose
def playAssisteantSound():
    music_dir = "www\\assets\\audio\\start_sound (1).mp3"
    playsound(music_dir)


def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute(
                'SELECT path FROM system_commands WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute(
                    'SELECT url FROM website_commands WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)
                    except:
                        speak("not found")

        except:
            speak("some thing went wrong")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak('playing ' + search_term + " on youtube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None
