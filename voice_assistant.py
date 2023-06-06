import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('clearing background noices .. please wait')
        print('ask something ')
        recordedaudio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(recordedaudio)
    except Exception as ex:
        print(ex)
    if 'chrome' in command:
        a='opening chrome..'
        engine.say(a)
        engine.runAndwait()
        program="C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait ()
    if 'play'in command:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(command)
    




