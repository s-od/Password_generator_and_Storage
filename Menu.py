from os import system, name
from pathlib import Path
from other_def import clear
import time, os
import other_def, password_gen, password_storage, setup

while True:
    clear()
    print('Password Generator & Storer')
    print('Made By Poggers1337')
    for _ in range(3):
        print()
    time.sleep(.25)
    print('0. Exit')
    time.sleep(.25)
    print('1. Password Generator')
    time.sleep(.25)
    print('2. Password Storage')

    v = int(input('Choose option: '))
    if v == 0:
        clear()
        exit()
    elif v == 1:
        clear()
        b = int(input('Enter in password length: '))
        password_gen.password_gen(b)
        time.sleep(1)

