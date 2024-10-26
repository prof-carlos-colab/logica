import os
import time
os.system("cls || clear")

# Função.
def contagem_regressiva(numero):
    if numero < 0:
        return
    print(numero)
    time.sleep(2)
    # Chamada recursiva.
    contagem_regressiva(numero -1) 

# Código principal.
print("Contagem regressiva...")
contagem_regressiva(5) # Chamada da função.
print("=== FIM ===")
