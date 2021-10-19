from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

#criar a tabela
with engine.connect() as con:    
    create_sql = """
    CREATE TABLE IF NOT EXISTS Jogador (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """    
    rs = con.execute(create_sql)

def inicializar_tabela():
    criar_jogador(nome="lucas goncalves", email="lucas.goncalves@faculdadeimpacta.com.br")
    criar_jogador(email="victor.silva@faculdadeimpacta.com.br",nome="victor")
    criar_jogador(email="email_do_jadir",nome="jadir")

def criar_jogador(nome,email):
    with engine.connect() as con:    
        sql_criar = "INSERT INTO Jogador (nome,email) VALUES (:nome,:email)"
        con.execute(sql_criar, nome=nome, email=email)

        # Repare que a minha query nao especificou uma coluna: a ID do usuário
        # o sqlite está preenchendo essa coluna sozinho (como podemos ver na criacao da tabela)
        
    

from jogadores_consultas import consultar_jogador
def alterar_jogador(id_j,novos_dados):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o usuario realmente existe
    #se nao existir, o localizar faz o exception pra mim
    #e aborta a execução da funcao
    consultar_jogador(id_j)
    with engine.connect() as con:    
        sql_editar = "UPDATE Jogador SET nome=:nome, email=:email WHERE id = :id"
        con.execute(sql_editar, nome=novos_dados['nome'], 
                    email=novos_dados['email'], id = id_j)


def remover_jogador(id_j):
    with engine.connect() as con:    
        sql = "DELETE FROM Jogador WHERE id = :id_j"
        con.execute(sql, id_j=id_j)
    




'''
Sobre a arquitetura:
    a arquitetura desses arquivos jogador está sem sentido
    
    ninguém separaria a parte dos selects da parte das alteraçoes.

    normalmente se coloca todos os acessos de banco da mesma entidade
    num mesmo arquivo, usando uma classe (padrao de projeto DAO)

    Por motivos didaticos, nao fizemos isso aqui
'''
