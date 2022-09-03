import speech_recognition as sr
import pyttsx3
# import pywhatkit
import datetime
import calendar
import wikipedia
import pyjokes
import math
import qrcode

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'malik' in command:
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    # if 'send' in command:
    #     try:
    #         pywhatkit.sendwhatmsg("+919812441174",
    #                               "Hlo thik hogi k",
    #                               1, 1)
    #         print("Successfully Sent!")
            
    #     except:
    #         print("An Unexpected Error!")

    
    if 'calendar' in command:
        cal = calendar.month(2022,3)
        print(cal)

    elif "search wikipedia" in command:
        talk("Checking the wikipedia ")
        command= command.replace("wikipedia", "")
        result = wikipedia.summary(command ,4)
        talk("According to wikipedia")
        print(result)
        talk(result)

    elif 'play' in command:
        song = command.replace('play','')
        talk('playing')
        print('playing...')
        pywhatkit.playonyt(song)

    elif 'search' in command:
        search = command.replace('search','')
        talk('Here are some web search results')
        pywhatkit.search(search)
        print('Here are some web search results')

    elif 'generate' in command:
        img= qrcode.make("https://github.com/MalikJaanvi/Website_Blocker")
        img.save("github.jpg")

    elif 'google' in command:
        google = command.replace('google', '')
        talk('i found this summary')
        talk(print(wikipedia.summary(google)))

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('current time is' + time)
    elif 'date' in command:
        date= datetime.datetime.now()
        print(date.strftime("%x"))
        talk(date.strftime("%x"))
    elif'weekday' in command:
        day = datetime.datetime.now()
        print(day.strftime("%A"))
        talk(day.strftime("%A"))
    elif 'pi' in command:
        print(math.pi)
        talk(math.pi)

    elif 'how are you' in command:
        print('i am fine')
        talk('i am fine thank you')
    elif 'are you single' in command:
        print('no you are my bf')
        talk('no you are my bf')
    elif 'i love you' in command:
        print('i love you too')
        talk('i love you too')
    elif 'good morning' in command:
        print('very cheerful morning to you')
        talk('very cheerful morning to you')
    elif 'good afternoon' in command:
        print('very good afternoon dear')
        talk('very good afternoon dear')
    elif 'good evening' in command:
        print('nice evening babe')
        talk('nice evening babe')
    elif 'good night' in command:
        print('good night jaan sweet dreams')
        talk('good night jaan sweet dreams')
    elif 'who are you' in command:
        print('i m Malik your friend')
        talk(' i m Malik your friend')

    
    elif 'hello' in command:
        talk('hii jaan')
        print('hii jaan')
    elif 'joke' in command:
        A=  talk(pyjokes.get_joke())
        print(A)
    elif "name" in command:
        print('Malik')
        talk('malik')

    elif 'made you' or 'banaya' in command:
        talk('Jaanvi')
    # elif 'banaya' in command:
    #     talk('Miss Jaanvi')
    
   

run_alexa()
