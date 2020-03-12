from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Elaine',
     'habilidades': ['PHP','.Net Core','Python','C#','.Net','Azure','Flask']},
    {'nome':'Mychell',
     'habilidades': ['C#', '.Net', '.Net Core', 'Azure']}
]


@app.route("/dev/<int:id>", methods=['GET','PUT','DELETE'])
def desenvolvedorPorId(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status":"erro", "mensagem":"Desenvolvedor de ID {} não existe.".format(id)} 
        except Exception:
            response = {"status":"erro", "mensagem":"Erro desconhecido. Procure o administrador da API."}       
        
        return jsonify(response)
        
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status":"sucesso", "mensagem":"Registro excluído!"})


@app.route("/dev", methods=['POST', 'GET'])
def listaDesenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)