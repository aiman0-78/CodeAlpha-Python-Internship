import speech_recognition as sr  #for conversion of voice into text
import pyttsx3   #for conversion of text to speech
import datetime   #for getting current date and time
import wikipedia   #for searches wikipedia
import webbrowser   #for open websites
import os            #for open apps like notepad
import pyjokes        #for getting funny jokes

def speak(text): #function speak that take text and print this text on screen
    print(f"Assistant : {text}") 
    try:
        engine= pyttsx3.init() #initialized pttsx3 speech engine 
        engine.say(text)       #Passes the text to the speech engine to speak
        engine.runAndWait()    #Runs the engine and waits until speaking is finished
    except: #if some thing wrong it give error massage
        print("speech output not supported in colab")
def wish_user(): #function for getting current hours from 0-23
    hour = int(datetime.datetime.now().hour)
    if hour < 12: #if it before 12 then say"Good Morning"
        speak("Good Morning!")
    elif hour < 18: #if it before 6pm than it say "Good afternoon"
        speak("Good Afternoon!")
    else:      #if it after 6pm than it say "Good Evening"
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")
def take_command(): #voice input function
    r=sr.Recognizer() #create a recoganizer object r to process audio
    with sr.Microphone() as source:   #Opens the microphone and prompts "Listening..."
        speak("Listening...") 
        audio = r.listen(source)  #Records audio from the microphone.
    try:
        command = r.recognize_google(audio)   #Uses Google's API to convert audio to text and saves it in command
        print(f"You: {command}")  #print what you said
        return command.lower()    #return it in lower case
    except sr.UnknownValueError:  #If speech was unclear, informs the user and returns empty string
        speak("Sorry,I did not catch that.")
        return ""
    except sr.RequestError:   #If Google's service is unavailable, says so and returns empty string
        speak("Sorry, The service is down.")
        return ""
def run_assistant():   #main assistant function
    wish_user() #Starts by greeting the user.
    while True:   #Loops forever, listening to user commands.
        query = take_command() 
        if 'wikipedia' in query: #handle wikipedia command

            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","") #query is only wikipedia it give empty string
            try: #if some topic on wikipedia it give 2 sentence on search topic from wikipedia
                result=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia:")
                speak(result)
            except:  #If assistant not understand
                speak("Sorry, I couldn't find anything.")
        elif 'open youtube' in query:   #for opening youtube
            speak("Opening YouTube...")

            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:  #for opening google
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif 'open tiktok' in query:    #for opening tiktok
            speak("Opening Tiktok...")
            webbrowser.open("https://www.tiktok.com")
        elif 'open facebook' in query:   #for opening facebook
            speak("Opening Facebook...")
            webbrowser.open("https://www.facebook.com")
        elif 'open instagram' in query:   #for opening instagram
            speak("Opening instagram...")
            webbrowser.open("https://www.instagram.com")
        elif 'time' in query:      #for accessing current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
        elif 'joke' in query:   #for getting job on programing
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'open notepad' in query:   #for opening notepad
            os.system('notepad.exe')
        elif 'search' in query:        #for searching any query from google
            speak("What should I search for?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif 'exit' in query or 'bye' in query:   #for ending the conversation
            speak("Goodbye! Have a nice day")
            break
        else:    #if some query not understand by assistant
            speak("sorry, I didn't understand that. try again.")
run_assistant()   #calling of run_assistant function