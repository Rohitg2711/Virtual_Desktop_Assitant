

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import random
import requests
from bs4 import BeautifulSoup
import wolframalpha
import webbrowser
import pywhatkit
import pyautogui
import keyboard
from time import sleep
import json
import os
import pyjokes
from plyer import notification
from pygame import mixer


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'play' in query:
             query = query.replace('Jarvis','')
             song = query.replace('play',"")
             speak('playing'+ song)
             pywhatkit.playonyt(song)

        elif "hello" in query:
            speak("Hello sir, how are you ?")
            print("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("That's great, sir")
            print("That's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
            print("Perfect, sir")
        elif "thank you" in query:
             speak("You are welcome, sir")
             print("You are welcome, sir")

        elif 'search' in query:
          a = query.split()
          b = a[1]
          webbrowser.open(b + '.com')
        
        elif 'wikipedia' in query:
              person = query.replace('wikipedia', '')
              info = wikipedia.summary(person, 3)
              print(info)
              speak(info)


        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(f"Sir, the time is {strTime}")  
            speak(f"Sir, the time is {strTime}")


        elif "open" in query:   
                query = query.replace("open","")
                query = query.replace("jarvis","")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
                

        elif "first tab" in query :
                speak("Closing Sir")
                pyautogui.hotkey("ctrl","w")
                speak("First tab is closed")
        elif "second tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak(" Second tab is closed")
        elif "third tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak(" Third tab is closed")
        elif "fourth tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("Fourth tab is closed")
        elif "fifth tab" in query:
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("Fifth tab is closed")
       

        elif "remember that" in query:
           rememberMessage = query.replace("remember that","")
           rememberMessage = query.replace("jarvis","")
           speak("You told me to"+rememberMessage)
           remember = open("Remember.txt","a")
           remember.write(rememberMessage)
           remember.close()
        elif "what do you remember" in query:
          remember = open("Remember.txt","r")
          speak("You told me to" + remember.read())

        elif "tired" in query:
         speak("Playing your favourite songs, sir")
         a = (1,2,3,4,5,6,7,8,9,10)
         b = random.choice(a)
         if b==1:
          webbrowser.open("https://www.youtube.com/watch?v=4N76_rUm3cQ") 
         elif b==2:
            webbrowser.open("https://www.youtube.com/watch?v=-KN8zSxOsEk")
         elif b==3:
            webbrowser.open("https://www.youtube.com/watch?v=Dl-g_s_DBXc")
         elif b==4:
            webbrowser.open("https://www.youtube.com/watch?v=3ONzh3tf884")     
         elif b==5:
            webbrowser.open("https://www.youtube.com/watch?v=RatDV50alQE")   
         elif b==6:
            webbrowser.open("https://www.youtube.com/watch?v=vKb9xwSRrsU")   
         elif b==7:
            webbrowser.open("https://www.youtube.com/watch?v=tFEcQUWLip0")   
         elif b==8:
            webbrowser.open("https://www.youtube.com/watch?v=OnAyBZQc1vk")   
         elif b==9:
            webbrowser.open("https://www.youtube.com/watch?v=5zkR5Zq1Gxk")   
         elif b==10:
            webbrowser.open("https://www.youtube.com/watch?v=6J_ZqAcxxWQ")   

        elif "stop" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "continue" in query:
            pyautogui.press("k")
            speak("video continued")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")
        elif "volume up" in query or "up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif "screenshot" in query or "screen" in query or "shot" in query:
            import pyautogui 
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            speak("Done Sir! Screenshot has been taken")


        elif "click my photo" in query or "photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(6)
            speak("Smile please")
            pyautogui.press("enter")
            speak("Photo has been Clicked!") 
            
        
        
        elif "shutdown" in query:
          speak("Are You sure you want to shutdown")
          shutdown = input("Do you wish to shutdown your computer? (yes/no)")
          if shutdown == "yes":
           os.system("shutdown /s /t 1")
          elif shutdown == "no":
           break

        
        elif "weather" in query or "weather in thane" in query:
          search = "temperature in Thane"
          url = f"https://www.google.com/search?q={search}"
          r  = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temp = data.find("div", class_ = "BNeawe").text
          print(f"current {search} is {temp}")
          speak(f"current {search} is {temp}")

        elif "weather in delhi" in query or "temperature in delhi" in query or "delhi" in query:
          search = "temperature in Delhi"
          url = f"https://www.google.com/search?q={search}"
          r  = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temp = data.find("div", class_ = "BNeawe").text
          print(f"current {search} is {temp}")
          speak(f"current {search} is {temp}")

        elif "weather in Uttar Pradesh" in query or "temperature in Uttar Pradesh" in query or "Uttar Pradesh" in query:
          search = "temperature in Uttar Pradesh"
          url = f"https://www.google.com/search?q={search}"
          r  = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temp = data.find("div", class_ = "BNeawe").text
          print(f"current {search} is {temp}")
          speak(f"current {search} is {temp}")    

        elif "schedule my day" in query or "my day" in query:
            tasks = [] #Empty list 
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takeCommand().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
        
        
        elif "show my schedule" in query or " show" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
            title = "My schedule :-",
            message = content,
            timeout = 15
             )
        
        elif "cricket score" in query or "score" in query:
            from plyer import notification  #pip install plyer
            import requests #pip install requests
            from bs4 import BeautifulSoup #pip install bs4
            url = "https://www.cricbuzz.com/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text,"html.parser")
            team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
            team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
            team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
            team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

            a = print(f"{team1} : {team1_score}")
            b = print(f"{team2} : {team2_score}")

            notification.notify(
                title = "CURRENT SCORE :- ",
                message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                timeout = 15
                )
        

        elif "game" in query:
             speak("Lets Play ROCK PAPER SCISSORS !!")
             print("LETS PLAYYYYYYYYYYYYYY")
             i = 0
             Me_score = 0
             Com_score = 0
             while(i<5):
                 choose = ("rock","paper","scissors") #Tuple
                 com_choose = random.choice(choose)
                 query = takeCommand().lower()
                 if (query == "rock"):
                     if (com_choose == "rock"):
                        speak("ROCK")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                     elif (com_choose == "paper"):
                        speak("paper")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                     else:
                         speak("Scissors")
                         Me_score += 1
                         print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                 elif (query == "paper" ):
                     if (com_choose == "rock"):
                        speak("ROCK")
                        Me_score += 1
                        print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

                     elif (com_choose == "paper"):
                        speak("paper")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                     else:
                        speak("Scissors")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                 elif (query == "scissors" or query == "scissor"):
                     if (com_choose == "rock"):
                        speak("ROCK")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                     elif (com_choose == "paper"):
                         speak("paper")
                         Me_score += 1
                         print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                     else:
                         speak("Scissors")
                         print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                 i += 1
    
             print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}") 

        elif 'quit' in query or 'bye' in query or 'exit' in query:
           speak("Bye Sir!.You Can Call Me Anytime")
           break 
        
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif "news" in query:
             api_dict ={"bussiness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=afba3ff4ae894343a6601337fe599b73",
                        "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=afba3ff4ae894343a6601337fe599b73",
                        "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=afba3ff4ae894343a6601337fe599b73",
                        "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=afba3ff4ae894343a6601337fe599b73"}

            
             content = None
             url = None
             speak("Which field news do you want, [business] , [technology], [sports] , [entertainment] ")
             field = input("Type field news that you want: ")
             for key ,value in api_dict.items():
                 if key.lower() in field.lower():
                    url = value
                    print(url)
                    print("url was found")
                    break
                 else:
                   url = True
                   if url is True:
                    print("url not found")

             news = requests.get(url).text
             news = json.loads(news)
             speak("Here is the first news.")

             arts = news["articles"]
             for articles in arts :
                 article = articles["title"]
                 print(article)
                 speak(article)
                 news_url = articles["url"]
                 print(f"for more info visit: {news_url}")

                 a = input("[press 1 to cont] and [press 2 to stop]")
                 if str(a) == "1":
                    pass
                 elif str(a) == "2":
                  break
                 speak("thats all")




       
           
           

           
           
                




                   
 

  

        








