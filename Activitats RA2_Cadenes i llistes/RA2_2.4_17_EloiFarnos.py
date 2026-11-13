# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Demana una paraula i guarda cada lletra en una llista.
# Especificacions d'entrada: Una paraula introduïda per l'usuari.

try:
    paraula=input("Introdueix una paraula: ")

    llista_lletres=list(paraula)

    print("La llista de lletres és:", llista_lletres)
except Exception as e:
    print("S'ha produït un error:", e)
