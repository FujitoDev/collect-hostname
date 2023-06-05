import pyautogui as pag
import time

pag.PAUSE = 0.22
pag.hotkey("win", "r")
pag.write("cmd")
pag.press("enter")
pag.write("hostname")
pag.press("enter")
pag.write("hostname | clip")
pag.press("enter")
pag.hotkey("alt", "F4")