from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import smtplib,ssl  #pip install email 
import random
import wikipedia

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am jarvis") 
    else:
        speak("good evening sir i am jarvis")  

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.......")
            audio = R.listen(source)
            
        try:
            print("Recognizing......")
            text = R.recognize_google(audio,language='en-in')
            
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text
    
    def JARVIS(self):
        wish()
            
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()

            elif "shutdown" in self.query:
                speak("Do you really want to shut down your pc Say Yes or else No")
                print("Say Yes or else No")
                ans_from_user=self.STT()
                if 'yes' in ans_from_user:
                    speak('Shutting Down...')
                    os.system('shutdown -s') 
                elif 'no' in ans_from_user:
                    speak('shutdown abort Speak Again')
                    self.STT()

            elif "wikipedia" in self.query:
                speak("searching details....Wait")
                self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                print(results)
                speak(results)

            elif 'open youtube' in self.query or "open video online" in self.query:
                webbrowser.open("https://www.youtube.com")
                speak("opening youtube")
            elif 'open github' in self.query:
                webbrowser.open("https://www.github.com")
                speak("opening github")  
            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook")      
            elif 'open instagram' in self.query:
                webbrowser.open("https://www.instagram.com")
                speak("opening instagram")    
            elif 'open google' in self.query:
                webbrowser.open("https://www.google.com")
                speak("opening google")
                
            elif 'open yahoo' in self.query:
                webbrowser.open("https://www.yahoo.com")
                speak("opening yahoo")
                
            elif 'open gmail' in self.query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail") 
                
            elif 'open snapdeal' in self.query:
                webbrowser.open("https://www.snapdeal.com") 
                speak("opening snapdeal")  
                 
            elif 'open amazon' in self.query or 'shop online' in self.query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            elif 'open flipkart' in self.query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")   
            elif 'open ebay' in self.query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")
            elif 'play music' in self.query or "music" in self.query:
                speak("ok i am playing music")
                music_dir = 'D:/music/'
                musics = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,musics[0]))
            elif 'open video' in self.query or "video" in self.query:
                speak("ok i am playing videos")
                video_dir = 'D:/movies/'
                videos = os.listdir(video_dir)
                os.startfile(os.path.join(video_dir,videos[0]))  
            elif "whats up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)  
                ans_take_from_user_how_are_you = self.STT()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'ok' in ans_take_from_user_how_are_you:
                    speak('okey..')  
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                    speak('oh sorry..')  
            elif 'make you' in self.query or 'created you' in self.query or 'develop you' in self.query:
                ans_m = " For your information Amaan JC Created me ! I give Lot of Thanks to Him "
                print(ans_m)
                speak(ans_m)
            elif "who are you" in self.query or "about you" in self.query or "your details" in self.query:
                about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                print(about)
                speak(about)
            elif "hello" in self.query or "hello Jarvis" in self.query:
                hel = "Hello Amaan JC ! How May i Help you.."
                print(hel)
                speak(hel)
            elif "your name" in self.query or "sweat name" in self.query:
                na_me = "Thanks for Asking my name my self ! Jarvis"  
                print(na_me)
                speak(na_me)
            elif "how you feel" in self.query:
                print("feeling Very sweet after meeting with you")
                speak("feeling Very sweet after meeting with you")
            elif 'open vs code' in self.query:
                codePath = "C:\\Users\\amndwn\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codePath)
            elif 'exit' in self.query or 'abort' in self.query or 'stop' in self.query or 'bye' in self.query or 'quit' in self.query :
                ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
                speak(ex_exit)
                exit()
            
            elif self.query == 'none':
                continue
            else:
                temp = self.query.replace(' ','+')
                g_url="https://www.google.com/search?q="    
                res_g = "sorry! i cant understand but if you want to search on internet say Yes or else No"
                speak(res_g)
                print("Say Yes or No")
                ans_from_user=self.STT()
                if 'yes' in ans_from_user:
                    speak('Opening Google...')
                    webbrowser.open(g_url+temp)
                elif 'no' in ans_from_user:
                    speak('Google Search Aborted,Speak Again')
                    self.STT()

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/redclose.png);border:none;")
        self.exitB.clicked.connect(self.close)

        self.minB.setStyleSheet("background-image:url(./lib/mini40.png);border:none;")
        self.minB.clicked.connect(self.showMinimized)
        self.setWindowFlags(flags)
        def shutDown():
            speak("Shutting down")
            os.system('shutdown /s /t 5') 
            self.shutB.clicked.connect(self.shutDown)
        def reStart():
            speak("Your PC is Restarting")
            os.system('shutdown /r /t 5') 
            self.restartB.clicked.connect(self.reStart)
        
        self.pauseB.clicked.connect(self.close)
            
        self.label_2.setStyleSheet("background-image:url(./lib/dashboard.png);")
        self.label_3.setStyleSheet("background-image:url(./lib/army.png);")
        self.label_6.setStyleSheet("background-image:url(./lib/panel.png);")
        
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()
        
        self.ts = time.strftime("%A, %d %B")
        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText(self.ts)
        self.label_5.setFont(QFont(QFont('Arial',8)))
        

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
