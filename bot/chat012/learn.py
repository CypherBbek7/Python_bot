
from chat012.chat import chat_conversation as chat
def learn(data):

    if "day" in data:
        chat.day()

    elif "news" in data:
        chat.news()

    elif "time" in data:
        chat.current_time()

    elif "temperature" in data:
        chat.temperature()

    elif "greeting" in data:
        chat.greeting()

    elif "close" in data:
        chat.close()
        
    elif "country" in data:
        chat.country()
    
    elif "places" in data:
        chat.places()
    
    elif "color" in data:
        chat.color()
    
    elif "continent" in data:
        chat.continent()
    
    elif "planet" in data:
        chat.planet()
        
    elif "footballer" in data:
        chat.footballer()
        
    elif "youtuber" in data:
        chat.youtuber()
        
                
    elif "cricketer" in data:
        chat.cricketer()
        
    elif "team" in data:
        chat.team()
    

    elif "exit" in data:
        chat.Exit()

    else:
        print(" Sorry,I don't know the answer")   
