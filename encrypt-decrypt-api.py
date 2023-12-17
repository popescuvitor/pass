from cryptography.fernet import Fernet
import cryptography
from flask import Flask, request, jsonify, Response
import base64

app = Flask(__name__)


@app.route('/hash', methods=["GET"])
def hash():
	keykey = Fernet.generate_key()
	return keykey.decode(), 200 

@app.route('/encryption', methods=["POST"])

def encryption():
 
    file = request.files.get('file')

    print("Método HTTP:", request.method)
    print("Headers:", request.headers)
    print("Parâmetros da solicitação:", request.args)
    print("Campos do formulário:", request.form)
        
    base64_data = base64.b64encode(file.read()).decode("utf-8")
    inhash = request.headers.get('inhash')
    if inhash is None:
    	return "Cabeçalho 'inhash' ausente na solicitação", 400
    fernet = Fernet(inhash)
    encMessage = fernet.encrypt(base64_data.encode())
    return encMessage, 200

@app.route('/decryption', methods=["POST"])
def decryption():
    inhash = request.headers.get('inhash')
    if inhash is None:
    	return "Cabeçalho 'inhash' ausente na solicitação", 400  
    file = request.files.get('file')
    encMessage = file.read()
    fernet = Fernet(inhash)
    try:
        decMessage = fernet.decrypt(encMessage).decode()
    except (cryptography.fernet.InvalidToken, TypeError):
    	return "hash invalida para o arquivo", 403 
    answer = base64.b64decode(decMessage.encode())
 
    return answer, 200
  

app.run(host="192.168.0.35", port=6500)