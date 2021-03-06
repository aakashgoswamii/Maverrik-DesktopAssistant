import pyttsx3
import json,requests
import speech_recognition as sr
import datetime
import wikipedia
import random
import psutil
import webbrowser
import os
import pyjokes
import pywhatkit as kit
import cv2
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def todayDate():
    weekDay = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    d1 = datetime.date.today().strftime("%B %d %Y")
    currDate = weekDay[datetime.datetime.now().isoweekday()] + " " + d1
    return currDate

def minimumTemp():
    user_api = "6ca7f6a67b34d910ceb437aa835c2b9f"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + "ghaziabad" + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    miniTemp = "{:.2f}".format(api_data['main']['temp_min'] - 273)
    return miniTemp


def maximumTemp():
    user_api = "6ca7f6a67b34d910ceb437aa835c2b9f"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + "ghaziabad" + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    maxiTemp = "{:.2f}".format(api_data['main']['temp_max'] - 273)
    return maxiTemp


def currentTemp():
    user_api = "6ca7f6a67b34d910ceb437aa835c2b9f"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + "ghaziabad" + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    currTemp = "{:.2f}".format(api_data['main']['temp']-273)
    return currTemp


def currentWeather():
    user_api = "6ca7f6a67b34d910ceb437aa835c2b9f"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + "ghaziabad" + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    currWeather = api_data['weather'][0]['description']
    return  currWeather


def systemDetail():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugStatus = ""
    if plugged==True:
        plugStatus += "plugged in"
    else:
        plugStatus += "plugged out"
    return f"I am fine, sir. All systems are at 100 percent. Battery percentage is {percent} and currently system is {plugStatus}"


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("goswami.aakash2244@gmail.com","Swaggo@2244")
    server.sendmail("goswami.aakash2244@gmail.com",to,content)
    server.close()



def takeCommand():
    # It take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"

    return  query



def intro():
    speak( "I am JARVIS , the robot. Speed 1 terahertz, memory 1 zigabyte. How can I help You?")


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir. How are you doing.")

    elif hour == 12:
      speak("Good Afternoon Sir. Do not forget to take sun cream with you sir.")

    elif hour>12 and hour<16:
        speak("Good evening sir.")

    else:
        speak("Good evening sir. How was your day today?")


if __name__=="__main__":

    wishMe()

    intro()

    while True:

        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching in  wikipedia.')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open facebook' in query:
            speak("Opening facebook...")
            webbrowser.open("https://www.facebook.com")


        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("https://www.youtube.com")


        elif 'open geeks for geeks' in query:
            speak("Opening geeks for geeks")
            webbrowser.open("https://www.geeksforgeeks.org")


        elif 'open w3 schools' in query:
            speak("Opening w3 schools...")
            webbrowser.open("https://www.w3schools.com")


        elif 'romantic song' in query or 'thinking about someone' in query:
            speak("Feeling loved . I have something for you.")
            musicFolder ='C:\\Users\\AAKASH\\Desktop\\Maverrik\\Song\\romantic'
            songs= os.listdir(musicFolder)
            os.startfile(os.path.join(musicFolder,songs[random.randint(0,2)]))


        elif 'party'in query:
            speak("Playing party song...")
            musicFolder ='C:\\Users\\AAKASH\\Desktop\\Maverrik\\Song\\partySong'
            songs= os.listdir(musicFolder)
            os.startfile(os.path.join(musicFolder,songs[random.randint(0,2)]))


        elif 'sad song' in query or 'make me sad'in query:
            speak("As  you wish sir.")
            musicFolder ='C:\\Users\\AAKASH\\Desktop\\Maverrik\\Song\\sadSongs'
            songs= os.listdir(musicFolder)
            os.startfile(os.path.join(musicFolder,songs[random.randint(0,1)]))


        elif 'haryanvi' in query:
            speak("Open haryanvi song")
            musicFolder ='C:\\Users\\AAKASH\\Desktop\\Maverrik\\Song\\haryanviSong'
            songs= os.listdir(musicFolder)
            os.startfile(os.path.join(musicFolder,songs[random.randint(0,1)]))

        elif 'open webcam'in query:
            speak("Opening webcam...")
            codePath = ""
            os.startfile(codePath)


        elif 'time' in query:
            timeNow = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {timeNow}")


        elif 'open code'in query:
            speak("Opening code...")
            codePath = "C:\\Users\\AAKASH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'command prompt'in query:
            speak("Opening command prompt...")
            codePath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(codePath)

        elif 'paint' in query:
            speak("Opening paint...")
            codePath = "C:\Windows\system32\\mspaint.exe"
            os.startfile(codePath)

        elif 'open notepad'in query:
            speak("Opening notepad...")
            codePath = "C:\Windows\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'who are you'in query:
            speak("I am JARVIS sir")


        elif 'who ceated you'in query:
            speak(" IRONMAN is the one who created me")


        elif 'hello'in query:
            speak("WEll HELLO SIR . ")


        elif 'are you there' in query:
            speak("Yes sir.")

        elif 'wake up' in query:
            speak("I am always here for you  sir")

        elif 'stack' in query:
            speak("Opening stack overflow...")
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open google'in query:
            speak("What should i search on google")
            takeComm = takeCommand().lower()
            speak(f"Searching{takeComm} on google")
            webbrowser.open(f"{takeComm}")

        elif 'play video on youtube'in query:
            speak("Which video should i play on youtube")
            takeComm = takeCommand().lower()
            speak(f"Playing {takeComm} on youtube...")
            kit.playonyt(takeComm)

        elif 'email'in query:
            try:
                speak("Whom you want to send message?")
                person = takeCommand().lower()
                speak("What should i say?")
                content = takeCommand().lower()
                speak(f"Sending message to {person}.")
                to =  "goswami.aakash2244@gmail.com"
                sendEmail(to,content)
                speak(f"Email has been sent to {person} successfully")
            except Exception as e:
                print(e)
                speak(f"Sorry Sir. I am not able to send message to {person}. Please try again")



        elif 'open camera'in query:
            speak("Opening Camera...")
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 30:
                    break
            cap.release()
            cv2.destroyAllWindows()


        elif 'jarvis stand' in query:
            speak("Well... JARVIS stands for  JUST   A   RATHER   VERY  INTELLIGENT  SYSTEM")


        elif 'how are you' in query:
            speak(systemDetail())


        elif 'prime minister'in query:
            speak("Narendra Modiji is our prime minister")


        elif 'anthem'in query:
            musicFolder = 'C:\\Users\\AAKASH\\Desktop\\Maverrik\\Song\\anthem'
            songs = os.listdir(musicFolder)
            os.startfile(os.path.join(musicFolder, songs[random.randint(0, 1)]))


        elif 'national song'in query:
            musicFolder = 'C:\\Users\\AAKASH\\Desktop\\Maverrik\\Song\\nationalSong'
            songs = os.listdir(musicFolder)
            os.startfile(os.path.join(musicFolder, songs[random.randint(0, 1)]))


        elif 'minimum temperature' in query:
            speak(f"Sir  the minimum temperature in your area is {minimumTemp()} degree celsius")


        elif 'maximum temperature'in query:
            speak(f"Sir the maximum temperature in your area is {maximumTemp()} degree celsius")


        elif 'current temperature' in query or 'temperature' in query:
            speak(f"sir the current temperature in your area is {currentTemp()} degree celsius")

        elif 'social media'in query:
            speak("sure sir. What should i check?")
            if 'check my facebook' in query:
                speak("Checking facebook...")

        elif 'weather' in query:
            speak(f"Sir weathher in yoour arrea is {currentWeather()}")


        elif 'location' in query:
            speak("Sir your current location is ghaziabad")


        elif "date" in query:
            speak(f"Sir, today is {todayDate()}")


        elif 'josh'in query:
            speak("Highh sir")

        elif 'ip address'in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Sir your IP address is {ip}")


        elif 'se bolo'in query:
            speak("JAI MATA DII .")


        elif 'milke'in query:
            speak("JAI MATA DII")


        elif 'college name' in query:
            speak("Sir your college name is  ABES Engineering College")


        elif 'joke'in query:
            speak("Ok sir . Here you are")
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())


        elif 'day'in query:
            speak(todayDate())


        elif "bye" in query or "stop"in query:
            speak("Good bye sir. See you next time")
            quit()