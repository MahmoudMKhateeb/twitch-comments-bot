
import time
import pyautogui
import pyperclip
import clipboard
import random


tabLocations = [ [403 , 341] , [859 , 345] , [1390 , 345] ] #Browser Window Location (the area that we type the msg in)
normalmsgs = ["hello","hi","wooo","this is cool","!uptime" , "Cheer100 love your content <3" , "time" , "OMG" , "lol" , "thanks" , "Holy" , "The only thing you could not kill was your lack of creativity" , "Great !" , "How are you guys ?" , "what is this ?" , "nice one" , "GOAT" , "Niiiice" , "Pog" , "yo !" , "LAMO",":)", "<3"]
activeMessageList = normalmsgs
delay = 40
def sendMessage():
    time.sleep(delay)
    randomTab = random.choice(tabLocations)
    pyautogui.moveTo(randomTab[0], randomTab[1]) #move to this location 
    pyautogui.click(clicks=2 , interval=0.25) #double click
    pyautogui.click()
    msg = random.choice(activeMessageList)
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    return ("[*] message Sent -->" , msg)

i = 1
while True:
    print("[*] Working on loop --> ",i)
    print("[*] Waiting for the Delay " , delay)
    print(sendMessage())
    i += 1
