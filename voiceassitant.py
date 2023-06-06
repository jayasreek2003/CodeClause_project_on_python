import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble recognizing your voice.")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hello there!")
    elif "how are you" in command:
        speak("I'm doing well, thank you!")
    elif "what's your name" in command:
        speak("I am your voice assistant.")
    elif "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

speak("Hello! How can I assist you today?")
while True:
    command = listen()
    process_command(command)
