import numpy as np
from random import choice


class NovoJogo(object):
	
	def __init__(self):
		self.arquivos = dict()
	
	
	def iniciar(self, linhas=4, colunas=3):
		self.linhas = linhas
		self.colunas = colunas
		# Gerar o tabuleiro
		matriz = self.gerar_tabuleiro()
		# Gerar chaves válidas para resolução
		chaves = self.gerar_chaves()
		# Atribuir a resposta
		self.arquivos["matriz"] = matriz
		self.arquivos.update(chaves)
		return self.arquivos
	
	
	def gerar_tabuleiro(self):
		self.elementos = ["7A", "1C",  "E7", "BD", "E9", "55", "FF"]
		self.matriz = np.random.choice(self.elementos, (self.linhas, self.colunas))
		return self.matriz
		
		
	def gerar_chaves(self):
		# Chaves
		chave1 = []
		chave2 = []
		chave3 = []
	
		# Tamanho das chaves
		tamanho1 = choice(range(2,3))
		tamanho2 = choice(range(3,5))
		tamanho3 = choice(range(tamanho2, 6))
		tamanhos = [tamanho1, tamanho2, tamanho3]
		
		# Por qual chave comecar
		opcoes = [chave1, chave2, chave3]
		bkp_opcoes = list()
		# item = choice(opcoes)
		# ...
		
		chaves = {
			"chave1": chave1,
			"chave2": chave2,
			"chave3": chave3
		}
		
		return chaves
		
		
jogo = NovoJogo()
x = jogo.iniciar(5,5)
print("TABULEIRO:\n")
print(x["matriz"])
print("\nChave1: ", x["chave1"])
print("\nChave2: ", x["chave2"])
print("\nChave3: ", x["chave3"])

