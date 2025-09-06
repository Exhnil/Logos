from config import PROJECT_NAME, VERSION
import logging
from utils.logging_config import setup_logging
from stt.recognizer import listen
from parser.parser import ParserPipeline
from executor.commands import Executor

setup_logging("logos.log", logging.DEBUG)
parser = ParserPipeline("en")
executor = Executor()


def main():
    print(f"[{PROJECT_NAME} v{VERSION}] Online")
    print("Awaiting istructions...")
    try:
        text = listen()
        command = parser.parse(text)
        print(command)
        executor.execute(command)

    except KeyboardInterrupt:
        print("\nLogos was interrupted")
        exit(0)


if __name__ == "__main__":
    main()
