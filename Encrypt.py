import hashlib
import os
import time

#Quebrando hashs SHA-256
os.system("clear")
crypt = input("\033[0;32mDigite a palavra que deseja cripgrafar: \033[m")
os.system("clear")

crypt = hashlib.sha256('{}'.format(crypt).encode('utf8')).hexdigest()
print ("\033[1;32mPronto:\033[m")
print (crypt)
