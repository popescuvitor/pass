from flask import Flask, request, jsonify, Response
from cryptography.fernet import Fernet
from getpass import getpass
import pyperclip
import os
import time

keykey = getpass("<-")
keykey = keykey.encode()
fkey = Fernet(keykey)


app = Flask(__name__)

# Endpoint to create a new guide
@app.route('/pass', methods=["POST"])
def password():
    key = request.json['key']
    key = fkey.decrypt(key.encode())
    fernet = Fernet(key)
    hashs = request.json['hash']
    hashs = hashs.encode()
    try:
        decMessage = fernet.decrypt(hashs).decode()
    except (cryptography.fernet.InvalidToken, TypeError):
        print("invalido")
        return Response(response="hash ou key invalido", status=500)
    pyperclip.copy(decMessage)
    print("Copiado!")
    time.sleep(3)
    pyperclip.copy('')
    os.system('xsel -bc')
    os.system('xclip -sel clip < /dev/null')    
    return Response(response="sucesso!", status=200)
app.run(host="127.0.0.1", port=8080)

v