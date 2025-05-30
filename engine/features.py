from playsound import playsound
import eel
# playing assistant sound


@eel.expose
def playAssisteantSound():
    music_dir = "www\\assets\\audio\\start_sound (1).mp3"
    playsound(music_dir)
