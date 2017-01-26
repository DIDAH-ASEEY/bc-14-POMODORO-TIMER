import winsound

def end_sound():
    sound = winsound.PlaySound('sound_sonar.wav', winsound.SND_FILENAME)
    return sound

    

