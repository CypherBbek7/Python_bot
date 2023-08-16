from datetime import *
import random
import chat012.information as c

now = datetime.now()

class chat_conversation:
    def greeting():
        hour = int(now.hour)
        if hour>=0 and hour<12:
            print("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
        else:
            print("Good evening!")

        print(random.choice(c.greeting))

    def day():
        days = now.strftime("%A, %B %d")
        print(f"Today is {days}")

    def current_time():
        current_time= now.strftime("%I:%M:%p")
        print(f"Time is {current_time}")
        
    def Exit():
        print(random.choice(c.close))
        exit()

    def temperature():
        print(random.choice(c.temperature))
        
    def news():
        print(random.choice(c.news))

    def country():
        print(random.choice(c.country))

    def places():
        print(random.choice(c.places))
        
    def color():
        print(random.choice(c.color))
        
    def continent():
        print(random.choice(c.continent))
        
    def planet():
        print(random.choice(c.planet))
        
    def cricketer():
        print(random.choice(c.cricketer))
        
    def footballer():
        print(random.choice(c.footballer))
        
    def youtuber():
        print(random.choice(c.youtuber))
        
    def team():
        print(random.choice(c.team))
     