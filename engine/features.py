import os
import re
from playsound import playsound
import eel
import pywhatkit as kit
from engine.command import speak
from engine.config import ASSISTANT_NAME
# playing assistant sound


@eel.expose
def playAssisteantSound():
    music_dir = "www\\assets\\audio\\start_sound (1).mp3"
    playsound(music_dir)


def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != '':
        speak("opening" + query)
        os.system(f"start {query}")
    else:
        speak("not found")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak('playing' + search_term + "on youtube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None
