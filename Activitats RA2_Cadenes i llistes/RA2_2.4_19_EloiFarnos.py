# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Fes una llista de números i multiplica tots els elements per 2.
# Especificacions d'entrada: Una llista de números enters.

try:
    llista=[int(input("Introdueix el nombre {}: ".format(i+1))) for i in range(5)]

    def multiplicar_per_dos(llista):
        return [num*2 for num in llista]

    print("La llista amb els elements multiplicats per 2 és:", multiplicar_per_dos(llista))
except Exception as e:
    print("S'ha produït un error:", e)
