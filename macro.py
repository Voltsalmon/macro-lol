# This macro was made by Voltsalmon:

# My youtube: https://www.youtube.com/@Voltsalmon_
# My Discord: asalmon
# My Github

# Instructions for using this macro:
# 
# If you are using a windows:
# 1.) Download Python3 through the microsoft store (make sure u get 3 (i think))
# 2.) In microsoft powershell, type in pip install pyautogui (a library required to run the script)
# 3.) Run the command in powershell: "cd C:\Users\YourName\Downloads" (or wherever your macro file is located)
# 4.) In powershell, run python3 macro.py
#
# If you are using a mac (and i think linux):
# 1.) First go to terminal
# 2.) In terminal, type in: curl -O https://www.python.org/ftp/python/3.10.7/python-3.10.7-macos11.pkg
# 3.) In terminal, type in: pip install pyautogui
# 4.) In terminal, type in: cd ~/Downloads (if you kept in a folder or somewhere else you can do something like this: cd ~/Desktop/pycode: This goes to my PyCode Folder in my desktop)
# 5.) In terminal, type in: python3 macro.py

# IMPORTANT INFORMATION:
# MAKE SURE THAT YOU ALLOW THIS FILE TO USE ADMIN/SCREEN CONTROL/ KEYBOARD CONTROL OR SMTH!
# THIS IS NOT A VIRUS FILE OK (source: trust me bro)

import pyautogui
import time
import random

timer = 5

print(f"You have {timer} seconds to focus your window (editor, terminal, etc.)")
time.sleep(timer) #This number determines how many seconds the macro will activate after running it (you can change it)

# Text to type
messages = [ #This is the list of messgaes (You can change it too, but make sure that you add speech marks for each word and a comma after the word)
    "nice",
    "hi",
    "cool",
    "bye",
    "this is a test",
    "wow",
    "crazy"
]



while True:
    message = messages[random.randint(1, len(messages)-1)]
    pyautogui.typewrite(message)  # This types the message
    pyautogui.press("enter")      # This presses enter

    