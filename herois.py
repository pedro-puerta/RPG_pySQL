from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import false


engine = create_engine('sqlite:///rpg.db')


'''
    Essa classe só representa uma exception com novo nome. Não mexa dentro dela.
    Escreva os imports (acima dela)
    E suas funcoes (depois dela)
'''


class HeroiNaoExisteException(Exception):
    pass


# --------------- Funções --------------- #


def heroi_existe(id_h):
    with engine.connect() as con:
        query = "SELECT * FROM Heroi WHERE id = :heroi"
        linhas = con.execute(query, heroi = id_h)
        primeiro = linhas.fetchone()
        if primeiro == None:
            return False
        return True


def consultar_heroi(id_h):
    with engine.connect() as con:
        query = "SELECT * FROM Heroi WHERE id = :heroi"
        linhas = con.execute(query, heroi = id_h)
        primeiro = linhas.fetchone()
        if primeiro == None:
            raise HeroiNaoExisteException
        return dict(primeiro)


def consultar_heroi_por_nome(nome_h):
    with engine.connect() as con:
        query = "SELECT * FROM Heroi WHERE nome = :heroi"
        linhas = con.execute(query, heroi = nome_h)
        primeiro = linhas.fetchone()
        if primeiro == None:
            raise HeroiNaoExisteException
        return dict(primeiro)


def ultimo_heroi():
    with engine.connect() as con:
        query = "SELECT id FROM Heroi ORDER BY id"
        linhas = con.execute(query)
        linha = linhas.fetchone()
        ultimo = int()
        while linha != None:
            ultimo = int(linha[0])
            linha = linhas.fetchone()
        return ultimo


def criando_heroi(atributos):
    with engine.connect() as con:
        query = "INSERT INTO Heroi VALUES (:id, :nome, :fisico, :magia, :agilidade)"
        linhas = con.execute(query, id = ultimo_heroi() + 1, nome = atributos['nome'], fisico = atributos['fisico'], magia = atributos['magia'], agilidade = atributos['agilidade'])

