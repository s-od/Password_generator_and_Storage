from os import system, name
from pathlib import Path
import time, os

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

