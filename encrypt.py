import hashlib
import os
import time

#Quebrando hashs SHA-256
os.system("clear")
print("\033[0;32mＥｎｃｒｙｐｔ\033[m\n  Bʏ ʏHᴀᴘᴇʀ\n\n")
crypt = input("\033[0;32mDigite a palavra que deseja criptografar: \033[m")
os.system("clear")

crypt = hashlib.sha256('{}'.format(crypt).encode('utf8')).hexdigest()
print("\033[1;32mCriptografando /\033[m")
time.sleep(0.1)
os.system("clear")
print("\033[1;32mCriptografando -\033[m")
time.sleep(0.1)
os.system("clear")
print("\033[1;32mCriptografando \ \033[m")
time.sleep(0.1)
os.system("clear")
print("\033[1;32mCriptografando -\033[m")
time.sleep(0.1)
os.system("clear")
print ("\033[1;32mPronto:\033[m")
print (crypt)
