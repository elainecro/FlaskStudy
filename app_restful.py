from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome':'Elaine',
     'habilidades': ['PHP','.Net Core','Python','C#','.Net','Azure','Flask']},
    {'nome':'Mychell',
     'habilidades': ['C#', '.Net', '.Net Core', 'Azure']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status":"erro", "mensagem":"Desenvolvedor de ID {} não existe.".format(id)} 
        except Exception:
            response = {"status":"erro", "mensagem":"Erro desconhecido. Procure o administrador da API."}       
        
        return jsonify(response)
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return id


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

api.add_resource(Desenvolvedor, "/dev/<int:id>")
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')

if __name__ == "__main__":
    app.run(debug=True)