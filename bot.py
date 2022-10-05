import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyautogui
from datetime import datetime
import time
import pyaudio
from gtts import gTTS
import subprocess
import wikipedia
import calendar
from datetime import date
from googletrans import Translator

#initialize all modules
listener = sr.Recognizer()
audio = pyttsx3.init()
translator = Translator()

nightmode = False
calc_words = ['0', '1', '2', '3', '5', '6', '7', '8', '9']

#allow bot to speak
def speak(text):
    audio.setProperty('rate', 150,)
    audio.say(text)
    audio.runAndWait()
    listen12()

def enter_command(command1):
    command1 = command1.replace('Jarvis', '')
    global nightmode

    if command1 == 'play':
        pyautogui.press('Space')

    elif 'play' in command1:
        command1 = str(command1).replace('jarvis', '')
        song = command1.replace('play', '')
        pywhatkit.playonyt(song)
        speak(f'playing {song}')

    elif 'pause' in command1:
        pyautogui.press('Space')

    elif command1 == 'unpause':
        pyautogui.press('Space')
    
    elif 'the time' in command1:
        speak(datetime.today().strftime("%I:%M %p"))

    elif 'close' in command1:
        pyautogui.keyDown('alt')
        pyautogui.keyDown('f4')
        time.sleep(.5)
        pyautogui.keyUp('f4')
        pyautogui.keyUp('alt')
    elif 'volume down' in command1:
        pyautogui.press('down')

    elif 'volume up' in command1:
        pyautogui.press('Up')

    elif 'say' in command1:
        word1 = command1.replace('say', '')
        speak(word1)
    
    elif 'calculate' in command1:
        command1 = command1.replace('calculate', '')
        command1 = command1.replace('Jarvis', '')
        command1 = command1.replace('÷', '/')
        if 'number' in command1:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('number', '')
            command1 = command1.replace('times', '*')
            with open('calc.txt')as ca2:
                current_total = ca2.read()
            command1 = command1.replace('jarvis', '')
            calc = command1.replace('number', '')
            calc = calc.replace('x', '*')
            calc = current_total + calc
            total = str(eval(calc))
            with open('calc.txt', 'w')as ca1:
                ca1.write(total)
            with open('pyperclip.txt', 'w')as clp1:
                clp1.write('ebtru2rjhntur2ijrnye27i2jkm7m24iujnrug34jm7hr3jghntn783j:::sg:clipboard'+total)
            speak(total)


        else:
            command1 = command1.replace('jarvis', '')
            calc = command1.replace('what is', '')
            calc = calc.replace('x', '*')
            total = str(eval(calc))
            with open('calc.txt', 'w')as ca1:
                ca1.write(total)
            with open('pyperclip.txt', 'w')as clp1:
                clp1.write('ebtru2rjhntur2ijrnye27i2jkm7m24iujnrug34jm7hr3jghntn783j:::sg:clipboard'+total)
            speak(total)

    elif 'search' in command1:
        command1 = command1.replace('search', '')
        command1 = command1.replace('jarvis', '')
        command1 = command1.replace('Jarvis', '')
        command1 = command1.replace(' ', '')
        url = command1.replace('open', '')
        with open('url.txt', 'w') as f1:
            f1.write(url)
            
    elif 'date' in command1:
        date1 = date.today()
        month = calendar.month_name[date1.month]
        speak(f'the current date is {date1.day}{month}{date1.year}')
    
    elif 'who is' in command1:
        command1 = command1.replace('jarvis', '')
        name11 = command1.replace('who is', '')
        result = wikipedia.summary(name11)
        result = str(result).split('.')
        result = result[0].replace('( (listen) a(w)l-BAY-nee-ə; ', '')
        speak(result)

    elif 'what is' in command1:
        if any(x in command1 for x in calc_words):
            command1 = command1.replace('Jarvis', '')
            command1 = command1.replace('÷', '/')
            if 'number' in command1:
                command1 = command1.replace('jarvis', '')
                command1 = command1.replace('number', '')
                command1 = command1.replace('times', '*')
                with open('calc.txt')as ca2:
                    current_total = ca2.read()
                command1 = command1.replace('jarvis', '')
                calc = command1.replace('number', '')
                calc = calc.replace('x', '*')
                calc = current_total + calc
                total = str(eval(calc))
                with open('calc.txt', 'w')as ca1:
                    ca1.write(total)
                with open('pyperclip.txt', 'w')as clp1:
                    clp1.write('ebtru2rjhntur2ijrnye27i2jkm7m24iujnrug34jm7hr3jghntn783j:::sg:clipboard'+total)
                speak(total)

            else:
                command1 = command1.replace('jarvis', '')
                calc = command1.replace('what is', '')
                calc = calc.replace('x', '*')
                total = str(eval(calc))
                with open('calc.txt', 'w')as ca1:
                    ca1.write(total)
                with open('pyperclip.txt', 'w')as clp1:
                    clp1.write('ebtru2rjhntur2ijrnye27i2jkm7m24iujnrug34jm7hr3jghntn783j:::sg:clipboard '+total)
                speak(total)

        else:
            command1 = command1.replace('jarvis', '')
            name11 = command1.replace('what is', '')
            result = wikipedia.summary(name11)
            result = str(result).split('.')
            result = result[0].replace('( (listen) a(w)l-BAY-nee-ə; ', '')
            speak(result)

    elif 'morning' in command1:
        speak('good morning. how may i help you today')

    elif 'evening' in command1:
        speak('evening. how may i help you')

    elif nightmode == True:
        if 'good night' in command1:
            nightmode = True
            speak('good night')

        elif 'goodnight' in command1:
            nightmode = True
            speak('good night')

    elif 'good night' in command1:
        if nightmode == False:
            nightmode = True
            speak('good night. is there any thing i can help with before sleep')
        else:
            False

    elif 'goodnight' in command1:
        nightmode = True
        speak('good night. is there any thing i can help with before sleep')
    
    elif 'open' in command1:
        command1 = command1.replace('jarvis', '')
        command1 = command1.replace('Jarvis', '')
        app1 = command1.replace('open', '')
        with open('app.txt', 'w')as p1:
            p1.write(app1+'4r6j38rj3imyr83rjmy373o4krym389r3ijkr9w:app')

    elif 'close app' in command1:
        command1 = command1.replace('jarvis', '')
        command1 = command1.replace('Jarvis', '')
        cl_app = command1.replace('open', '')
        with open('app.txt', 'w')as p2:
            p2.write(cl_app+'4r6j38rj3imyr83rjmy373o4krym389r3ijkr9w:close')

    elif 'text' in command1:
        if 'in Albanian' in command1:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('Jarvis', '')
            message = command1.replace('text', '')
            message = message.replace('in Albanian', '')
            message = translator.translate(message, dest='sq').text
            with open('message_bot\\msg.txt', 'w')as msg1:
                msg1.write(message)

        elif 'to Albanian' in command1:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('Jarvis', '')
            message = command1.replace('text', '')
            message = message.replace('to Albanian', '')
            message = translator.translate(message, dest='sq').text
            with open('message_bot\\msg.txt', 'w')as msg1:
                msg1.write(message)
        
        else:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('Jarvis', '')
            message = command1.replace('text', '')
            with open('message_bot\\msg.txt', 'w')as msg1:
                msg1.write(message)



    elif 'message' in command1:
        if 'in Albanian' in command1:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('Jarvis', '')
            message = command1.replace('message', '')
            message = message.replace('in Albanian', '')
            message = translator.translate(message, dest='sq').text
            with open('message_bot\\msg.txt', 'w')as msg1:
                msg1.write(message)

        elif 'to Albanian' in command1:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('Jarvis', '')
            message = command1.replace('message', '')
            message = message.replace('to Albanian', '')
            message = translator.translate(message, dest='sq').text
            with open('message_bot\\msg.txt', 'w')as msg1:
                msg1.write(message)
        
        else:
            command1 = command1.replace('jarvis', '')
            command1 = command1.replace('Jarvis', '')
            message = command1.replace('message', '')
            with open('message_bot\\msg.txt', 'w')as msg1:
                msg1.write(message)

def listen12():
    while True:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            enter_command(str(command))
listen12()