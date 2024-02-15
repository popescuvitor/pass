from cryptography.fernet import Fernet
from getpass import getpass
import os
import time
import cryptography
import json
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

#print(fkey.encrypt(key))
#print("encrypted string: ", encMessage)
with open('pass.json', 'r') as update:
    json_string = update.read()

json_obj = json.loads(json_string)

json_obj['key'] = fkey.encrypt(key).decode()
json_obj['hash'] = encMessage.decode()

json_string_atualizado = json.dumps(json_obj, indent=4)

with open('pass.json', 'w') as arquivo:
    arquivo.write(json_string_atualizado)

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



