import pyautogui as pag
from time import sleep 
import keyboard
import colorama
from colorama import init, Fore
colorama.init()

print(Fore.GREEN)
print(
    """
               ████████████████████████████████████████████████████████████████
               █▄▄▄░█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄▀█▄─▄█▄─▀█▄─▄██▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█
               ███░██─███▀█─██─██─▄─▄██─██─██─███─█▄▀─███─▀─████─███─██─██─▄─▄█
               ▀▀▄██▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀
    """
)

print(Fore.RED)

def screencord():
    cord = pag.position()
    print('=============')
    print(cord)
    print('')

def marker():
    print('')
    print('xXxXx')
    print('')

keyboard.add_hotkey('insert', screencord)
keyboard.add_hotkey('home', marker)
nickname = input('> ')