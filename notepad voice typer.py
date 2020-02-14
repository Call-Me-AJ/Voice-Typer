import os
import speech_recognition as sr
a=sr.Recognizer()
from pyautogui import typewrite,press,hotkey
import time
with sr.Microphone() as speech:
    def reg():
        while True:
            try:
                spoke=a.listen(speech)
                text=a.recognize_google(spoke)
                return text
                break
            except:
                continue
    os.startfile(r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk")
    while True:
        text=reg()
        if text!="close" or text!="close":
            typewrite(text)
            press('space')
        else:
            hotkey('alt','f4')
            press('right')
            press('enter')
            break
