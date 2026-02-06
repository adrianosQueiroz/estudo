# Crie um programa que receba uma lista de números (pode ser hardcoded ou via input).
# Calcule a média aritmética desses números.
# Crie uma nova lista contendo apenas os números que estão acima da média calculada.
# Exiba a média e a nova lista.


def lista_acima_media(arquivo: str)-> list:

    import pandas as pd
    import numpy as np

    # Use header=None para que o pandas não ache que o primeiro número é o título da coluna
    df = pd.read_csv(arquivo, sep=",", header=None)

    # Para converter tudo em uma lista simples de números:
    valores = df.values.flatten()

    # lista nova
    file = []
    # média
    media = np.average(valores)

    for i in valores:
        if i > media:
            file.append(int(i))

    return file

# --- Bloco interativo ---
if __name__ == "__main__":
    print("---Analisador de médias---")
    print("-"*50)
    file = input("Informe o nome do arquivo: ")
    
    resultado = lista_acima_media(file)

    print(f"\nResultado:")
    print(resultado)
    



    




