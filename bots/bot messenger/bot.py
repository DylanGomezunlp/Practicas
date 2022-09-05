from datetime import datetime
import pyautogui, webbrowser
from time import sleep

def send(id):
    pyautogui.typewrite('sample text')
    sleep(10)
    webbrowser.open(f'https://www.messenger.com/t/{id}')
    pyautogui.press('enter')
    return flag

flag = 1

id = '----'

while flag:
    time = datetime.now().strftime('%I:%M')
    if time == '11:00':
        flag = send(id)
