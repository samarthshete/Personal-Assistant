import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import os.path
import subprocess
import pyautogui
import psutil
import wmi


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning,Sir')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon,Sir')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening,Sir')

greetMe()

speak('Hello')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("ssa")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! ')
        
        query=myCommand()
        
    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'am bored' in query or 'am getting bored' in query:
            speak('bored doesnot stand a chance against interesting facts')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open calculator' in query:
            speak('Opening....')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            
        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'screenshot' in query or 'screen shot' in query or 'snapshot' in query:
            speak('ok, sir let me take a snapshot ')
            speak('ok done')
            speak('check your desktop, i saved there')
            pic = pyautogui.screenshot()
            pic.save('C:/Users/Samarth/Desktop/Screenshot.png')


        elif 'send mail' in query:
            speak('ok sir')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('samarthshete14@gmail.com', 'Sam14shete')
            speak('Who is the recepient')
            print (' tell ')
            send = read_voice_cmd().lower()
            print (send)
            speak('what is the subject line')
            print ('tell')
            subject = read_voice_cmd().lower()
            print (subject)
            speak('what is the message')
            print ('tell')
            meaasge = read_voice_cmd().lower()
            print (meaasge)
            server.sendmail('samarthshete14@gmail.com', send,
                            'Subject: ' + subject + ' \n\n ' + meaasge)
        
        elif 'brightness' in query:
            if 'decrease ' in query:
                print ('ok look.......')
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(30, 0)
            elif 'increase ' in query:
                print ('ok look.......')
                ins = wmi.WMI(namespace='wmi')
                methods = ins.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(100, 0)
        elif query == 'how are you' or query == 'how are you sam':
            print ('i am fine.......')
            speak ('i am fine.......')
        elif 'sing a birthday song' in query or 'sing birthday song' in query:
            speak(' happy birth day to you, happy birth day to you')
            speak(' happy birth day to the most amazing person  in the universe')
            speak(' happy birth day to you!')

        elif 'who are you' in query:
            speak('i am not really a person, i am  a i robot')
            speak('i had prefer to think of myself as your friend')
        elif 'great voice' in query or 'beautiful voice' in query:
            speak(' thank you sir')
            speak(' most people think my sound a little stiff')
            speak('maybe they are feeling jealous')

        elif 'drive' in query:
            print ('In Open.......')
            speak('Opening...')
            drive = query[5]
            os.system('explorer ' + drive + ':\\'.format(''))
            print ('ok done')    
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'time' in query:
            now = datetime.datetime.now()
            speak('Sir,Current time is %d hours %d minutes' % (now.hour, now.minute))
        elif 'sing a song' in query:
            speak('la la la la la la la la la la la la ')
            
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif "who made you" in query or "created you" in query: 
            speak ("I have been created by Samarth Shete.")
            
        elif 'hello' or 'hey' or 'hey sam' in query:
            speak('Hello Sir')

        elif 'please remind' in query or 'remind it' in query:
            speak('what should i remind?')
            print ('ok.......')
            speak('ok..')
            with sr.Microphone() as source:
                speech.adjust_for_ambient_noise(source)
                print ('say')
                audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)
                global remind_speech
                remind_speech = speech.recognize_google(audio)
                speak(static_remind_speech + remind_speech)

        elif 'bye' or 'sleep' or 'nothing' or 'ok thanks' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'search' in query:
            webbrowser.open(query)                           
        elif 'play music' or 'play some music' or 'play a song' or 'play music sam' or 'play a song sam' in query:
            print ('ok sir listen.......')
            speak ('ok sir listen.......')
            DIR="D:\Ganna\Bolly"
            music = filter(lambda x: x.lower().endswith("mp3"),os.listdir(DIR))
            music = list(music)
            while 1:
                choice = int(raw_input("Press 1 to play a new song"))
                if choice == 1:
                    song = random.choice(music)
                    webbrowser.open(os.path.join(DIR,song))

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'charge'or 'check battery charging'in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            print (percent)
            if percent < 35:
                speak('sir, please connect charger because i can survive only ' + time_left)
            if percent > 35:
                speak("don't worry, sir charger is connected")
            else:
                speak('sir, no need to connect the charger because i can survive ' + time_left)        
        elif 'shutdown' or 'shutdown the pc' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak('shutting down your computer')
            os.system('shutdown -s')
    
        
        elif 'open notepad' in query: 
            speak("Opening Notepad ") 
            os.system("notepad.txt")    
        elif 'close notepad' in query:
            while 1 :
                os.system("TASKKILL /F /IM notepad.exe")
                time.sleep(10)
        elif 'open word' in query:
            speak("Opening Microsoft Word") 
            os.system("document.docx")
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
