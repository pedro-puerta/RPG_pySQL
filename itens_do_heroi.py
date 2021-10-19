from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import false


engine = create_engine('sqlite:///rpg.db')


class ItemNaoExisteException(Exception):
    pass


# --------------- Funções --------------- #


def heroi_tem_item(id_h):
    with engine.connect() as con:
        query = "SELECT * FROM ItemDoHeroi WHERE idHeroi = :heroi"
        linhas = con.execute(query, heroi = id_h)
        primeiro = linhas.fetchone()
        if primeiro == None:
            return False
        return True


def heroi_quantos_itens(id_h):
    with engine.connect() as con:
        query = "SELECT * FROM ItemDoHeroi WHERE idHeroi = :heroi"
        linhas = con.execute(query, heroi = id_h)
        qtdItens = 0
        while linhas.fetchone() != None:
            qtdItens += 1
        return qtdItens


def itens_do_heroi(id_h):
    with engine.connect() as con:
        query = "SELECT Item.tipo, Item.magia FROM Item INNER JOIN ItemDoHeroi ON Item.id = ItemDoHeroi.iditem and ItemDoHeroi.idheroi = :heroi"
        linhas = con.execute(query, heroi = id_h)
        itens = []
        linha = linhas.fetchone()
        while linha != None:
            itens.append(dict(linha))
            linha = linhas.fetchone()
        return itens


def itens_em_uso_do_heroi(idHeroi):
    with engine.connect() as con:
        query = "SELECT * FROM Item INNER JOIN ItemDoHeroi ON Item.id = ItemDoHeroi.iditem WHERE ItemDoHeroi.idheroi = :heroi and Item.emUso = 1"
        linhas = con.execute(query, heroi = idHeroi)
        itens = []
        linha = linhas.fetchone()
        while linha != None:
            dic_linha = dict(linha)
            itens.append(dic_linha)
            linha = linhas.fetchone()
        return itens


def itens_em_uso_por_nome_do_heroi(nomeHeroi):
    with engine.connect() as con:
        query = "SELECT Item.* FROM Item INNER JOIN ItemDoHeroi ON Item.id = ItemDoHeroi.iditem INNER join Heroi ON ItemDoHeroi.idheroi = Heroi.id WHERE Heroi.nome = :heroi and Item.emUso = 1"
        linhas = con.execute(query, heroi = nomeHeroi)
        itens = []
        linha = linhas.fetchone()
        while linha != None:
            dic_linha = dict(linha)
            itens.append(dic_linha)
            linha = linhas.fetchone()
        return itens


def ultimo_ItemDoHeroi():
    with engine.connect() as con:
        query = "SELECT id FROM ItemDoHeroi ORDER BY id"
        linhas = con.execute(query)
        linha = linhas.fetchone()
        ultimo = int()
        while linha != None:
            ultimo = int(linha[0])
            linha = linhas.fetchone()
        return ultimo


def dando_item_para_heroi(heroi, item):
    with engine.connect() as con:
        query = "INSERT INTO ItemDoHeroi VALUES (:id, :idItem, :idHeroi)"
        linhas = con.execute(query, id = ultimo_ItemDoHeroi() + 1, idItem = item, idHeroi = heroi)


def colocando_item_em_uso(heroi, item):
    with engine.connect() as con:
        query = "UPDATE Item SET emuso = 1 WHERE id = (SELECT iditem from ItemDoHeroi WHERE idheroi = :idHeroi and iditem = :idItem)"
        linhas = con.execute(query, idItem = item, idHeroi = heroi)


def tipos_itens_do_heroi(id_h):
    with engine.connect() as con:
        query = "SELECT Item.tipo FROM Item INNER JOIN ItemDoHeroi ON Item.id = ItemDoHeroi.iditem and ItemDoHeroi.idheroi = :heroi where Item.emuso = 1"
        linhas = con.execute(query, heroi = id_h)
        tipos_itens = []
        linha = linhas.fetchone()
        while linha != None:
            tipos_itens.append(str(linha[0]))
            linha = linhas.fetchone()
        return tipos_itens
