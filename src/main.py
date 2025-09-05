from config import PROJECT_NAME, VERSION
import logging
from utils.logging_config import setup_logging
from stt.recognizer import listen
from nlp.parser import parse
from executor.commands import execute

setup_logging("logos.log", logging.DEBUG)

def main():
    print(f"[{PROJECT_NAME} v{VERSION}] Online")
    print("Awaiting istructions...")
    try:
        # while True:
        text = listen()
        """
            print(f"You said: {text}")
            if text and text.lower() == "exit":
                print("Logos shutting down...")
                break
            command = parse(text)
            print(command)
            execute(command)
            """

    except KeyboardInterrupt:
        print("\nLogos was interrupted")
        exit(0)


if __name__ == "__main__":
    main()
