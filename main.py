import pyautogui
import time

pyautogui.alert("     [0] NUmeros\n     [1] Bee movie punto txt\n     [2] Mistborn\n     [3] Somebody once told me\n     [4] Enter a secas \n     [5] Espacios")
time.sleep(0.5)

eleccion = pyautogui.prompt('Elige una perro')
eleccion = int(eleccion)

i = 1

time.sleep(5)
if eleccion == 0:
    while i != 10000:
        I = str(i)
        pyautogui.typewrite(I)
        pyautogui.press('enter')
        i = i + 1
if eleccion == 1:
    f = open("bee.txt", 'r')
if eleccion == 2:
    f = open("mistborn.txt", 'r')
if eleccion == 3:
    f = open("somebody.txt", 'r')
if eleccion == 4:
    while i != 10000:
        pyautogui.press('enter')
        i = i + 1
if eleccion == 5:
    while i != 10000:
        pyautogui.press('space')
        i = i + 1
for word in f:
    pyautogui.typewrite(word)
