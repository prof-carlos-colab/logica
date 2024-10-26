# Implemente um algoritmo que, usando recursividade,
# receba um número como parâmetro e some todos os números
# de zero até o número informado.

import os
os.system("cls || clear")

def somar_numero(numero):
    if numero == 0:
        return 0
    else:
        print(f"{numero} + {numero - 1}")
        return numero + somar_numero(numero - 1)
    
print(f"Soma: {somar_numero(5)}")