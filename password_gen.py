from os import system, name
from other_def import clear
from pathlib import Path
import time, os, random, string, time


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



def password_gen(length=8):
    try:
        f = open(ali + '/password_cache.txt','x')
    except FileExistsError:
        f = open(ali + '/password_cache.txt','w')
    for _ in range(length):
        isan = random.randint(1,2)
        if isan == 1:
            a_raw = random.randint(0,9)
            a = str(a_raw)
            f.write(a)
        elif isan == 2:
            a = random.choice(string.ascii_letters)
            f.write(a)
    print(f.readlines())
    f.close()
    




