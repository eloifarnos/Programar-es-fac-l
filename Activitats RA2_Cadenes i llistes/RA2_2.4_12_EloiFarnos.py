# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari 5 paraules i emmagatzema-les en una llista.
# Especificacions d'entrada: Cinc paraules introduïdes per l'usuari.

try:
    llista_paraules=[input("Introdueix la paraula {}: ".format(i+1)) for i in range(5)]

    print("La llista de paraules és:", llista_paraules)
except Exception as e:
    print("S'ha produït un error:", e)
