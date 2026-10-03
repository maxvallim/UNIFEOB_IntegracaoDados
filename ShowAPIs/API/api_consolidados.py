from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient(
    "mongodb+srv://maxvallim:max123456@cluster0.tc1z19w.mongodb.net/"
)

db = mongo["integracao_dados"]

colecao = db["cliente_consolidado"]

@app.route('/consolidados')
def consolidados():

    lista = []

    for doc in colecao.find():

        doc["_id"] = str(doc["_id"])

        lista.append(doc)

    return jsonify(lista)

if __name__ == '__main__':
    app.run(port=5005, debug=True)