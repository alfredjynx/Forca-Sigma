import requests
from copy import deepcopy

def obter_palavras():

    url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
    r = requests.get(url, allow_redirects=True)
    if r.status_code==200:
        print("Lista de palavras carregada com sucesso!")
        return str(r.content.decode()).split('\n')
        
    else:
        print("Erro: x", r.status_code)

class BotSigma:

    lista_de_palavras = []

    def __init__(self ):
        self.current_word = ""
        self.letras_tentadas = []

    def filtra_palavras(self, palavra_secreta):

        filtered_list = []
        for word in self.lista:
    
            match = True
            for i, letter in enumerate(palavra_secreta):
                if letter != '_' and letter != word[i]:
                    match = False
                    break
            if match:
                filtered_list.append(word)

        self.lista = filtered_list
    
    def letra_com_maior_frequencia(self):

        dict_letras = {}

        for palavra in self.lista:
            for letra in palavra:
                if letra not in self.letras_tentadas:
                    if letra in dict_letras:
                        dict_letras[letra] += 1
                    else:
                        dict_letras[letra] = 1

        if not dict_letras:
            return None
        # get the letter with the highest frequency
        return max(dict_letras, key=dict_letras.get)
    

    
    def jogar(self, jogo):

        n = jogo.novo_jogo()
        
        self.current_word = "_" * n
        self.lista = [pal for pal in BotSigma.lista_de_palavras if len(pal) == n]

        while jogo.vidas > 0:

            if "_" not in self.current_word:
                if jogo.tentar_palavra(self.current_word):
                    
                    return True
            
            if len(self.lista) == 1:
                if jogo.tentar_palavra(self.lista[0]):
                    return True

            letra_com_maior_frequencia = self.letra_com_maior_frequencia()
        
        
            # If letra_com_maior_frequencia is None, break the loop
            if letra_com_maior_frequencia is None:
                break

            
            posicoes_letras = jogo.tentar_letra(letra_com_maior_frequencia)

            if posicoes_letras == False:
                break

            for indice_letra in posicoes_letras:
                self.current_word = self.current_word[:indice_letra] + letra_com_maior_frequencia + self.current_word[indice_letra+1:] 
            
            
            self.letras_tentadas.append(letra_com_maior_frequencia)
            
            self.filtra_palavras(self.current_word)
        
        return False

        
import random


class JogoDeForca:

    lista_de_palavras = []

    def __init__(self):
        self.content = JogoDeForca.lista_de_palavras
    
    def novo_jogo(self, vidas=5):
        self.vidas = vidas
        self.palavra = random.choice(self.content)
        return len(self.palavra)

    def tentar_letra(self, letra):
        if self.vidas > 0:
            if letra in self.palavra:
                return [idx for idx in range(len(self.palavra)) if self.palavra[idx]==letra]
            else:
                self.vidas -= 1
                if self.vidas == 0:
                    print("Fim de jogo!")
                    return False
                else:
                    return []
        
    def tentar_palavra(self, palavra):
        if self.vidas > 0:
            if self.palavra == palavra:
                print ("Ganhou!")
                return True
            else:
                self.vidas = 0
                print("Fim de jogo!")
                return False
            


lista = obter_palavras()

BotSigma.lista_de_palavras = lista
JogoDeForca.lista_de_palavras = lista

n_jgos = 100
vitorias = 0


for i in range(n_jgos):
    
    jogo = JogoDeForca()
    # new_game = jogo.novo_jogo()
    
    bot = BotSigma()

    # cortar palavras sem o mesmo tamanho
    ganhou = bot.jogar(jogo)
    if ganhou:
        vitorias += 1

    
        

    
print("Vitórias: ", vitorias)
print("Derrotas: ", n_jgos-vitorias)
print("Porcentagem de vitórias: ", vitorias/n_jgos*100, "%")

