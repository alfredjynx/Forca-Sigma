import requests
from copy import deepcopy

class BotSigma:

    lista_de_palavras = []

    def __init__(self, tamanho_palavra):

        self.tamanho_palavra = tamanho_palavra
        self.current_word = "_" * tamanho_palavra

        self.letrar_tentadas = []

        self.lista = [pal for pal in BotSigma.lista_de_palavras if len(pal) == tamanho_palavra]
        

    def filtra_palavras(self, palavra_secreta):
        

        # dictionary with the letters and their frequency
        frequencia_letras_palavra_secreta = {}
        for letter in palavra_secreta:
            if letter in frequencia_letras_palavra_secreta:
                frequencia_letras_palavra_secreta[letter] += 1
            elif letter != "_":
                frequencia_letras_palavra_secreta[letter] = 1
        

        # remove word that letters not in the same position as the secret word
        for palavra in self.lista:
            for idx in range(len(palavra_secreta)):
                if palavra_secreta[idx] != "_":
                    if palavra_secreta[idx] != palavra[idx]:
                        self.lista.remove(palavra)
                        break

            
        for palavra_da_lista in self.lista:
            freq_palavra_lista = {}

            for letter in palavra_da_lista:
                if letter in freq_palavra_lista:
                    freq_palavra_lista[letter] += 1
                else:
                    freq_palavra_lista[letter] = 1

            
            for letra in frequencia_letras_palavra_secreta.keys():
                if letra in freq_palavra_lista:
                    if frequencia_letras_palavra_secreta[letra] != freq_palavra_lista[letra]:
                        self.lista.remove(palavra_da_lista)
                        break


        return self.lista
    
    def letra_com_maior_frequencia(self):

        dict_letras = {}

        for palavra in self.lista:
            for letra in palavra:
                if letra not in self.letrar_tentadas:
                    if letra in dict_letras:
                        dict_letras[letra] += 1
                    else:
                        dict_letras[letra] = 1

        if not dict_letras:
            return None
        # get the letter with the highest frequency
        letter = max(dict_letras, key=dict_letras.get)

        return letter

import random


class JogoDeForca:

    lista_de_palavras = []

    def __init__(self):
        # import requests
        # url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
        # r = requests.get(url, allow_redirects=True)
        # if r.status_code==200:
        #     self.content = str(r.content.decode()).split('\n')
        # else:
        #     print("Erro: ", r.status_code)

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
            

vitorias = 0

lista = []
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
r = requests.get(url, allow_redirects=True)
if r.status_code==200:
    lista = str(r.content.decode()).split('\n')
    print("Lista de palavras carregada com sucesso!")
    
else:
    print("Erro: ", r.status_code)

BotSigma.lista_de_palavras = lista
JogoDeForca.lista_de_palavras = lista


n_jgos = 1

for i in range(n_jgos):
    jogo = JogoDeForca()
    new_game = jogo.novo_jogo()
    bot = BotSigma(new_game)

    # cortar palavras sem o mesmo tamanho

    while jogo.vidas > 0:


        if "_" not in bot.current_word:
            if jogo.tentar_palavra(bot.current_word):
                vitorias += 1
                break

        letra_com_maior_frequencia = bot.letra_com_maior_frequencia()
        print("----------------------------------")
        print("Vidas: ", jogo.vidas)
        print(bot.current_word)
        print("Letras tentadas: ", bot.letrar_tentadas)
        print("Letra com maior frequência: ", letra_com_maior_frequencia)
        print(bot.lista)

        
        # If letra_com_maior_frequencia is None, break the loop
        if letra_com_maior_frequencia is None:
            break

        
        posicoes_letras = jogo.tentar_letra(letra_com_maior_frequencia)

        if posicoes_letras == False:
            break

        for indice_letra in posicoes_letras:
            bot.current_word = bot.current_word[:indice_letra] + letra_com_maior_frequencia + bot.current_word[indice_letra+1:] 
        
        # print(bot.current_word)
        
        bot.letrar_tentadas.append(letra_com_maior_frequencia)
        # print(len(bot.lista))
        bot.filtra_palavras(bot.current_word)

    
print("Vitórias: ", vitorias)
print("Derrotas: ", n_jgos-vitorias)
print("Porcentagem de vitórias: ", vitorias/n_jgos*100, "%")

