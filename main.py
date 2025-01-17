import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import os
import streamlit
import subprocess

listener =  sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening..")
            voice  = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'professor' in command:
                command = command.replace('professor','')
                print(command)
    
    except Exception as e:
        raise e
    
    return command

def run_assistant():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play','')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("current time is " + time)

    elif 'name' in command:
        speak("My name is Professor")

    elif 'joke' in command:
        speak(pyjokes.get_jokes())

    elif 'wikipedia' in command:
        speak("Searching wikipedia")
        query = command.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia...")
        print(results)
        speak(results)

    elif 'generate email' in command:
        os.system("app.py")
        # from subprocess import call
        # call(["streamlit run app.py", "-1"])
        # command = 'streamlit run app.py'
        # result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    elif 'detect object' in command:
        os.system("object.py")
    
    elif 'detect face' in command:
        os.system("face_detect.py")

    else:
        print("Please say the command again")


if __name__ == "__main__":
    while True:
        run_assistant()
