from obter_palavras import obter_palavras

class BotSigma:

    # lista de palavras - totais
    lista_de_palavras = obter_palavras()

    # inicialização - guardam a palavra atual (apenas as letras obtidas) e as letras que foram tentatadas
    def __init__(self ):
        self.current_word = ""
        self.letras_tentadas = []

    # filtragem de palavras possíveis de serem a palavras misteriosa
    def filtra_palavras(self, palavra_secreta):

        # lista de palavras filtradas, inicialização vazia
        filtered_list = []

        # percorrendo a lista de palavras completa
        for word in self.lista:
            
            # match - a palavra é possível de ser a escolhida pelo algoritmo da forca
            match = True

            # percorre cada letra da palavra, assim como seu índice
            for i, letter in enumerate(palavra_secreta):

                # se a letra não for um espaço vago ("_") e não for a letra correspondente na palavra, a palavra não é possível de ser a escolhida
                if letter != '_' and letter != word[i]:
                    match = False
                    break
            
            # coloca a palavra na lista de palavras possíveis se ela sobreviveu a checagem superior
            if match:
                filtered_list.append(word)

        # troca a lista de todas as palavras pela lista filtrada que apenas possui palavras possíveis de serem a escolhida tendo em mente as informações que foram dadas
        self.lista = filtered_list
    
    # devolve a letra com maior frequência das palavras na lista de palavras
    def letra_com_maior_frequencia(self):

        # dicionário de frequência de letras
        dict_letras = {}

        # percorre a lista de palavras
        for palavra in self.lista:
            # percorre as letras em cada palavra
            for letra in palavra:

                # se a letra ainda não foi tentada
                if letra not in self.letras_tentadas:

                    # se a letra já existir no dicionário, adicionar 1 na sua frequência
                    if letra in dict_letras:
                        dict_letras[letra] += 1
                    # se não há a letra o dicionário, adiciona ela com 1 de frequência 
                    else:
                        dict_letras[letra] = 1


        if not dict_letras:
            return None
        
        # pegar a letra com a maior frequência
        return max(dict_letras, key=dict_letras.get)
    

    
    def jogar(self, jogo):

        # enviar a classe de JogoDeForca no jogo
        n = jogo.novo_jogo()
        
        # inicialização da palavra como sendo apenas de espaços vazios
        self.current_word = "_" * n

        # lista de palavras inicializada com palavras do mesmo tamanho da selecionada pelo JogoDeForca
        self.lista = [pal for pal in BotSigma.lista_de_palavras if len(pal) == n]

        # enquanto o jogador ainda possuir vidas
        while jogo.vidas > 0:

            # se uma palavra for completa, chutar ela
            if "_" not in self.current_word:
                if jogo.tentar_palavra(self.current_word):
                    return True
            
            # se há apenas uma palavra possível na lista, tentar essa palavra
            if len(self.lista) == 1:
                if jogo.tentar_palavra(self.lista[0]):
                    return True

            # pega letra com maior frequência dentro das possibilidades que ainda não foi tentada
            letra_com_maior_frequencia = self.letra_com_maior_frequencia()
        
            # se todas as letras já foram chutadas, quebrar o while
            if letra_com_maior_frequencia is None:
                break

            # chutar a letra com base na frequência
            posicoes_letras = jogo.tentar_letra(letra_com_maior_frequencia)

            # se acabar as vidas, quebrar o loop
            if posicoes_letras == False:
                break
            
            # atualizar a palavra atual
            for indice_letra in posicoes_letras:
                self.current_word = self.current_word[:indice_letra] + letra_com_maior_frequencia + self.current_word[indice_letra+1:] 
            
            # adicionar a letra que acaba de ser tentada na lista de letras tentatadas
            self.letras_tentadas.append(letra_com_maior_frequencia)
            
            # refiltragem de palavras possíveis com base nas novas informações
            self.filtra_palavras(self.current_word)
        
        # se o while acabar, retornar False (agente não conseguiu chegar na palavra correta)
        return False

