# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 05:24:36 2020

@author: mrsid
"""

# this is avishkaar

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyjokes


engine = pyttsx3.init()
en_voice_id =" HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice', en_voice_id)


def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
    
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome sir")
    speak("the current time is")
    time()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("good morning sir")
    elif hour >=12 and hour<18:
        speak("good afternoon sir")
    elif hour >=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")
        
    speak("Avishkaar AI is at your service .. please tell me how can i help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        
    
    except Exception as e:
        print(e)
        speak("Pardon please")
        
        return "none"
    
    return query

def sendEmail(to,content):
    server  = smtplib.SMTP('smtp.gmail.com', 587)
    server.echo()
    server.starttls()
    server.login('siddhantsaxenaphy@gmail.com','soixante_et_onze')
    server.sendmail('siddhantsaxenaphy@gmail.com', to, content)
    server.close()
    
def jockes():
    speak(pyjokes.get_joke())

if __name__ == "__main__" :
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query :
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)  
            speak(result)
        elif 'send mail' in query:
            try:
                speak("this mail is going to god siddy")
                to = 'siddhantsaxenanet@gmail.com'
                speak("what is the message sir")
                content = takeCommand
                sendEmail(to, content)
                speak("Your mail has been sent")
             
            except Exception as e :
                print(e)
                speak("unable to send the mail")
        
        elif 'search in chrome' in query:
            speak("what should i search ")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search +'.com')
            
        elif 'logout' in query:
            os.system("shutdown -1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif ' play song' in query:
            songs_dir = 'D:\\Music' 
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif 'remember that' in query:
            speak("what should i remember")
            data = takeCommand()
            speak("you said to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif "do you have any note" in query :
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
        
        elif 'joke' in query:
            jockes()  
            
        elif 'offline' in query:
            quit()
        