import os
import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone={----a number---}')

sleep(10)
LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))
SONG_PATH = os.path.join(LOCAL_PATH, 'song.txt')
with open(SONG_PATH, 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
