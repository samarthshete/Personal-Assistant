import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
 


engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!,sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!,sir")   

    else:
        speak("Good Evening!,sir")  

    speak("I am Sam. Please tell me how may I help you")       

def command():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
           
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


wishMe()
    
    
query = command()
        
       
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

elif 'open google' in query.lower():
    webbrowser.open("google.com")

elif 'open facebook' in query.lower():
    webbrowser.open("facebook.com")   


elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak("Sir, the time is {strTime}")

        
elif 'open notepad' in query.lower(): 
    speak("Notepad ") 
    os.system("%windir%\\system32\\notepad.exe") 

elif 'open word' in query.lower(): 
    speak("Opening Microsoft Word") 
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE") 
        
elif 'who created you' or 'who made you' in query.lower():
    speak("I was created by Samarth")

if 'Ok,Sam thank you' or 'thank you' in query.lower():
    
    speak("Welcome sir")

if 'where is i am' or 'show me where is i am' or 'show my location' in query.lower():
        query = query.split(" ")
        location = query[2]
        speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        
