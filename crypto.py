from cryptography.fernet import Fernet
from getpass import getpass
import os
import time
import cryptography
import pyperclip
keykey = Fernet.generate_key()
print(keykey.decode())

message = getpass()

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()
fkey = Fernet(keykey)
# Instance the Fernet class with the key
 
fernet = Fernet(key)
 
# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())

print(fkey.encrypt(key))
print("encrypted string: ", encMessage)

k = True
while True:
    encMessage = input("-> ")
    encMessage = encMessage.replace("()","_")
    if encMessage == "0":
        print("END!")
        break
    encMessage = encMessage.encode()
    try:
        decMessage = fernet.decrypt(encMessage).decode()
    except (cryptography.fernet.InvalidToken, TypeError):
        print("invalido")
        continue
    if k == True:
        print(decMessage)
        time.sleep(3)
        os.system('clear')
        k = False
    else:
        pyperclip.copy(decMessage) 
        print("Copiado!")
        time.sleep(10)
        pyperclip.copy('')
        os.system('xsel -bc')
        os.system('xclip -sel clip < /dev/null')
        os.system('clear')


