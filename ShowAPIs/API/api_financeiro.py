from flask import Flask, jsonify
import firebase_admin

from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    "bancofinanceiro-b0bc5-firebase-adminsdk-fbsvc-6ff543f4fe.json"
)

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL":
        "https://bancofinanceiro-b0bc5-default-rtdb.firebaseio.com/"
    }
)

app = Flask(__name__)

@app.route('/financeiro/<codigo>')
def financeiro(codigo):

    ref = db.reference("/")

    dados = ref.child(codigo).get()

    if not dados:
        return jsonify(
            {"erro": "Cliente não encontrado"}
        ), 404

    return jsonify(dados)

if __name__ == '__main__':
    app.run(port=5003, debug=True)