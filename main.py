# pip install ChatterBot==1.0.4
# pip install chatterbot-corpus==1.2.0


#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
from playsound import playsound
import pyttsx3
engine = pyttsx3.init()


chatbot = ChatBot('Ron Obvious')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

r = sr.Recognizer()
chatInProgress = True
while chatInProgress:
    with sr.Microphone() as source:
        audio = r.listen(source)
        playsound('startup.mp3')
    try:
        me = r.recognize_google(audio)
        print(me)
        response = chatbot.get_response(me)
        if me == "end" or me == "goodbye":
            print(chatbot.get_response("goodbye"))
            exit(1)
            chatInProgress = False
        else:
            engine.say(response)
            print(response)
            engine.runAndWait()
    except sr.UnknownValueError:
        print("I did not understand")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        chatbot.get_response(me)
