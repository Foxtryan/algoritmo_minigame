# algoritmo_minigame
*Em desenvolvimento.

Algoritmo do Coding Dojo baseado no minigame "Breach Protocol" de CP2077.

RESOLUÇÃO DE ALGORITMO.

	- PROBLEMA E REGRAS:
		- MATRIZ COM VALORES GERADOS ALEATÓRIAMENTE;
		- TODA MATRIZ TEM TRÊS CHAVES;
		- CADA CHAVE POSSUI UMA SEQUENCIA DE ELEMENTOS PRÓPRIOS QUE DEVEM SER PREENCHIDOS EM ORDEM PARA RESOLUÇÃO DA CHAVE;
		- A ORDEM DA RESOLUÇÃO DAS CHAVES NÃO IMPORTAM;
		- A ORDEM DOS ELEMENTOS PERTENCENTES AS CHAVES DEVEM SER PREENCHIDOS EM ORDEM;
		- A CHAVE REINICIA CASO O PREENCHIMENTO FOR INTERROMPIDO POR UM CÓDIGO DISTINTO DE SUA ORDEM;
		- CASO OS ELEMENTOS DENTRO DE DUAS OU MAIS CHAVES SIGAM A MESMA ORDEM, ELES SERÃO PREENCHIDOS EM CONJUNTO,
		RESPEITANDO A REGRA ANTERIOR.
	
	- MOVIMENTO:
		- O PRIMEIRO MOVIMENTO SEMPRE DEVE OCORRER NA PRIMEIRA LINHA;
		- O ALGORITMO DEVE MARCAR UM CÓDIGO DE CHAVE;
		- O MOVIMENTO APAGARÁ O VALOR NO INDEX ALI ESTABELECIDO;
		- O PRÓXIMO MOVIMENTO DEVE OCORRER NA COLUNA DO INDEX ATUALMENTE MARCADO;
		- O MOVIMENTO SEGUINTE, SEGUIRÁ NA HORIZONTAL DO INDEX DA COLUNA MARCADO ANTERIORMENTE;
		- ASSIM SUCESSIVAMENTE, ATÉ AS TRÊS CHAVES SEREM PREENCHIDAS.
    
# EXEMPLO:

elementos = ["7A", "1C", "E7", "BD", "E9", "55", "FF"]

matriz = [
	["55", "E7", "E9"],
	["E9", "55", "FF"],
	["BD", "FF", "BD"],
	["7A", "55", "7A"]]
	
chave1 = ["E7", "55", "E9"]
chave2 = ["55", "7A", "7A"]
chave3 = ["7A", "7A", "E9"]

resposta = [[0,0], [3,0], [3,2], [0,2], [0,1], [1,1], [1,0]]
posições   = [[55], [7A], [7A]**, [E9]***,[E7], [55], [E9]*]

OBS:
* = Fechou chave1
** = Fechou chave2
*** = Fechou chave3
