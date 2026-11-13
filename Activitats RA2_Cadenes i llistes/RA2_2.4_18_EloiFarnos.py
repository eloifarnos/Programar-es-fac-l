# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Escriu una funció que retorni la llista al revés (sense reverse()).
# Especificacions d'entrada: Una llista de nombres.

try:
    llista=[int(input("Introdueix el nombre {}: ".format(i+1))) for i in range(5)]

    def invertir_llista(llista):
        return llista[::-1]

    print("La llista invertida és:", invertir_llista(llista))
except Exception as e:
    print("S'ha produït un error:", e)
