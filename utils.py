from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Vanessa', idade=38)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    #pessoa = Pessoas.query.all()
    #print(pessoa)
    pessoas = Pessoas.query.filter_by(nome='Elaine Cristina')
    for pessoa in pessoas:
        print(pessoa.nome)
        
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Elaine Cristina').first()
    pessoa.nome = 'Elaine Cristina'
    pessoa.save()
    
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Elaine Cristina').first()
    pessoa.delete()
    
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()
    
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == "__main__":
    #insere_pessoas()    
    #altera_pessoa()
    #excluir_pessoa()
    #consulta_pessoa()
    insere_usuario('edesio','2312')
    insere_usuario('maria','4321')
    consulta_todos_usuarios()