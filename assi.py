import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak('Good Morning!')
	elif hour>=12 and hour<18:
		speak('Good Afternoon!')
	else:
		speak('Good Evening!')

	speak('I am Jarvis Ma'am. Please tell me how may I help you?')


def takeCommand():
	#It takes microphone input from the user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening..')
		r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete i.e 1 sec pause in between can be wait
		audio = r.listen(source)
	try:
		print('Recognizing..')
		query = r.recognize_google(audio, language='en-in')
		print(f'User said: {query}\n')

	except Exception as e:
		print(e)

		print('Say that again please..')
		return 'None'
	return query

def sendEmail(to, content):
	server = smtplib.SMTP( 'smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('yachhna@gmail.com', '********')
	server.sendmail('yachhna@gmail.com',to,content)
	server.close()

 
if __name__ == '__main__':
	wishMe()
	#while True:
	if 1:
		query = takeCommand().lower()
		#Logic for executing task based on query
		if('wikipedia') in query:
			speak('Searching wikipedia..')
			query = query.replace('wikipedia', '')
			results = wikipedia.summary(query, sentences=2)
			speak('According to wikipedia')
			print(results)
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open('youtube.com')

		elif 'open google' in query:
			webbrowser.open('google.com')

		elif 'open stackflow' in query:
			webbrowser.open('stackflow.com')

		elif 'play music' in query:
			music_dir = 'D:\\music'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0])) #Or we can generate a random number from 0 to l-1 and play a song at a random place in the list

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime('%H:%M:%S')
			speak(f'Mam, the time is {strTime}')

		elif 'open sublime' in query:
			sublimePath = 'D:\\Sublime Text 3'
			os.startfile(sublimePath)

		elif 'send email' in query:
			lisu = query.split()
			try:
				speak('What would you like to say?')
				content = takeCommand()
				to = messyaryal@gmail.com
				sendEmail(to, content)
				speak('Email has been sent!')

			except Exception as e:
				print(e)
				speak('Sorry my friend, I am not able to send this email')





