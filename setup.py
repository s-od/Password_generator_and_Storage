from os import system, name
from pathlib import Path
import time, os
from other_def import *

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



def cas(file):
    f = open(file,'x')
    f.write('########################          #\n')
    f.write('########################         # \n')
    f.write('## CHECKED AND STABLE ##    #   #  \n')
    f.write('########################     # #   \n')
    f.write('########################      #    \n')
    f.close()

def setup():
    #file storage
    try:
        f = open(vocf, 'r')
        f.close()
    except FileNotFoundError:
        os.mkdir(cf)
        cas(vocf)
    try:
        f = open(voimf, 'r')
        f.close()
    except FileNotFoundError:
        os.mkdir(imf)
        cas(voimf)
    try:
        f = open(voali, 'r')
        f.close()
    except FileNotFoundError:
        os.mkdir(ali)
        cas(voali)