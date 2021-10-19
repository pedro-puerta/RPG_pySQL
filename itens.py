from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import false


engine = create_engine('sqlite:///rpg.db')


class ItemNaoExisteException(Exception):
    pass


# --------------- Funções --------------- #


def consultar_item(id_i):
    with engine.connect() as con:
        query = "SELECT * FROM Item WHERE id = :item"
        linhas = con.execute(query, item = id_i)
        primeiro = linhas.fetchone()
        if primeiro == None:
            raise ItemNaoExisteException
        return dict(primeiro)


def nome_para_id_item(nome_i):
    with engine.connect() as con:
        query = "SELECT id FROM Item WHERE nome = :nome"
        linhas = con.execute(query, nome = nome_i)
        id_item = linhas.fetchone()
        if id_item == None:
            raise ItemNaoExisteException
        else:
            return id_item[0]


def ultimo_item():
    with engine.connect() as con:
        query = "SELECT id FROM Item ORDER BY id"
        linhas = con.execute(query)
        linha = linhas.fetchone()
        ultimo = int()
        while linha != None:
            ultimo = int(linha[0])
            linha = linhas.fetchone()
        return ultimo


def criando_item(atributos):
    with engine.connect() as con:
        query = "INSERT INTO Item VALUES (:id, :nome, :tipo, :fisico, :magia, :agilidade, 0)"
        linhas = con.execute(query, id = ultimo_item() + 1, tipo = atributos['tipo'], nome = atributos['nome'], fisico = atributos['fisico'], magia = atributos['magia'], agilidade = atributos['agilidade'])


def criar_item(tipo, nome, fisico, agilidade, magia):
    dic = dict()
    dic['tipo'] = tipo
    dic['nome'] = nome
    dic['agilidade'] = agilidade
    dic['fisico'] = fisico
    dic['magia'] = magia
    criando_item(dic)
