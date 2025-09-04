from config import PROJECT_NAME, VERSION
from stt.recognizer import listen,listenWhisper
from nlp.parser import parse
from executor.commands import execute

def main():
    print(f"[{PROJECT_NAME} v{VERSION}] Online")
    print("Awaiting istructions...")
    try:
        #while True:
            listenWhisper()
            '''
            text=listen()
            print(f"You said: {text}")
            if text and text.lower() == "exit":
                print("Logos shutting down...")
                break
            command = parse(text)
            print(command)
            execute(command)
            '''
           
    
    except KeyboardInterrupt:
        print("\nLogos was interrupted")
        exit(0)
    

if __name__ == "__main__":
    main()