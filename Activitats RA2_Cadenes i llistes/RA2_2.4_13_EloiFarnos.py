# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Escriu una funció que sumi tots els nombres d'una llista.
# Especificacions d'entrada: Una llista de nombres.

try:
    llista=[int(input("Introdueix el nombre {}: ".format(i+1))) for i in range(5)]

    def sumar_llista(llista):
        return sum(llista)

    print("La suma dels nombres de la llista és:", sumar_llista(llista))
except Exception as e:
    print("S'ha produït un error:", e)
