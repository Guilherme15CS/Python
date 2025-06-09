import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('Wamp')
pyautogui.press('enter')
sleep(30)
pyautogui.press('win')
pyautogui.write('MySQL')
pyautogui.press('enter')
sleep(10)
for i in range(3):
    pyautogui.press('tab')
    sleep(0.3)
pyautogui.press('enter')