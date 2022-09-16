import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour< 18:
        speak("Good Afternoon")

    else :
        speak("Good Evening!")

    speak("I am Stormy. Please tell me, how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Attending...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source) 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
       #print(e)  
       print("Say that again please....") 
       return "None"
    return query

if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'classroom' in query:
            webbrowser.open("classroom.google.com")
        
        elif 'meet' in query:
            webbrowser.open("meet.google.com")
        
        elif 'potify' in query:
            codePath = "C:\\Users\\anika\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
    #speak("Sonika Says, that Every on has beauty but no on can see it. hmmm")