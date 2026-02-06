# O que fazer: Crie um script que receba uma lista de números.

# Requisitos:
# Calcule a média de tempo de entrega.
# Identifique a maior e a menor duração.
# Conte quantas entregas ficaram acima de 24 horas (atraso).
# Dica: Use as funções sum(), len(), max() e um loop for com if.

import numpy as np

lista = np.random.randint(1, 100, 20)


# Todas as entregas:
print(lista)
#print(f"A qtde de entregas foi de {len(lista)}")

entregas_atrasadas = [i for i in lista if i > 24]
print(f"A qtde de entregas superiores a 24 h foi de {len(entregas_atrasadas)}")



# Calcule a média de tempo de entrega:
media_tempo = np.mean(lista)
print(f"A média de tempo de entrega foi de {media_tempo:.0f}")

# Identifique a maior e a menor duração:
menor_tempo = np.min(lista)
maior_tempo = np.max(lista)
print(f"O menor tempo de entrega foi de {menor_tempo}")

print(f"O maior tempo de entrega foi de {maior_tempo}")













