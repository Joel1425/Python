    import pyttsx3
    import pytesseract
    from PIL import Image
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser
    import os
    import math
    from bs4 import BeautifulSoup
    import smtplib
    import warnings
    from PyDictionary import PyDictionary
    from twilio.rest import Client
    import requests
    import getpass
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Sir")
        elif hour>=12 and hour<16:
            speak("Good Afternoon Sir")
        else:
            speak("Good Evening Sir") 
        speak("I'm Jarvis. Please say how may i help you")       
    def goodbye_wish():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<4:
            speak("Good night Sir. Sleep well. See you again.")
        elif hour>=4 and hour<14:
            speak("Good Bye Sir. have a good day. See you again.")
        elif hour>=14 and hour<20:
            speak("Good Bye Sir. See you again.")
        else:
            speak("Good Night Sir. See you again.") 
    def takeCommand():
        rec=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            rec.pause_threshold=1
            audio=rec.listen(source)
        try:
            print("Recognizing...")
            query=rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query
    def sendEmail(to, content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo
        server.starttls()
        server.login('itm2017002@iiita.ac.in','justdial')
        server.sendmail('itm2017002@iiita.ac.in',to,content)
        server.close() 
    def provide_weather_data(city):
        units='metric'
        appId='f820a6a338003f3ad4e622ee4b706b2a'
        api_add='http://api.openweathermap.org/data/2.5/weather?q='
        url=api_add+city+'&APPID='+appId+'&units='+units
        # print(url)
        json_data=requests.get(url).json()
        main_weather=json_data['weather'][0]['main']
        temperature=json_data['main']['temp']
        country=json_data['sys']['country']
        minimum=str(math.floor(json_data['main']['temp_min']))
        maximum=str(math.floor(json_data['main']['temp_max']))
        pressure=str(json_data['main']['pressure'])
        temperature=math.floor(temperature)
        temp=str(temperature)
        print("Country: "+country)
        print(main_weather)
        print("Temperature: "+temp+"°C")
        print("Minimum: "+minimum+"°C")
        print("Maximum: "+maximum+"°C")
        print("Pressure: "+pressure+"Pa")
        speak("The temperature in "+city+" located in "+country+" is "+temp+" degree celcius with "+main_weather)
        speak("The minimum and maximum temperatures ranges from "+minimum+" degree celcius to "+maximum+" degree celcius with atmospheric pressure being "+pressure+" Pascals")        
    def provide_meaning(word):
        dictionary=PyDictionary()
        warnings.filterwarnings("ignore")
        print(dictionary.meaning(word))
        # print(dictionary.synonym(word))
        # print(dictionary.antonym(word))
        speak(dictionary.meaning(word))
        # speak(dictionary.translate(word,'es'))
    def read_bible(data,s,e):
        apiad='https://bible-api.com/'
        apiad=apiad+data
        json_data=requests.get(apiad).json()
        # print(json_data[])
        for i in range (s,e):
            print(json_data['verses'][i]['text'])
        for i in range (s,e):
            speak(json_data['verses'][i]['text'])
    def send_sms():
        acc_sid = 'ACd1d5d2e6d86a6f06e7bcd9319ede0b72'
        auth_token='7a8e3bd3ffc8a979cc2a0fcadeae4c5a'
        client = Client(acc_sid, auth_token)
        speak("What should I say?")
        content=takeCommand()
        client.messages.create(body=content,from_='+16308120993',to='+918839379117')
        speak('The message has been sent')
        # print(message.sid)
    def wish_other(query):
        string = query.split(' ')
        greet=''
        for i in range(len(string)):
            if string[i]=="is":
                for j in range (i+1,len(string)):
                    greet= greet+string[j]+" "
        speak(f'Hello {greet}. Pleasure to meet you')

    if __name__ == "__main__":
        wishMe()
        while True:
            query=takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching in wikipedia...')
                query=query.replace("wikipedia","")
                result= wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                speak(result)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'read image' in query:
                pytesseract.pytesseract.tesseract_cmd = r"G:\\Tesseract-OCR\\tesseract.exe"
                img=Image.open('hi2.jpg')    
                text=pytesseract.image_to_string(img,lang='eng')
                print(text)
                speak(text)
            elif 'he is' in query:
                wish_other(query)
            elif 'she is' in query:
                wish_other(query)
            elif 'Holy Bible' in query:
                print('checking')
                string=query.split(' ')
                word=''
                for i in range (len(string)):
                    if string[i]=="bible":
                        word=word+string[i+1].lower()+"+"+string[i+3]+":"+string[i+6]+"-"+string[i+8]
                        end=int(string[i+8])-int(string[i+6])
                print(word)
                speak(f"According to {string[i+1]} chapter {string[i+3]} verses from {string[i+6]} to {string[i+8]}")
                read_bible(word,0,end-1)   
            elif 'weather of' in query:
                string=query.split(' ')
                city=""
                for i in range (len(string)):
                    if string[i]=="of":
                        for j in range(i+1,len(string)):
                            city=city+string[j]+" "    
                        provide_weather_data(city)
            elif 'meaning of' in query:
                string=query.split(' ')
                for i in range (len(string)):
                    if string[i]=="of":
                        word=string[i+1]
                        provide_meaning(word)
            elif 'play music' in query:
                music_dir= 'F:\\MM'
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[2]))
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir, the time is {strTime}")
            
            elif 'email to me' in query:
                try:
                    speak("What should I say?")
                    content=takeCommand()
                    to="joel.singh78@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. the email was not sent.")
            elif 'send message' in query:
                send_sms()
            elif 'email to Ronald' in query:
                try:
                    speak("What should I say?")
                    content=takeCommand()
                    to="ronaldbrown9552@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. the email was not sent.")
            elif 'email to big brother' in query:
                try:
                    speak("What should I say?")
                    content=takeCommand()
                    to="singhjacob94@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. the email was not sent.")
            elif 'bye jarvis' in query:
                goodbye_wish()
                exit(0)
            # speak(query)

