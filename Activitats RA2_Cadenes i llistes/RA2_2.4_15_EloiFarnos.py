# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Crea una llista amb noms i ordena'ls alfabèticament.
# Especificacions d'entrada: Una llista de noms introduïts per l'usuari.

try:
    llista_noms=[input("Introdueix el nom {}: ".format(i+1)) for i in range(5)]

    llista_noms.sort()

    print("La llista de noms ordenada alfabèticament és:", llista_noms)
except Exception as e:
    print("S'ha produït un error:", e)
