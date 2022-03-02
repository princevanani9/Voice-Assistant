import pyttsx3  # convert text format into speech format.
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import pywhatkit
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


def takeCommand():
    #It takes microphone input from the user and returns string output    
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.    
     except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
     return query
def Play_Video_In_Youtube():
    instruct = takeCommand()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
        print(song)
def Send_Message():
    instruct = takeCommand()
    if 'message' in instruct:
        number = instruct.replace('play', '')
        speak('Message to' + number)
        pywhatkit.sendwhatmsg(number,"demo",22, 28)
        print(number)
if __name__ == "__main__":
    wishme()
    Play_Video_In_Youtube()
    # Send_Message()
    while True:
        query = takeCommand().lower() #Converting user query into lower case    
        # Logic for executing tasks based on query
        if query in ['exit','stop']:
            speak('thank you!!')
            exit(0)
            
        if query!="none":
            webbrowser.open(query+".com")
        