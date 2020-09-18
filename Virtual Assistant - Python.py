import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import pyautogui
import random
import psutil
e = pyttsx3.init()
def screenshot():
    a=random.randint(1,10)
    a=str(a)
    img=pyautogui.screenshot()
    img_path1="C:\\Users\\ROOBAN\\Desktop\\New folder\\"
    img_exe=".png"
    img_name="s"+a
    img.save(img_path1+img_name+img_exe)
def speak(audio):
    voices = e.getProperty('voices')
    e.setProperty('voice',voices[1].id )
    e.say(audio)
    e.runAndWait()
def cpu():
     cpu_usage = str(psutil.cpu_percent())
     speak("Your CPU usage percent is" + cpu_usage)
     battery=psutil.sensors_battery()
     speak("Your battery percent is")
     speak(battery.percent)
speak("Hello Sir, Iam your personal Assistant called as JARVIS")
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome back sir!!")
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Night Sir")
    speak("How can I help you Sir!")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in")
        print(query)
    except:
        speak("Please say it again")
        takecommand()
    return query
def playsongs():
    songs_dir = "E:\\SONGS\\New songs"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[1]))
 
if __name__== "__main__":
    wishme()
    while True:
         query = takecommand().lower()
         if "time" in query:
             time()
         elif "date" in query:
             date()
         elif "wikipedia" in query:
             speak("Searching....")
             query=query.replace("wikipedia","").replace("search","").replace("on","")
             result = wikipedia.summary(query,sentences=2)
             print(result)
             speak(result)
         elif "open" in query:
             search = query.replace("open","")
             speak("opening" + search)
             chromedriver ="E:\chromedriver.exe"
             driver = webdriver.Chrome(chromedriver)
             search=search.join(["https://www.",".com"])
             search=search.replace(" ","")
             print(search)
             driver.get(search)
         elif "cpu" in query:
             cpu()
         elif "search" and "google" in query:
             search_item=query.replace("search","").replace("google","").replace("in","")
             chromedriver ="E:\chromedriver.exe"
             driver = webdriver.Chrome(chromedriver)
             driver.get("https://www.google.com/")
             inputElems = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
             inputElems.send_keys(search_item)
             inputElems = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
             #inputElems.click()
             inputElems=driver.find_element_by_class_name("gNO89b")
             inputElems.click()
         elif "screenshot" in query:
             screenshot()
             speak("Screenshot is done")
         elif "search" and "youtube" in query:
             search_item=query.replace("search","").replace("youtube","").replace("in","")
             chromedriver ="E:\chromedriver.exe"
             driver = webdriver.Chrome(chromedriver)
             driver.get("https://www.youtube.com/")
             inputElems = driver.find_element_by_xpath('//*[@id="search"]')
             inputElems.send_keys(search_item)
             inputElems = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
             #inputElems.click()
             inputElems=driver.find_element_by_class_name("style-scope ytd-searchbox")
             inputElems.click()
             time.sleep(5)
         elif "who are you" in query:
             speak("Iam your personal Assistant")
         elif "name" in query:
             speak("Your name is rooban")
         elif "play songs" in query:
            speak("Playing Songs")
            playsongs()
         elif "remember that" in query:
             speak("What I should remember")
             data=takecommand()
             remember = open("data.txt","w")
             remember.write(data)
             remember.close()
         elif "offline" or "Goodbye" or "exit"in query:
             speak("Good bye sir, Have a nice day!")
             quit()
