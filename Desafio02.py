#2. Desafio: Limpeza de Dados de Estoque (Intermediário - Pandas)Na logística, 
# os dados raramente vêm limpos. 
# Vamos simular uma planilha de estoque com problemas.
# O que fazer: Crie um DataFrame com as colunas: Produto, Quantidade e Preço_Unitario.
# Requisitos:Insira propositalmente alguns valores nulos (NaN) e linhas duplicadas.
# Use o Pandas para remover as duplicatas.
# Substitua os valores nulos na Quantidade por 0.
# Crie uma nova coluna chamada Valor_Total_Estoque ($Quantidade \times Preco\_Unitario$).
# Dica: Explore os métodos .dropna(), .fillna() e .duplicated().

import pandas as pd


def limpeza_dados (filename:str):
    try:
        df_csv = pd.read_csv(filename, sep=",")
        df_csv = df_csv.fillna(0) # remover NaN
        df_limpa = df_csv.drop_duplicates()
        return df_limpa
    
    except FileNotFoundError:
        print(f"O filename {filename} não foi encontrado")    
        return None
    
    
# --- Bloco interativo ---
if __name__ == "__main__":
    print("Dataframe gerado via txt")
    print("-"*50)
file = input("Digite o nome do arquivo? ")
resultado = limpeza_dados(file)

print(f"\nResultado:")
print(resultado)



