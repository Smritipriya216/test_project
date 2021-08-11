from math import inf
from os import times
from posixpath import commonpath
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:  
        with sr.Microphone() as source:
             hour = int(datetime.datetime.now().hour)
             if hour>= 0 and hour<12:
                 talk("Good Morning Sir !")

             elif hour>= 12 and hour<18:
                 talk("Good Afternoon Sir !")  

             else:
                 talk("Good Evening Sir !") 

            talk("I am your Assistant")
            talk("How can i help you")
            print("You can speak now, I am listening:")
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
           

    except Exception :
        print("Unable to recognize your voice")
        return None
    return command

# def run_jarvis():
    
while True:
    command = take_command().lower()
    print(command)

    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p') 
        print("Current time is : " + time)
        talk('current time is' + time)
    
    elif 'date' in command:
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        print("Today's Date is : " + date)
        talk("Today's Date is : " + date)
    
    elif 'who is' in command or 'tell me about' in command or 'what' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    
    elif 'are you single' in command:
        talk('no,I am in relationship with WIFI')
        print('no,I am in relationship with WIFI')
    
    elif 'do you love me' in command:
        talk('Yeah , you are an amazing person and i like you')
        print('Yeah , you are an amazing person and i like you')

    elif 'joke' in command:
        fun=pyjokes.get_joke()
        talk(fun)
        print(fun)
    
    elif 'fun' in command:
        talk('Thank you for the compliment')
    
    else:
        talk('Please say again.')


# run_jarvis()
