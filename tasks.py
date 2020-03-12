from flask import Flask, request, jsonify
from json

app = Flask(__name__)

tasks = [
    {'id':'1',
     'responsavel':'Elaine',
     'tarefa':'Declarar Imposto de Renda',
     'status':'Pendente'},
    {'id':'2',
     'responsavel':'Elaine',
     'tarefa':'Fazer almoço',
     'status':'Em Andamento'}
]

# API para gerenciar o cadastro de tarefas
# API terá uma lista de tarefas que deverá ter os seguintes campos: id, responsável, tarefa e status
# Permitir listar todas as tarefas e também incluir novas tarefas
# API deve permitir consultar uma tarefa através do ID, alterar o status de uma tarefa e também excluir uma tarefa
# Nenhuma outra alteração deverá ser permitida além do status da tarefa
@app.route("/tarefas", methods=[''])