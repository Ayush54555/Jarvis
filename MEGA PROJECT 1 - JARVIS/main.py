import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="0d8dc367f8764df59121568819396493"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the json response
            data = r.json()

            #Extract the articles
            articles = data.get('articles',[])

            #Print the headlines
            for article in articles:
                speak(article['title'])



if __name__ == "__main__": #this shows if we are running code directly else we are importing from another file
    speak('Initializing Jarvis......')
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone
        r=sr.Recognizer()
        



        #recognize speech using google
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)  #Now this step listens what we speak to our system timeout ka mtlb kitne seconds wait karega hamari phrase start hone tak. Phase time mtlb phrase ko kitne seconds tak listen karega
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("How can i help you sir")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
 
