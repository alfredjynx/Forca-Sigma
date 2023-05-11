import pandas as pd

# função para obter o fundo de palavras 
def obter_palavras():
    return pd.read_csv('palavras.csv')['Palavras'].tolist()
