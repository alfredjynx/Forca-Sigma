# Forca-Sigma

## Funcionamento do BotSigma

Nosso bot funciona por meio de filtros, uma string e uma lista. Essas filtragens são implementadas por meio de algumas funções:

#### Inicialização 

Na inicialização nós temos uma variável de classe e duas variáveis prórpias do objeto.

* Variável Global: Lista completa de palavras. 

* Palavra Atual (self.current_word): Uma string que é inicializada como espaços vazios ("_") com o mesmo tamanho da palavra do `JogoDeForca()`. 

* Letras Tentadas (self.letras_tentadas): lista com as palavras que são chutadas pelo algoritmo.

#### Funções

Utilizamos os seguintes funções nossa implementação:

* Filtro de Palavras Possíveis( filtra_palavras(self, palavra_secreta)): filtrar a lista de todas as palavras para que elas contenham os caracteres nas posições exatas dos caracteres da palavra atual (self.current_word). 

* Letra com Maior Frequência (letra_com_maior_frequencia(self)): devolve a letra não chutada (não está presente nas letras tentadas) com maior frequência dentro das palavras possíveis. 

* Jogar (jogar(self, jogo)): Se passa um "jogo" da classe `JogoDeForca()`. A palavra atual é inicializada como um sequência de espaços vazios ("_") e uma variável de objeto `self.lista` é criada, contendo uma lista com todas as palavras do mesmo tamanho da escolhida pelo `JogoDeForca`. Vai se chamando as funções, adicionando letras na lista de tentativas, filtrando as palavras possíveis conforme vamos descobrindo novas informações e completando a palavra atual (self.current_word). O loop termina quando completamos uma palavra (self.current_word não possui espaços vazios) e chutamos ela, quando apenas há uma possibilidade de palavra (self.lista tem tamanho 1) e chutamos ela, quando não há nova letra com maior frequência ou quando se terminam as tentativas do jogador. 

Nosso Bot, essencialmente, sempre chuta a letra com maior frequência dentro das possibilidades que são coerentes com as informações que lhe são dadas. 

#### Funcionamento - Exemplo Descrito

Um exemplo seria um jogo que tem uma palavra com 5 letras (a palavra sorteada foi "sorte"). 

Não sabemos qual é a palavra e não temos nenhuma letra que ela possui, mas chutamos a letra com maior frequência dentro de palavras com 5 letras. Vamos supor que essa letra seria "e". Ao chutar "e" recebemos do `JogoDeForca` uma lista com a posição dessa letra na palavra, nesse caso a letra está na palavra então recebemos uma lista completa e não perdemos nenhuma vida. Adicionamos a letra no local exato dela na palavra atual (self.current_word) e filtramos a lista de palavras para que ela apenas possua palavras que terminem em "e". Rodamos de novo a função de letra com maior frequência, que apenas retorna uma letra que não foi chutada, e tentamos novamente. 

Esse é o loop básico da função. 


### Acurácia

A última célula do `demo.py` roda 100 vezes 100 iterações do robô, e nos trás uma acurácia média em forma da porcentagem de vitória, ou seja, a porcentagem de vezes que o robô chega no resultado correto. 

O resultado atual da célula (pois ela muda cada vez que você a executa) está com uma acurácia média de 90%, um resultado excelente. 