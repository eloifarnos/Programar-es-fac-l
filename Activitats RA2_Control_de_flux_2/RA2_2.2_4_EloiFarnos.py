# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Genera un número aleatori entre 1 i 100. Demana a l'usuari que endevini el número, donant pistes de "massa alt" o "massa baix" fins que l'encerti.
# Especificacions d'entrada: Generar un número aleatori i demanar a l'usuari que endevini el número amb pistes.

import random

secret = random.randint(1, 100)

while True:
    intent = int(input("Endevina el nombre entre 1 i 100: "))

    if intent > secret:
        print("massa alt")
    elif intent < secret:
        print("massa baix")
    else:
        print("L'has encertat!")
        break
