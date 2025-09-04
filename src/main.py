from config import PROJECT_NAME, VERSION
from stt.recognizer import listen

def main():
    print(f"{PROJECT_NAME} booting...")
    print(f"[{PROJECT_NAME} v{VERSION}] Online")
    print("Awaiting istructions...")
    while True:
        listen()

if __name__ == "__main__":
    main()