from os import system, name
from pathlib import Path
import time, os, cryptography, time
from cryptography import fernet
from cryptography.fernet import Fernet

#######################################################
if os.name == 'nt':                                   #
    dp = str(Path.home() / "Downloads")               #
else:                                                 #
    dp = str(os.path.join(Path.home(), "Downloads"))  #
cf = dp + '/Pass-gen-core'                            #
imf = cf + '/Password-Output'                         #
ali = cf + '/Pass-and_usr_store'                      #
vocf = cf + '/var.txt'                                #
voimf = imf + '/var.txt'                              #
voali = ali + '/var.txt'                              #
#######################################################

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def encryption_key():
    key = Fernet.generate_key()
    with open(ali + "/secret.key", "wb") as key_file:
        key_file.write(key)

def load_key(location):
    print('Loosing this key will result in you not being able to view your passwords')
    return open(location, "rb").read()


def encrypt(username, password_needin_encryption, key_location):
    try:
        e = open(ali + '/passwords_usernames.txt', 'x')
    except FileExistsError:
        e = open(ali + '/passwords_usernames.txt', 'r')
    

    key = load_key
    print(f'Loaded key: {key}')
    time.sleep(.5)
    encoded_message = password_needin_encryption.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    e.writelines(username+'|'+encrypted_message)
    print(username+' | '+encrypted_message)
    

    

