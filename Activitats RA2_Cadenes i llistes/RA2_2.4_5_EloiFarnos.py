# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Substitueix totes les lletres "a" per "@" en una frase donada.
# Especificacions d'entrada: Una frase introduïda per l'usuari.

try:
    frase = input("Introdueix una frase: ")
    frase_modificada = frase.replace("a", "@").replace("A", "@")
    print("La frase modificada és:", frase_modificada)
except Exception as e:
    print("S'ha produït un error:", e)