import pyautogui
import time
import pyperclip
from tkinter import *
from tkinter import messagebox as MessageBox

def isPrime(num):
    if num < 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

if __name__ == '__main__':
    time.sleep(3)
    opciones = pyautogui.prompt(' [0] Meter cosas randoms\n [1] Meter textos')
    opciones = int(opciones)
    time.sleep(0.5)
    i = 1

    if opciones == 1:
        eleccion = pyautogui.prompt(' [0] Bee movie\n [1] Mistborn\n [2] Shrek\n [3] Somebody\n [4] Miku\n [5] Kaladin siendo un dios')
        eleccion = int(eleccion)
        time.sleep(2.5)

        if eleccion == 0:
            f = open("bee.txt", 'r')
        if eleccion == 1:
            f = open("mistborn.txt", 'r')
        if eleccion == 2:
            f = open("shrek.txt", 'r')
        if eleccion == 3:
            f = open("somebody.txt", 'r')
        if eleccion == 4:
            f = open("miku.txt", 'r')
        if eleccion == 5:
            f = open("honor.txt", 'r')
        for word in f:
            if f != "" or f != " ":
                pyautogui.typewrite(word)

    elif opciones == 0:
        eleccion = pyautogui.prompt(' [0] Contar\n [1] Espacios\n [2] Intos \n [3] Numeros primos\n [4] Donut\n [5] Putx')
        eleccion = int(eleccion)
        time.sleep(2.5)
        if eleccion == 0:
            while i != 10000:
                I = str(i)
                pyautogui.typewrite(I)
                pyautogui.press('enter')
                i = i + 1

        if eleccion == 1:
            while i != 100000:
                pyautogui.press('space')
                i = i + 1

        if eleccion == 2:
            while i != 10000:
                pyautogui.press('enter')
                i = i + 1

        if eleccion == 3:
            a = 1
            while a != 1000000000:
                a = a + 1
                if isPrime(a) is True:
                    A = str(a)
                    pyautogui.typewrite(A)
                    pyautogui.press('enter')

        if eleccion == 4:
            while i != 100000000:
                pyautogui.write('.')
                f = open("donut.txt", 'r')
                for word in f:
                    pyautogui.write(".")
                    pyperclip.copy(word)
                    pyautogui.hotkey('ctrl', 'v', interval=0.001)
                    pyautogui.press('enter')

        if eleccion == 5:
            puto = 3
            while puto <= 1000000:
                pyautogui.press('n')
                pyautogui.write("F")
                pyautogui.hotkey('ctrl', 'Enter', interval=.1)
