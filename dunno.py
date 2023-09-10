import time
import pyautogui
import random

time.sleep(2)

# pyautogui.displayMousePosition()
# 669, 529
def doStuff():
    EnterCall = pyautogui.locateOnScreen("Open.png", grayscale=True, region=(624, 248, 1045, 606), confidence=0.8)
    if(EnterCall == None): return
    
    Disconnect = (290, 640)
    pyautogui.click(pyautogui.center(EnterCall))
    time.sleep(.5)

    SoundPlayer = pyautogui.locateOnScreen("sound.png", grayscale=True, region=(76, 665, 307, 706), confidence=0.8)
    if(SoundPlayer == None):
        pyautogui.click(Disconnect)
        return

    SoundPlayer = pyautogui.center(SoundPlayer)
    pyautogui.click(SoundPlayer)

    Detector = pyautogui.locateOnScreen("detector.png", grayscale=True, region=(306, 305, 771, 649))

    count = 20
    pyautogui.moveTo(x=450, y=400)
    while Detector == None and count > 0:
        pyautogui.scroll(-100)
        time.sleep(0.1)
        Detector = pyautogui.locateOnScreen("detector.png", grayscale=True, region=(306, 305, 771, 649), confidence=0.8)
        count -= 1
    if(count <= 0): return

    Detector = pyautogui.center(Detector)

    # Sounds
    Cricket = (Detector[0], Detector[1] - 40)
    Sad = (Detector[0] - 155, Detector[1])
    Clap = (Detector[0] - 312, Detector[1])
    airhorn = (Sad[0], Cricket[1])
    quack = (Clap[0], Cricket[1])

    array = [
        Detector,
        Cricket,
        Sad,
        Clap,
        airhorn,
        quack
    ]

    for i in range(0, 20):
        pyautogui.click(random.choice(array))

    pyautogui.click(SoundPlayer)
    pyautogui.click(Disconnect)

doStuff()