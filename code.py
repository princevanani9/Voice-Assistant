import pyttsx3  # convert text format into speech format.
import datetime
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice


# this function takes audio as an input, and pronounces it, as an output.
def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak('Hello Sir, I am Ironman, your assistant. Please tell me how may I help you')




if __name__ == "__main__":
    wishme()
