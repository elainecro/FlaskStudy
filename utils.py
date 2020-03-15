from models import Pessoas

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

if __name__ == "__main__":
    #insere_pessoas()    
    #altera_pessoa()
    #excluir_pessoa()
    consulta_pessoa()