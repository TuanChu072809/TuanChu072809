- import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os 

friday=pyttsx3.init()
voice=friday.getProperty('voices')
voice=friday.setProperty('voice',voice[1].id)

def speak(audio):
	print('F.R.I.D.A.Y: ' + audio)
	friday.say(audio)
	friday.runAndWait()
def time(): 
	Time=datetime.datetime.now().strftime("%I:%M:%p")
def welcome():
	hour=datetime.datetime.now().hour
	if hour >=6 and hour<12:
		speak("Good morning Zack")
	elif hour >=12 and hour<18:
		speak("Good evening")
	elif hour >=18 and hour<24:
		speak("Good night boss")
	speak('What you want me to help sir')
def command():
	c=sr.Recognizer()
	with sr.Microphone() as source:
		c.pause_threshold=1
		audop=c.listen(source)
	try:
		query=c.recognize_google(audop,language='en')
		print("Admin :" + query)
	except sr.UnknownValueError:
		print("Could you try agian or typing the command ")
		query=str(input('Your command is:'))
	return query

if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
        	speak("What would you like to search?")
        	search=command().lower()
        	url=f"https://www.google.com/search?q={search}"
        	wb.get().open(url)
        	speak(f'I found this on the web {search} on google')
        if "youtube" in query:
        	speak("What would you like to search?")
        	search=command().lower()
        	url=f"https://www.youtube.com/search?q={search}"
        	wb.get().open(url)
        	speak(f'I found this on the web {search} on youtube')
        if "talking" in query:        	
        	search=command().lower()
        	url=f"https://discord.com/channels/q={search}"
        	wb.get().open(url)
        	speak(f'opening chat {search} on discord')
        if "what time it is" in query:
        	time()
        if "hello" in query
            speak("hi")
        if "quit" in query:
            speak("quiting...")
            quit()           
        elif "open podcast":
            Spotify=r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify"
            os.startfile(Spotify)
        
