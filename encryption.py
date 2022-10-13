import hashlib
import os
import time

os.system("clear")
print("\033[0;32mＥｎｃｒｙｐｔｉｏｎ\033[m\n  Bʏ ʏHᴀᴘᴇʀ\n\n")
crypt = input("\033[0;32mEnter the word you want to encrypt: \033[m")
os.system("clear")

crypt = hashlib.sha256('{}'.format(crypt).encode('utf8')).hexdigest()
print("\033[1;32mencrypting /\033[m")
time.sleep(0.1)
os.system("clear")

print("\033[1;32mencrypting -\033[m")
time.sleep(0.1)
os.system("clear")

print("\033[1;32mencrypting \ \033[m")
time.sleep(0.1)
os.system("clear")

print("\033[1;32mencrypting -\033[m")
time.sleep(0.1)
os.system("clear")

print ("\033[1;32mdone:\033[m")
print (crypt)
