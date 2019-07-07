import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning ! have a nice day")

    elif hour>12 and hour  <=18:
        speak("Good Afternoon !")

    else:
        speak("Good evening")

    speak("I am shiny developed by jonty , how may i help you ")

def takeCommand():
    #it takes micrrophone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return"None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()


        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'in youtube' in query:
            webbrowser.open("youtube.com/watch?v=bhVH0C-6f8Q")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir , the time is {strTime}")

        elif 'wish my mom' in query:
            speak("happy birthday mummy")
        
        elif 'thank you' in query:
            speak("it's my plasure sir")

        elif 'who are you' in query:
            speak("i am virtual assistant at your service , sir")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'riya' in query:
            webbrowser.open(" riya is the most beautiful girl in the world ")
        

        
        