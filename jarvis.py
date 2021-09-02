import pyttsx3
import speech_recognition
import datetime
import wikipedia
import pyaudio
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("hello! i am jarvis .please tell me how i can help you") 

def takecommand():
    r = speech_recognition.Recognizer() 
    with speech_recognition.Microphone() as source:
        print("listening....!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"    
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
speak("sada is a good boy and he want to know about all thing in  world")
wishme()
while True:
      query = takecommand().lower()


      if "wikipedia" in query:
         speak('searching wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak(results)

      elif "open youtube" in query:
          webbrowser.open(youtube.com)
      elif "open facebook" in query:
          webbrowser.open(facebook.com)
      elif "open instagram " in query:
          webbrowser.open(instagram.com)    
      elif "open stackoverflow" in query:
          webbrowser.open("stackoverflow.com")
      elif "play music" in query:
          music_dir = 'C:\sadamusic'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[0]))
      elif "the time" in query:
          strtime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir the time is {strtime}")

      elif "open python"  in query:
          codepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.9"
          os.startfile(codepath)
      elif "send email to sada" in query:
          try:
              speak("what should i say?")
              content = takecommand()
              to = "ssadagupta@gmail.com"
              sendemail(to,content)
              speak("email has been sent")
          except Exception as e:
               print(e)
               speak("sorry my friend i am unable to send")



