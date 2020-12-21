#/usr/bin/python3

import re
from pyowm import OWM
import wikipedia
from random import choice
import datetime

greetings_response = ['Hello', 'Hi', 'Hey']
response = {
        "/who are you" : "I'm Kōdingu, a ChatBot, created by Tarun Gupta ( @tarung10 ).",
        "/who made you" : "Tarun Gupta ( @tarung10 )",
        "/who created you" : "Tarun Gupta ( @tarung10 )",
        "/who is your father" : "Tarun Gupta ( @tarung10 )",
        "year" : datetime.datetime.now().year - 2020,
        "month" : datetime.datetime.now().month - 5,
        "day" : datetime.datetime.now().day - 15,
        "/how was your day" : "It was amazing.",
        "/what are you doing" : "Talking to you",
        "/do you believe in ghost" : "No",
        "/i like you" : "I like You too",
        "/i like you kodingu" : "I like You too",
        "/do you like me" : "I like you too",
        "/are you my friend" : "Yes always",
        "/bye" : "Bye."
    }
help = ['/How old are you', '/who created you','/who are you','/do you believe in ghost','/commands', '/current weather in CITY', '/wikipedia TOPIC', '/search TOPIC']

def kodingu(self, command, user):
    if '/search' in command:
        reg_ex = re.search('search (.*)', command)

        try:
            if reg_ex:
                topic = reg_ex.group(1)

                #New tab opens
                self.driver.execute_script("window.open('');")
                self.driver.switch_to.window(self.driver.window_handles[1])

                #new URL opens
                self.driver.get("https://www.google.com/?q=" + str(topic))
                self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
                self.driver.implicitly_wait(5)

                #selecting appropriate link
                link = self.driver.find_elements_by_tag_name('a')[50].get_attribute("href")

                #closing new tab
                self.driver.close()

                #coming back to original tab
                self.driver.switch_to.window(self.driver.window_handles[0])

                return link

        except:
            return "Something went wrong"


    elif '/wikipedia' in command:
        reg_ex = re.search('wikipedia (.*)', command)

        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)

            return str(ny.content[:200].encode('utf-8'))

        except:
            return "Invalid synatx. Try '/search TOPIC'"


    if '/help' in command:
        return "Try '" + choice(help) + "'"
     
        
    elif '/commands' in command:
        return "Visit: https://tarung10.github.io/2020/05/14/instabot.html"


    elif 'sex' in command or 'fuck' in command or 'motherfuck' in command:
        return "Don't use such language."


    elif command == '/what is your age' or command == '/how old are you':
        return "It's " + str(response['year']) + " year " + str(response['month']) + " months " + str(response['day']) + " days."


    elif '/current weather' in command:
        reg_ex = re.search('/current weather in (.*)', command)

        try:
            city = reg_ex.group(1)
            owm = OWM(API_key='760349efe7241a63512a89e9a242f1ac')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')

            return "Current weater in " + city + " is " + k + ". The max temp is " + str(x['temp_max']) + " and the min temp is " + str(x['temp_min']) + " degree celsius."

        except:
            return "Invalid syntax. '/Current weather in CITY'"


    elif 'hey' in command or 'hi' in command or 'hello' in command or 'morning' in command or 'afternoon' in command or 'evening' in command or 'night' in command:
        hour = datetime.datetime.now().hour

        if hour < 12:
            greeting = "Morning."

        elif 12 <= hour < 16:
            greeting = "Afternoon."

        elif hour >= 16:
            greeting = "Evening."


        return choice(greetings_response) + " @" + user + ". Good " + greeting


    else:
        try:
            ans = response[command]
            return ans
        
        except:
            return None
