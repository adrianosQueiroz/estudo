 # Desafio 3: Conversor de Temperaturas
 # Escreva um programa que receba uma temperatura em graus
 # Celsius e a converta para Fahrenheit. 
 # A fórmula é: $F = (C * 1.8) + 32$.


def conv_fahrenheit (valor: int)->int:
    '''
    Ferramenta para conversão de temperatura.    
    '''
    resultado = (valor * 1.8) + 32
    return resultado

# --- Bloco interativo ---
if __name__ == "__main__":
    print("Aplicação de conversão de temperatura")
    print("-"*50)
file = int(input("Digite o valor que deve ser convertido para Fahrenheit: "))
resultado = conv_fahrenheit(file)

print(f"\nResultado:")
print(resultado)


