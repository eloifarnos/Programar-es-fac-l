# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Fes un programa que elimini els duplicats d'una llista.
# Especificacions d'entrada: Una llista de nombres amb duplicats.

try:
    llista=[int(input("Introdueix el nombre {}: ".format(i+1))) for i in range(5)]

    def eliminar_duplicats(llista):
        return list(set(llista))

    print("La llista sense duplicats és:", eliminar_duplicats(llista))
except Exception as e:
    print("S'ha produït un error:", e)
