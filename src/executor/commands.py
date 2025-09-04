import os
import subprocess

def execute(command):
    action = command.get("action")
    target= command.get("target")
    if action == "open_browser" and target == "browser":
        print("Executing: Open Browser")
        # Code to open the browser would go here   
    elif action == "open_spotify" and target == "spotify":
        print("Executing: Open Spotify")
        print(apps["spotify"])
        os.startfile(apps["spotify"])
    else:
        print("Unknown command. Cannot execute.")

apps = {
    "spotify":"spotify",
    "browser":"chrome"
}