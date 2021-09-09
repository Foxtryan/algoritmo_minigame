import numpy as np
from random import choice, shuffle


class NovoJogo(object):
    
    def __init__(self):
        self.arquivos = dict()
        self.resposta = []
    
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
        self.arquivos["resposta"] = self.resposta
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
        shuffle(opcoes)
        # Primeiro sorteio começa na linha 0

        # Clone da Matriz para formar as chaves
        mod_matriz = matriz.copy()
        
        # primeiro numero sempre linha 0
        self.linha = 0
        self.coluna = 0
        for chave in opcoes:
            for n in range(tamanhos[chave]):
                valor = "00"
                while valor == "00":
                    pos = self.verificar_chave(n)
                    valor = mod_matriz[pos]
                    
                # A linha abaixo adiciona a coordenada ao lado da chave gerada
                #chaves[chave].append([valor, [pos]])
                
                # A linha abaixo gera somente a chave sem a coordenada
                chaves[chave].append([valor])
                
                # Gera a resposta esperada
                self.resposta.append([pos])
                # zera o valor da matriz de teste para nao repetir        
                mod_matriz[pos] = "00"
        return chaves
        
    def verificar_chave(self, n):
        if n % 2 == 0:
            self.coluna = choice(range(0, self.colunas))
        else:
            self.linha = choice(range(0, self.linhas))
        pos = self.linha, self.coluna
        return pos

def teste_dev(x):
    while True:
        print("\nVerificar valor (Vazio interrompe a execução): ")
        linha = input("Linha: ")
        coluna = input("Coluna: ")
        if linha == "" or coluna == "":
            break
        else:
            print(f"Valor da pos:[{linha},{coluna}]\n>>>: ", x["matriz"][int(linha), int(coluna)])
        
        # Resolver a partir daqui
        
        
if __name__ == '__main__':
    jogo = NovoJogo()
    x = jogo.iniciar(5,5)

    print("TABULEIRO:\n")
    print(x["matriz"])
    print("\nChave1: ", x["chave1"])
    print("\nChave2: ", x["chave2"])
    print("\nChave3: ", x["chave3"])
    print("\nResposta esperada: ", x["resposta"])

    # teste_dev(x)
