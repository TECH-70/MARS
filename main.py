import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

## ==> GLOBALS
counter = 0

# IMPORT FUNCTIONS
from ui_functions import *

#main artificial recursions script...
from tkinter import *
#from PIL import ImageTk, Image
import numpy
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess,pyjokes, pickle, winshell
from time import ctime
import finder
import cv2
#import cam
import requests
import ctypes
from bs4 import BeautifulSoup
import win32api
#import numpy as np
from datetime import *
#import cv2
from time import *
import os
import time
import playsound
from ttkSimpleDialog import ttkSimpleDialog as t
import ttkSimpleDialog as t
from ttkSimpleDialog import ttkSimpleDialog as t
from pyttsx3.drivers import sapi5

client = wolframalpha.Client('Your_App_ID')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

url = "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/8fad677d-7b1f-40a2-b5d3-4c28f8fb1f9b"
api = "ajHj3HaKxB3anfbFklNorme0ewJ7Yywh8dvN9NPPqNSG"

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

Auth = IAMAuthenticator(api)
tts = TextToSpeechV1(authenticator=Auth)
tts.set_service_url(url)
def speak(words):
	VoiceMod = f'<prosody pitch="low">{words}</prosody>'
	with open('./tts_converted.mp3','wb') as audio_file:
		res = tts.synthesize(VoiceMod, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
		audio_file.write(res.content)


def myCommand():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold =  1
		audio = r.listen(source)
	try:
		query = r.recognize_google(audio, language='en-in')
		print('User: ' + query + '\n')

	except sr.UnknownValueError:
		speak('Try again')
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		pass

	return query


def cam():
	cam = cv2.VideoCapture(0)

	cv2.namedWindow("test")

	img_counter = 0

	while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break
		cv2.imshow("test", frame)

		k = cv2.waitKey(1)
		if k%256 == 27:
		# ESC pressed
			print("Escape hit, closing...")
			break
		elif k%256 == 32:
		# SPACE pressed
			img_name = "opencv_frame_{}.png".format(img_counter)
			cv2.imwrite(img_name, frame)
			print("{} written!".format(img_name))
			img_counter += 1

	cam.release()

	cv2.destroyAllWindows()

def WeatherFunction():
	place = str(myCommand())
	search = f"Weather in {place}"
	url = f"https://www.google.com/search?q={search}"
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	update = soup.find("div", class_="BNeawe").text
	speak(f"{search} now is {update}")
	playsound('./tts_converted.mp3')
	os.remove('./tts_converted.mp3')

def find_file(root_folder, rex):
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			result = rex.search(f)
			if result:
				print(os.path.join(root, f))
				break

def find_file_in_all_drives(file_name):
	rex = re.compile(file_name)
	for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
		find_file( drive, rex )
		break

def wolfram(Arnab_Goswami):
	i = Arnab_Goswami
	client = wolframalpha.Client('VQ3QP9-YHEAT4EWLU')
	result = client.query(i)
	ans = next(result.results).text
	speak(ans)
	playsound('./tts_converted.mp3')
	os.remove('./tts_converted.mp3')

def clicked():
	print('Working')
	query = myCommand()
	query = query.lower()

	if 'youtube' in query:
		hx = query.replace("search youtube for","")
		tab = ('https://www.youtube.com/search?q=')
		webbrowser.open(tab+hx)
		speak('Youtube has been successfully launched...')
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif 'weather' in query:
		speak("What places weather would you like to know sir...")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		WeatherFunction()

	elif 'camera' in query:
		speak('accessing camera')
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		cam()

	elif 'google' in query:
		speak('okay')
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		speak('what should I search for')
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		hx = str(myCommand())
		tab=("https://www.google.com/search?q=")
		webbrowser.open(tab+hx)
		speak ('here you go')
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif 'music' in query:
		speak(" what do you want to listen to sir...")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		troll = str(myCommand())
		gaana=('https://open.spotify.com/search/')
		webbrowser.open(gaana+troll)


	elif 'time' in query:
		speak (ctime())
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif 'shutdown' in query:
		os.system("shutdown /s")
		speak("okay...your device is on the way of shutdown...goodbye...")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		exit()

	elif 'change background' in query:
		ctypes.windll.user32.SystemParametersInfoW(20,
												0,
												"Location of wallpaper",
												0)
		speak("Background changed succesfully")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')


	elif 'lock window' in query:
			speak("locking the device")
			playsound('./tts_converted.mp3')
			os.remove('./tts_converted.mp3')
			ctypes.windll.user32.LockWorkStation()
			exit()

	elif 'recycle bin' in query:
		winshell.recycle_bin().empty(confirm = True, show_progress = True, sound = True)
		speak("Trash Can has been emptied...")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif "stop listening" in query:
		speak("for how much time you want to stop me from listening to your commands sir")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		a = int(myCommand())
		time.sleep(a)
		print(a)

	elif "restart" in query:
		subprocess.call(["shutdown", "/r"])
		exit()

	elif "write a note" in query:
		speak("What should i write, sir")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		iwe = myCommand()
		pickle.dump(iwe,open("FRED.txt", "wb"))

	elif "show note" in query:
		speak("Showing Notes")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		file = pickle.load(open("FRED.txt", "rb"))
		print(file)
		speak(file)
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')


	elif "calculate" in query.lower():
		app_id = "E46YXW-T5LG6RT7K7"
		client = wolframalpha.Client(app_id)

		indx = query.lower().split().index('calculate')
		query = query.split()[indx + 1:]
		res = client.query(' '.join(query))
		answer = next(res.results).text
		speak("The answer is " + answer)
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif 'open tools' in query:
		the = r'E:\\python projects\\my python files\\microsoft tools (shortcuts)'
		os.startfile(the)
		speak("opening microsoft tools...")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif "read" in query:
		rein = t.askstring("Text reader","Enter text hear to listen")
		speak(rein)
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')

	elif "exit" in query:
		speak ("thanks for giving me your time")
		playsound('./tts_converted.mp3')
		os.remove('./tts_converted.mp3')
		exit()

	else:
		try:
			wolfram(query)
		except:
			speak(' Lets see... I didnt get any results on the web? maybe i couldnt understand you sir...')
			playsound('./tts_converted.mp3')
			os.remove('./tts_converted.mp3')


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self) 
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		UIFunctions.uiDefinitions(self)

		def moveWindow(event):
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()

		self.ui.frame_40.mouseMoveEvent = moveWindow
		## TOGGLE/BURGER MENU
		########################################################################
		self.ui.menu_butt.clicked.connect(lambda: ToggleMenu.toggleMenu(self, 250, True))

		## PAGES 
		########################################################################

		# PAGE 1
		self.ui.V2.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.v2))
		self.ui.Desktop.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.Desktop_2))
		self.ui.profile.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.Profile))
		#self.ui.buttboi.clicked.connect(self.file)
		self.ui.mic.clicked.connect(self.startkeromarf)


		self.show()

	def file(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			print(fileName)

	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()

	def startkeromarf(self):
		clicked()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_SplashScreen()
		self.ui.setupUi(self)

		## UI ==> INTERFACE CODES
		########################################################################

		## REMOVE TITLE BAR
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


		## DROP SHADOW EFFECT
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 60))
		self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

		## QTIMER ==> START
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.progress)
		# TIMER IN MILLISECONDS
		self.timer.start(35)

		# CHANGE DESCRIPTION

		# Initial Text
		self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

		# Change Texts
		QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
		QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


		## SHOW ==> MAIN WINDOW
		########################################################################
		self.show()
		## ==> END ##

	## ==> APP FUNCTIONS
	########################################################################
	def progress(self):

		global counter

		# SET VALUE TO PROGRESS BAR
		self.ui.progressBar.setValue(counter)

		# CLOSE SPLASH SCREE AND OPEN APP
		if counter > 100:
			# STOP TIMER
			self.timer.stop()

			# SHOW MAIN WINDOW
			self.main = MainWindow()
			self.main.show()

			# CLOSE SPLASH SCREEN
			self.close()

		# INCREASE COUNTER
		counter += 1




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = SplashScreen()
	sys.exit(app.exec_())