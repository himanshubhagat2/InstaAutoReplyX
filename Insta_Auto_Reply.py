import os
import webbrowser
import time
from time import sleep
import pyautogui as pt
import pyperclip as at

n=time.time()
os.system('cls')

username=("somewherefar")
password=("himanshu@12345")

os.system('cls')
#print("Attempting to login!")
sleep(.3)
a=1
webbrowser.open ('https://www.instagram.com/accounts/login/')
sleep(6)


def login():
    position3=pt.locateOnScreen('IG_loginusername.png',confidence=.6)
    pt.click(position3)
    pt.typewrite(username)
    sleep(.2)
    position4=pt.locateOnScreen('IG_loginpassword.png',confidence=.6)
    pt.click(position4)
    pt.typewrite(password)
    pt.press('enter')
    sleep(8.5)
    position5=pt.locateOnScreen("IG_notsavelogindetail.png",confidence=.5)
    pt.click(position5)


def openIGMSG():
    webbrowser.open("https://www.instagram.com/direct/inbox/")
    sleep(6)   


def move_to_new_msg():
    position=pt.locateOnScreen('IG_newmsg.png', confidence=.7)
    if position is None:
        pass
    elif position is not None:
        pt.click(position)
        sleep(.2)
        position2=pt.locateOnScreen('IG_keyboard.png', confidence=.7)
        pt.click(position2)
        pt.typewrite("Hey!\n I am currently AFK. Because I am busy. Last seen " + str(x) + " seconds ago. I will try to reply as soon as possible.🤘✌✌")
        pt.press('enter')
        #print("Message sent!")
    else:
        #print("No new message found!")
        pass


try:
    login()
except:
    pass  
openIGMSG()
position=pt.locateOnScreen('IG_newmsg.png', confidence=.7)
print(position)


while True:
    y=time.time()
    x=y-n
    move_to_new_msg()


    








