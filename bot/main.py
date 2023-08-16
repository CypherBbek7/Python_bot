from chat012.chat import chat_conversation
from chat012.learn import learn 

def main():
    chat_conversation.greeting()
    while True:
        data = input(f'Bibek:')
        learn(data)
    

if __name__ == "__main__":
    main()