

from jogadores_consultas import JogadorNaoExisteException
from jogadores_consultas import conta_jogadores
from jogadores_consultas import consultar_jogador
from jogadores_consultas import jogador_por_email 
'''

Examine as funcoes do arquivo jogadores_consultas.py, que ilustra como
podemos usar o sql no python com sqlite.

(depois faça várias atividades e depois volte aqui)

Examine as funcoes do jogadores.py, que mostra como fazer alteracoes
no banco usando a biblioteca sqlite

'''
from jogadores_editar import criar_jogador
from jogadores_editar import alterar_jogador
from jogadores_editar import remover_jogador


'''
Inicio dos testes
'''

import unittest
import hashlib
class TestStringMethods(unittest.TestCase):

    def test_consultas_01_jogador_por_id(self):
        self.assertEqual(consultar_jogador(1)['nome'],'lucas goncalves')
        self.assertEqual(consultar_jogador(2)['nome'],'victor')
        self.assertRaises(JogadorNaoExisteException,consultar_jogador,567)


    def test_consultas_02_contar_jogadores(self):
        self.assertEqual(conta_jogadores(),3)
    
    def test_consultas_03_jogador_por_email(self):
        self.assertEqual(jogador_por_email('lucas.goncalves@faculdadeimpacta.com.br')['nome'],'lucas goncalves')
        self.assertEqual(jogador_por_email('victor.silva@faculdadeimpacta.com.br')['nome'],'victor')
        self.assertRaises(JogadorNaoExisteException,jogador_por_email,'john@doe')


    def test_editar_01_criar_jogadores(self):
        criar_jogador('macaco louco','macaco@superpoderosas.com')
        self.assertEqual(conta_jogadores(),4)
        self.assertEqual(jogador_por_email('macaco@superpoderosas.com')['nome'],
                         'macaco louco')


    def test_editar_02_alterar_jogadores(self):
        novo_victor = {'email': 'victor.silva@faculdadeimpacta.com.br',
                        'nome': 'victor silva'}
        alterar_jogador(2,novo_victor)
        self.assertEqual(consultar_jogador(2)['nome'],'victor silva')
    
    def test_editar_03_excluir_jogadores(self):
        criar_jogador('homem codorna','doug@funny.com')
        self.assertEqual(jogador_por_email('doug@funny.com')['nome'],
                         'homem codorna')
        remover_jogador(5)
        self.assertRaises(JogadorNaoExisteException,jogador_por_email,'doug@funny.com')
    
import shutil
def runTests():
        shutil.copyfile('rpg.original.db','rpg.db')
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
