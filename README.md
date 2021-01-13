## Resolução de Algoritmo

Algoritmo do Coding Dojo baseado no minigame "Breach Protocol" de CP2077.

RESOLUÇÃO DE ALGORITMO.
### Algoritmo e suas regras

- Geração da Matriz: 
	- A matriz deve ter elementos em posições aleatórias;
	- Toda matriz gerada deve ter três chaves para sua resolução;
	- Toda matriz gerada deve possuir chaves válidas para resolução;
	- Cada chave possui uma série de elementos;
	- A resolução de uma chave ocorre quando todos os elementos são marcados;
	- Um elemento é marcado quando sua posição é exposta pelo requerente;
	- Quando marcado, o elemento em sua matriz recebe o valor de zero, e não poderá ser usado novamente.
	- A ordem da resolução das chaves não é importante;
	- A ordem dos elementos pertencentes as chaves devem ser preenchidos em ordem;
	- A chave reinicia ao primeiro valor, caso seu preenchimento seja interrompido por um código distinto de sua ordem;
	- Caso os elementos de duas ou mais chaves sigam a mesma ordem, eles serão preenchidos em conjunto, respeitando a regra anterior.

- Regra de movimento para resolução:
	- O primeiro movimento sempre deve ocorrer na primeira linha (horizontal;
	- O próximo movimento deve ocorrer na coluna (vertical) do index atualmente marcado;
	- O movimento seguinte seguirá na linha (horizontal) do index da coluna marcada anteriormente;
	- Assim sucessivamente até as três chaves serem preenchidas.
    
## EXEMPLO:
```
elementos = ["7A", "1C", "E7", "BD", "E9", "55", "FF"]

matriz = [
	["55", "E7", "E9"],
	["E9", "55", "FF"],
	["BD", "FF", "BD"],
	["7A", "55", "7A"]]
	
chave1 = ["E7", "55", "E9"]
chave2 = ["55", "7A", "7A"]
chave3 = ["7A", "7A", "E9"]
```
- resposta = [[0,0], [3,0], [3,2], [0,2], [0,1], [1,1], [1,0]]
- elementos = [[55], [7A], [7A], [E9],[E7], [55], [E9]*]
