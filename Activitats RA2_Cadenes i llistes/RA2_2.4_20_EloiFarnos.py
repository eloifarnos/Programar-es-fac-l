# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.
# Especificacions d'entrada: Una llista de paraules introduïdes per l'usuari.

try:
    llista_paraules=[input("Introdueix la paraula {}: ".format(i+1)) for i in range(5)]

    llista_vocals=[paraula for paraula in llista_paraules if paraula[0].lower() in 'aeiou']

    print("La llista de paraules que comencen per vocal és:", llista_vocals)
except Exception as e:
    print("S'ha produït un error:", e)
