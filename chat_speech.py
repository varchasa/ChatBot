import chatterbot
import speech_recognition as sr
import pyttsx3
import sys

bot=chatterbot.ChatBot('bot',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
try:
    r=sr.Recognizer()
    while True:
        speak('You : ')
        print("you : ")
        with sr.Microphone() as source:
            audio=r.listen(source)
        user=r.recognize_google(audio)
        print("you : ",user)
        ans=bot.get_response(user)
        speak(ans)
        print('bot : ',ans)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    speak('google speech recognition could not understand audio')
    sys.exit()
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    sys.exit()

    
