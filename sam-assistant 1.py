import pyttsx3 
import speech_recognition as sr

import pyaudio
import random,os


engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         a = r.listen(source)

         try:

                    return r.recognize_google(a)

         except sr.UnknownValueError:
                print('could not understand audio')

         except sr.RequestError as e:
                print("Recog Error; {0}".format(e))

         return ""



         
def media():
    speak('ok sir')
    speak('starting required application')
    speak('what do you want me to play for you')
    k = listen()
    speak('ok sir playing' + k + 'for you')
    os.startfile('C:/Users/it/Music/Playlists/Music/'+k+'.mp3')


def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')

def gooffline():
    speak('ok sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    quit()



def speak(text):
    engine.say(text)
    engine.runAndWait()
def online():
    speak('Hello Sir')
    speak('starting all system ')
    
    speak('all systems have been started')
    speak('Now i am all set,Sir')
    speak('Howmay i help you')
def mainfunction():
    
    with sr.Microphone() as source:
        a= r.listen(source)
        user = r.recognize_google(a)
        print(user)

        if user in ['sam','Sam','hey sam']:
            online()
    
        elif user == "song":
            media()
    

        elif user == "down":
            gooffline()
        elif user == "shutdown":
            shutdown()
        elif user in ['hi','hey','whatsup','sup','good']:
            d = random.choice(['hey','hi','sup'])
            speak(d)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
         

        while 1:
            mainfunction()
