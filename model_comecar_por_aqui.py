

'''
1) Examine o banco de dados no site https://sqliteonline.com/.
O arquivo é rpg.db, e você pode subir ele ao site
usando file > opendb. Note que há 4 tabelas diferentes
(veja no canto superior direito).

Depois pode fazer varias consultas (por exemplo, select * from jogador;
select * from Heroi; select * from Item; select * from ItemDoHeroi)

2) rode "pip install sqlalchemy --user" no cmd para poder usar os arquivos
fornecidos

3) Examine as funcoes do arquivo exemplo_sql/jogador_consultas.py, 
que ilustra como podemos usar o sql no python com sqlite. 
Pode deixar os demais arquivos do diretório exemplo_sql/ para depois



4) Sobre o sqlite:
    Voce deve manipular e consultar apenas o arquivo rpg.db
    Jamais manipule o arquivo rpg.original.db no seu programa,
    pois ele serve para termos um ponto de partida confiavel
    para os testes

    Voce nao deve enviar os arquivos sqlite ao submeter sua AC

5) Seu ponto de partida é esse arquivo model. Ele pedirá que você crie funções,
tanto nele quanto nos outros arquivos, e será com ele que voce rodará os testes
'''



'''
já temos um arquivo herois, que foi importado
abaixo
'''
from herois import HeroiNaoExisteException
import herois

'''
Parte 1: Consultas

Se familiarize com as tabelas "Heroi" e "Item", pois 
vamos fazer diversas consultas com elas.

Então, comece os exercícios abaixo
'''

'''
Ex1
O arquivo herois deve conter uma função heroi_existe
Ela recebe uma id de herói e consulta no banco para ver
se o herói em questão existe. Ela retorna True
se ele existe, False caso contrário
'''
# Ok!!
'''
Ex2
O arquivo herois deve conter uma funcao 
consultar_heroi.
ela recebe uma id de heroi e retorna 
um dicionario com todos os dados do heroi
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma HeroiNaoExisteException 
'''
# Ok!!
'''
Já existe um arquivo itens.py,
que está importado abaixo

'''
from itens import ItemNaoExisteException
import itens

'''
Ex3
O arquivo itens.py
deve conter uma funcao consultar_item.
ela recebe uma id de item e retorna 
um dicionario com todos os dados do item
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma ItemNaoExisteException (que voce deverá
criar)

(já fizemos coisa parecida no heroi. Lá, foram
3 testes, agora é um só testando tudo!)
'''
# Ok!!
'''
Ex4
Nesse arquivo model, crie uma funcao heroi_pronto_por_nome, que recebe um nome de heroi
e retorna um dicionario com os dados desse heroi.

Os itens ainda nao sao importantes, mas serão em breve

fazer a funcao abaixo - pode ser útil definir uma
nova função de acesso ao banco, chamada consultar_heroi_por_nome,
no arquivo herois
'''

from herois import consultar_heroi_por_nome
from itens_do_heroi import itens_em_uso_por_nome_do_heroi

def heroi_pronto_por_nome(nomeHeroi):
    dicionario_itens_em_uso_do_heroi = itens_em_uso_por_nome_do_heroi(nomeHeroi)
    dicionario_heroi = consultar_heroi_por_nome(nomeHeroi)
    for i in dicionario_itens_em_uso_do_heroi:
        dicionario_heroi['fisico'] += i['fisico']
        dicionario_heroi['magia'] += i['magia']
        dicionario_heroi['agilidade'] += i['agilidade']
    dicionario_heroi['vida'] = int(dicionario_heroi['fisico']) * 10
    return dicionario_heroi

'''
Ex5 (ainda no model.py)
Melhore sua funcao heroi_pronto_por_nome. Agora, o dicionario também
incluirá o a chave vida. O valor da vida de um heroi é inicializado
com seu fisico multiplicado por 10

(fazer a funcao nesse arquivo - na verdade, melhorar a função
que já existe)
'''
# Ok!!
'''
Ex06 (ainda no model.py)
Chegou a hora de fazer um ataque!

A função atacar_com_fisico recebe dois dicionarios, de dois herois. 
(esses dicionarios sao os gerados pela funcao heroi_pronto_por_nome
mas, você não precisa chamar a função. Eu mesmo chamo lá no teste
e já te passo os dicionários)

O primeiro heroi é o atacante e o segundo é o defensor

O defensor perde vida. A perda é igual ao atributo fisico do atacante.

O retorno não importa, o que importa é alterar o dicionario do defensor

Repare que a funcao recebe dicionários, e nem fala com o SQL
'''


def atacar_com_fisico(atacante, defensor):
   defensor['vida'] -= atacante['fisico']

'''
Opcional - não testado

Se você quiser, pode usar a funcao mensagem_de_ataque_fisico para
dar uns prints simpaticos avisando quanto de dano o defensor tomou.

A função mensagem_de_ataque_fisico já está definida, mais abaixo, 
mas você pode trocar as
mensagens de ataque por coisas mais interessantes, se quiser.

Esses prints nao serão corrigidos, é só pela diversão mesmo
'''


'''
Ex07 (ainda no arquivo model)
A função atacar_com_magia faz o mesmo, mas agora o dano do
defensor é o atributo magia do atacante.

Repare que a vida nunca pode ficar negativa. O mínimo é 0.

(fazer a funcao abaixo) - ela recebe dicionarios e nem fala com o sql
'''
from math import floor as arredondaBaixo

def atacar_com_magia(atacante, defensor):
    qtd_ataques = atacante['agilidade'] / defensor['agilidade']
    qtd_ataques = (qtd_ataques <= 1 and 1 or arredondaBaixo(qtd_ataques))
    for i in range(0,qtd_ataques):
        defensor['vida'] -= atacante['magia']
        if defensor['vida'] < 0:
            defensor['vida'] = 0

'''
Parte 2: Consultas mais complexas
Temos um terceiro arquivo de acesso ao banco, 
chamado itens_do_heroi. Ele está importado
abaixo
Ele representa um relacionamento. Diz quais herois tem quais itens.

Verifique e se familiarize com a tabela ItemDoHeroi do banco de dados
'''
import itens_do_heroi

'''
Ex08
No arquivo itens_do_heroi, crie uma funçao heroi_tem_item.

Ela recebe uma id de heroi, e retorna True se o heroi
possui algum item, false caso contrário

Um heroi 10 tem o item 15 se na tabela itemDoHeroi
temos uma linha com idItem 15 e idHeroi 10
'''
# Ok!!
'''
Ex09
No arquivo itens_do_heroi,
crie uma função heroi_quantos_itens, que recebe uma
id de heroi e diz quantos itens ele possui
'''
# Ok!!
'''
Ex10

No arquivo itens_do_heroi,
crie uma funcao itens_do_heroi

Ela recebe a id do heroi e devolve uma lista com dicionarios, um para cada item dele.

Cada dicionário descreve um item 

Por exemplo, se o heroi 3 tem uma varinha com 2 de magia:

Chamar itens_do_heroi.itens_do_heroi(3) vai devolver a lista de dicionarios. Um desses dicionarios vai representar a varinha: ter chaves "tipo" com valor "varinha" e chave "magia" com valor 2


Dica: é possivel fazer com duas consultas, usando
o python para fazer o meio de campo, mas é mais
interessante e rápido usar um join
'''
# Ok!!
'''
Ex11
Agora, criemos uma nova função, que lista apenas os itens em uso. Essa função será criada no arquivo model, onde você está agora

Um item está em uso quando o valor da coluna emUso é 1.
Se for 0, o heroi tem o item mas não está usando.

A assinatura da função será:
def lista_itens_em_uso_do_heroi(idHeroi):

Voce já pegou todos os dados necessários 
do banco. Usando as funcoes que já definiu, nao precisará
fazer acessos a mais
'''
from itens_do_heroi import itens_em_uso_do_heroi


def lista_itens_em_uso_do_heroi(idHeroi):
    return itens_em_uso_do_heroi(idHeroi)

'''
Ex12
Funcao itens em uso por nome do heroi

Crie essa função no arquivo itens_do_heroi

Ela recebe uma string (o nome do heroi) e devolve uma lista (com os itens em uso do heroi)

Cada item é um dicionário descrevendo o item

Recomendo usar um join para fazer a consulta, mas terá que ter cuidado. Se fizer o join de forma desatenta, pode ser que os atributos do heroi sobrescrevam os do item (vide teste 12b)
'''
# Ok!!
'''
Ex13
Melhore sua função heroi_pronto_por_nome: agora, os o dicionario que representa o heroi é alterado pelos itens em uso. 

Se o heroi está usando um item que aumenta
suas habilidades, as habilidades que aparecem no dicionario serão
as do heroi, aumentadas de acordo com o item

Por exemplo, considere um heroi com agilidade 2 e usando 
um item de agilidade 3. Para ele, o dicionario devera 
reportar agilidade 5 

repare, porem, que o item tem que ser do heroi e estar
em uso para fazer efeito

(fazer a funcao nesse arquivo - na verdade, melhorar a função
que já existe)
Se for o caso, altere a vida do heroi adequadamente! (ex13b)
'''
# Ok!!
'''
Ex14
Façamos um upgrade nas nossas funções de ataque: se o atacante
for muito mais rápido que o defensor, poderá atacar mais vezes

Para isso, divida agilidade do atacante pela agilidade do defensor,
arredondando para baixo.

Se der algum número maior que 1, esse é o número de ataques
que o atacante vai conseguir fazer.

Se der 1 ou menos, o atacante conseguirá fazer exatamente 1 ataque.

Fazer um ataque 2 vezes significa dar duas vezes o dano:
Se harry tem 7 de magia e vai atacar 2 vezes, dará 14 de dano
'''
# Ok!!
'''
Parte 3: Editar os valores do banco de dados

Agora você já conhece todos os arquivos, é hora de criar herois e heroinas
'''

'''
Ex20 (sim, pulamos alguns numeros)
Nesse arquivo, faça uma funcao criar heroi, que recebe
o nome e os atributos:

def criar_heroi(nome,agilidade,fisico,magia):

Ela deve criar um heroi no banco de dados, com os atributos
dados.

Para isso, ela deve chamar uma funcao no arquivo heroi.py. Essa funcao no heroi.py fará o acesso ao banco de dados
'''

class OverpowerException(Exception):
    pass

from herois import criando_heroi

def criar_heroi(nome,agilidade,fisico,magia):
    if agilidade + fisico + magia > 20:
        raise OverpowerException
    else:
        dic = dict()
        dic['nome'] = nome
        dic['agilidade'] = agilidade
        dic['fisico'] = fisico
        dic['magia'] = magia
        criando_heroi(dic)

'''
Ex21
Façamos um upgrade em criar_heroi. Se o heroi for poderoso
demais (a soma dos 3 atributos for maior que 20) nossa funcao
criar_heroi devera lançar uma OverpowerException

(fazer a funcao nesse arquivo. Na verdade, se trata de um upgrade de criar_heroi)

(Você também deve criar a excessao nesse arquivo)
'''
# Ok!!
'''
Ex22
No arquivo itens.py crie uma funcao nome_para_id_item, que recebe
um nome de item e devolve a id numerica correspondente

(se você nao deletou, esse arquivo ja foi importado)
'''
# Ok!!
'''
Ex23
no arquivo itens.py, crie uma funcao criar_item, que recebe os atributos
do item e cria um item novo no banco de dados.

Ou seja, uma funcao com a seguinte assinatura:
criar_item(tipo, nome,fisico,agilidade,magia)

repare: omitimos um dos atributos do item, o emUso. Esse atributo
será inicializado sempre com 0, para representar False
'''
# Ok!!
'''
Ex24 -- repare que voce precisa de duas funcoes para passar esse teste!
Crie uma funcao dar_item_para_heroi, que faz com que o heroi se
torne o dono (ou dona) do item. Ela recebe dois dicionarios:
um do heroi e um do item.

Para dar o item ao heroi, sua função deve 
chamar uma funcao no arquivo itens_do_heroi,
que você também deverá criar. No itens_do_heroi, você
adicionará uma linha nova, marcando que o item pertence
ao heroi. 

Lembre-se de manter o codigo sql apenas no arquivo itens_do_heroi

Alem dessa funcao, para passar o teste relevante, voce precisara
tambem do proximo exercicio (colocar_item_em_uso)
'''

from itens_do_heroi import dando_item_para_heroi, colocando_item_em_uso, tipos_itens_do_heroi


def dar_item_para_heroi(heroi, item):
    dando_item_para_heroi(heroi['id'], item['id'])


'''
Ex24 -- essa é a segunda função necessária para passar o ex 24
Crie uma funcao colocar_item_em_uso, que recebe o dicionario do
heroi e o dicionario do item, e faz com que o item fique emUso

Para isso, voce deve criar uma funcao no arquivo itens para a manipulacao
do SQL
'''
class HeroiJaUsaEsseTipoDeItemException(Exception):
    pass

def colocar_item_em_uso(heroi,item):
    if item['tipo'] in tipos_itens_do_heroi(heroi['id']):
        raise HeroiJaUsaEsseTipoDeItemException
    else:
        colocando_item_em_uso(heroi['id'], item['id'])

'''
Ex25
Façamos um upgrade em colocar_item_em_uso: um item só pode ficar em 
uso se o heroi nao está usando outro item do mesmo tipo

Se tentarmos colocar_item_em_uso em um chapeu quando o heroi já
tem um chapeu em uso, a funcao deve lancar 
o erro HeroiJaUsaEsseTipoDeItemException
'''
# Ok!!
'''
Voce terminou a atividade!

Agora, pode fazer tres coisas:
    * primeiro, experimentar os prints abaixo
    * depois, fazer o server.py receber dois nomes de lutadores
    e colocar eles pra brigar de verdade
    * terceiro: criar uma nova tabela,de ataques personalizados
    por exemplo "merlin sufoca harry com a sua barba" e
    "hulk esmaga conan". um heroi poderá ter um ou mais
    ataques personalizados, e deverá usar eles em vez/misturados
    com os genericos (como você preferir, porque isso nao
    será testado)
'''

'''
O uso das funcoes a seguir é opcional
'''
fazer_prints = False
import random
def mensagem_de_ataque_fisico(dano,nome_atacante,nome_defensor):
    msgs = [f'{nome_atacante} dá um soco em {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} dá um chute em {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} ataca {nome_defensor} covardemente, causando {dano} de dano']
    msg = msgs[random.randrange(0,len(msgs)-1)]
    if fazer_prints:
        print(msg)

def mensagem_de_ataque_magico(dano,nome_atacante,nome_defensor):
    msgs = [f'{nome_atacante} solta raios contra {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} congela {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} transforma {nome_defensor} em um flamingo, causando {dano} de dano']
    msg = msgs[random.randrange(0,len(msgs)-1)]
    if fazer_prints:
        print(msg)

def luta(atacante,defensor):
    while (atacante['vida'] != 0 and defensor['vida'] != 0):
        if atacante['magia'] > atacante['fisico']:
            atacar_com_magia(atacante,defensor)
        else:
            atacar_com_fisico(atacante,defensor)
        print(f'Agora, {defensor["nome"]} tem {defensor["vida"]} de vida')
        atacante,defensor = defensor,atacante #inverte

def merlin_versus_harry():
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        luta(merlin,harry)
'''
Fim das funcoes de uso opcional

Inicio dos testes
'''

import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

    def test_ex01_heroi_existe(self):
        self.assertTrue(herois.heroi_existe(1))
        #    ----------  xxxxx oooooooooooo a
        #  no arquivo herois (xxxxx), tem que existir uma funcao
        # heroi existe (oooooooo), quando eu passar o argumento 1
        # para ela (a), a funcao tem que retornar verdadeiro
        # (---------)
        self.assertTrue(herois.heroi_existe(2))
        self.assertTrue(herois.heroi_existe(3))
        self.assertFalse(herois.heroi_existe(30))

    def test_ex02_consultar_heroi(self):
        self.assertEqual(herois.consultar_heroi(1)['nome'],'conan')
        self.assertEqual(herois.consultar_heroi(2)['nome'],'merlin')
        #    ooooooooooo--------------------------------- xxxxxxxx
        #estou usando o assertEqual (ooooooo) para dizer que o lado
        # esquerdo (--------) tem que ser igual ao direito (xxxxxxx)
        self.assertEqual(herois.consultar_heroi(3)['nome'],'harry')
   
    def test_ex02a_consultar_heroi_invalido(self):
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,50329)
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,50)
        #                 xxxxxxxxxxxxxxxxxxxxxxx oooooooooooooooooooooo aa
        #diz que tem que ocorrer uma excessão (xxxxxx), quando eu chamar aa funcao (ooooooooooo) com a id 50 (aa)
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,450)

    def test_ex03_consultar_item(self):
        self.assertEqual(itens.consultar_item(1)['nome'],'forca do gigante')
        self.assertEqual(itens.consultar_item(1)['tipo'],'cinto')
        self.assertEqual(itens.consultar_item(2)['nome'],'de alladin')
        self.assertEqual(itens.consultar_item(2)['tipo'],'lampada')
        self.assertRaises(ItemNaoExisteException,itens.consultar_item,329)
    
    def test_ex04_heroi_pronto_por_nome(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['fisico'],3)
        self.assertEqual(heroi_pronto_por_nome('conan')['magia'],2)
        self.assertEqual(heroi_pronto_por_nome('conan')['agilidade'],5)
        self.assertEqual(heroi_pronto_por_nome('merlin')['fisico'],3)
        self.assertEqual(heroi_pronto_por_nome('merlin')['agilidade'],1)
        self.assertEqual(heroi_pronto_por_nome('merlin')['magia'],8)
    
    def test_ex05_vida_do_heroi(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['vida'],30)
        self.assertEqual(heroi_pronto_por_nome('merlin')['vida'],30)
    
    def test_ex06_ataque_fisico(self):
        conan = heroi_pronto_por_nome('conan')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'],20)
        atacar_com_fisico(atacante=conan,defensor=harry)
        #conan tem 3 de fisico, harry perdeu 3 de vida
        self.assertEqual(harry['vida'],17)
        atacar_com_fisico(atacante=conan,defensor=harry)
        self.assertEqual(harry['vida'],14)
        atacar_com_fisico(defensor=conan,atacante=harry)
        self.assertEqual(conan['vida'],28)

    def test_ex07_ataque_magico(self):
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'],20)
        atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],12)
        atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],4)
        atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],0)

    def test_ex08_heroi_tem_item(self):
        self.assertEqual(itens_do_heroi.heroi_tem_item(1),True)
        self.assertEqual(itens_do_heroi.heroi_tem_item(3),True)
        self.assertEqual(itens_do_heroi.heroi_tem_item(2),False)
    
    def test_ex09_heroi_quantos_itens(self):
        self.assertEqual(itens_do_heroi.heroi_quantos_itens(1),2)
        self.assertEqual(itens_do_heroi.heroi_quantos_itens(3),1)
        self.assertEqual(itens_do_heroi.heroi_quantos_itens(2),0)
    
    def test_ex10a_itens_do_heroi_acerta_quantidades(self):
        self.assertEqual(len(itens_do_heroi.itens_do_heroi(1)),2)
        self.assertEqual(len(itens_do_heroi.itens_do_heroi(3)),1)
        self.assertEqual(len(itens_do_heroi.itens_do_heroi(2)),0)


    
    def test_ex10b_itens_do_heroi(self):
        itens = itens_do_heroi.itens_do_heroi(1)
        lista_tipos = [itens[0]['tipo'],itens[1]['tipo']]
        self.assertIn('cinto',lista_tipos)
        self.assertIn('lampada',lista_tipos)

    


    def test_ex11_itens_que_heroi_esta_usando(self):
        self.assertEqual(len(lista_itens_em_uso_do_heroi(1)),0)
        self.assertEqual(len(lista_itens_em_uso_do_heroi(3)),1)
        self.assertEqual(len(lista_itens_em_uso_do_heroi(2)),0)
        item=lista_itens_em_uso_do_heroi(3)
        item_do_3 = item[0]
        self.assertEqual(item_do_3['tipo'],'varinha')

    def test_ex12_itens_em_uso_por_nome_do_heroi(self):
        itens = itens_do_heroi.itens_em_uso_por_nome_do_heroi("conan")
        self.assertEqual(itens,[])
        itens = itens_do_heroi.itens_em_uso_por_nome_do_heroi("harry")
        self.assertEqual(len(itens),1)
        #varinha de duelo do harry é do tipo "varinha"
        self.assertEqual(itens[0]['tipo'],"varinha")
    
    def test_ex12b_itens_em_uso_por_nome_do_heroi_verifica_atributos(self):
        itens = itens_do_heroi.itens_em_uso_por_nome_do_heroi("harry")
        #varinha de duelo do harry tem 2 de magia. Cuidado! dependendo
        #de como você fez seu select, você poderá ver a magia do harry
        #no lugar da magia da varinha.
        #Seu select, em vez de usar SELECT * FROM, deve especificar
        #as colunas, para poder especificar a coluna Item.magia,
        #e evitar esse problema
        self.assertEqual(itens[0]['magia'],2)
        # e faça o mesmo para agilidade e fisico. Mostrar os atributos do
        # item, nao do personagem!
        self.assertEqual(itens[0]['agilidade'],1)
        self.assertEqual(itens[0]['fisico'],0)
    

    def test_ex13_status_alterado_por_itens(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['fisico'],3)
        self.assertEqual(heroi_pronto_por_nome('conan')['magia'],2)
        self.assertEqual(heroi_pronto_por_nome('conan')['agilidade'],5)
        self.assertEqual(heroi_pronto_por_nome('harry')['fisico'],2)
        self.assertEqual(heroi_pronto_por_nome('harry')['agilidade'],4)
        self.assertEqual(heroi_pronto_por_nome('harry')['magia'],7)
        self.assertEqual(heroi_pronto_por_nome('merlin')['fisico'],3)
        self.assertEqual(heroi_pronto_por_nome('merlin')['agilidade'],1)
        self.assertEqual(heroi_pronto_por_nome('merlin')['magia'],8)

    
    def test_ex13b_vida_do_heroi_alterado_por_itens(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['vida'],30)
        self.assertEqual(heroi_pronto_por_nome('merlin')['vida'],30)
        self.assertEqual(heroi_pronto_por_nome('harry')['vida'],20)
    

    def test_ex14_ataque_repetido_gracas_a_agilidade(self):
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(merlin['vida'],30)
        atacar_com_magia(atacante=harry,defensor=merlin)
        self.assertEqual(merlin['vida'],2)
        atacar_com_magia(atacante=harry,defensor=merlin)
        self.assertEqual(merlin['vida'],0)

    def test_ex20_criar_heroi(self):
        criar_heroi('chun-li',agilidade=5,fisico=7,magia=0)
        chun = heroi_pronto_por_nome('chun-li')
        self.assertEqual(chun['agilidade'],5)
        self.assertEqual(chun['fisico'],7)
        harry = heroi_pronto_por_nome('harry')
        atacar_com_magia(atacante=harry,defensor=chun)
        self.assertEqual(chun['vida'],63)


    def test_ex21_criar_overpower(self):
        self.assertRaises(OverpowerException,criar_heroi,'freeza',10,10,10)
        self.assertRaises(OverpowerException,criar_heroi,'legolas',20,2,2)


    def test_ex22_nome_para_id_item(self):
        idDuelo = itens.nome_para_id_item('de duelo')
        duelo = itens.consultar_item(idDuelo)
        self.assertEqual(duelo['nome'],'de duelo')
        idConfortavel = itens.nome_para_id_item('confortavel')
        confortavel = itens.consultar_item(idConfortavel)
        self.assertEqual(confortavel['nome'],'confortavel')


    def test_ex23_criar_item(self):
        itens.criar_item(tipo='varinha', nome='mestra',fisico=0,agilidade=0,magia=8)
        idMestra = itens.nome_para_id_item('mestra')
        mestra = itens.consultar_item(idMestra)
        self.assertEqual(mestra['nome'],'mestra')
        self.assertEqual(mestra['id'],idMestra)
        self.assertEqual(mestra['magia'],8)

    def test_ex24_dar_item_para_heroi_e_colocar_item_em_uso(self):
        itens.criar_item(tipo='espada', nome='celestial',
                          fisico=3,agilidade=3,magia=3)
        chun = heroi_pronto_por_nome('chun-li')
        idCelestial = itens.nome_para_id_item('celestial')
        celestial = itens.consultar_item(idCelestial)
        dar_item_para_heroi(heroi=chun,item=celestial)
        chun = heroi_pronto_por_nome('chun-li')
        self.assertEqual(chun['agilidade'],5) #agilidade ainda nao mudou
        colocar_item_em_uso(chun,celestial)
        self.assertEqual(chun['agilidade'],5) #agilidade ainda nao mudou,
        #pois ainda nao fizemos uma nova consulta
        chun = heroi_pronto_por_nome('chun-li')
        self.assertEqual(chun['agilidade'],8) #agilidade mudou
        #chun está usando o item e tb fizemos a nova consulta


    def test_ex25_heroi_nao_pode_usar_dois_itens_do_mesmo_tipo(self):
        itens.criar_item(tipo='espada', nome='vorpal',
                          fisico=10,agilidade=2,magia=0)
        chun = heroi_pronto_por_nome('chun-li')
        idVorpal = itens.nome_para_id_item('vorpal')
        vorpal = itens.consultar_item(idVorpal)
        dar_item_para_heroi(heroi=chun,item=vorpal) #roda sem problemas
        #o que nao pode eh ela usar o item, porque ela ja tem outra varinha
        self.assertRaises(HeroiJaUsaEsseTipoDeItemException,colocar_item_em_uso,chun,vorpal)




import shutil
def runTests():
        shutil.copyfile('rpg.original.db','rpg.db')
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
