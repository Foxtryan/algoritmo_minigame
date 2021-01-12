import numpy as np
from random import choice


class NovoJogo(object):
	
	def __init__(self):
		self.arquivos = dict()
	
	
	def iniciar(self, linhas=4, colunas=3):
		if linhas < 4:
			linhas = 4
		if colunas < 3:
			colunas = 3
	
		self.linhas = linhas
		self.colunas = colunas
		# Gerar o tabuleiro
		matriz = self.gerar_tabuleiro()
		# Gerar chaves válidas para resolução
		chaves = self.gerar_chaves(matriz)
		# Atribuir a resposta
		self.arquivos["matriz"] = matriz
		self.arquivos.update(chaves)
		return self.arquivos
	
	
	def gerar_tabuleiro(self):
		elementos = ["7A", "1C",  "E7", "BD", "E9", "55", "FF"]
		matriz = np.random.choice(elementos, (self.linhas, self.colunas))
		return matriz
		
		
	def gerar_chaves(self, matriz):
		# Chaves
		chave1 = []
		chave2 = []
		chave3 = []
		chaves = {"chave1": chave1, "chave2": chave2, "chave3": chave3}
		
		# Tamanho das chaves
		
		tamanho1 = 3
		tamanho2 = 3
		tamanho3 = choice(range(3,5))
		tamanhos = {"chave1": tamanho1, "chave2": tamanho2, "chave3": tamanho3}
		
		# Por qual chave comecar
		opcoes = ["chave1", "chave2", "chave3"]
		chave = choice(opcoes)
		
		# sortear um elemento para a soma de todos os tamanhos 3+3+4=10
		valores = dict()
		
		for i in range(sum(list(tamanhos.values()))):
			# Se for o primeiro sorteio
			if valores == {}:
				linha = 0
				coluna = choice(range(self.colunas))
			else:
				if i % 2 != 0:
					linha = choice(range(self.colunas))
				else:
					coluna = choice(range(self.colunas))
			pos = [linha, coluna]
			''' com as duas funcionam mas valores em posicoes dobradas podem ser sorteados '''
			# valor = matriz[linha, coluna]
			# valores[i] = [valor, pos]
			''' Valores e posições repetidos são invalidos, então: '''
			while True:
				response = [matriz[linha, coluna] , pos] in valores.values()
				if response is False:
					valor = matriz[linha, coluna]
					break
				else:
					if i % 2 == 0:
						if linha+1 < self.linhas:
							linha += 1
						else:
							linha -= 1
					else:
						if coluna+1 < self.colunas:
							coluna += 1
						else:
							coluna -= 1
					pos = [linha, coluna]

			valores[i] = [valor, pos]
		
		''' '''
		# Distribuir os valores sorteados nas chaves:
		i = 0
		for chave in tamanhos.keys(): # chave1, cahve2, chave3
			while len(chaves[chave]) < tamanhos[chave]:
				chaves[chave].append(valores[i])
				i += 1

		chaves = {
			"chave1": chave1,
			"chave2": chave2,
			"chave3": chave3
		}
		return chaves
		
def teste_dev(x):
	while True:
		print("\nVerificar valor (Vazio interrompe a execução): ")
		linha = input("Linha: ")
		coluna = input("Coluna: ")
		if linha == "" or coluna == "":
			break
		else:
			print(f"Valor da pos:[{linha},{coluna}]\n>>>: ", x["matriz"][int(linha), int(coluna)])
		
jogo = NovoJogo()
x = jogo.iniciar(5,5)

print("TABULEIRO:\n")
print(x["matriz"])
print("\nChave1: ", x["chave1"])
print("\nChave2: ", x["chave2"])
print("\nChave3: ", x["chave3"])

teste_dev(x)
