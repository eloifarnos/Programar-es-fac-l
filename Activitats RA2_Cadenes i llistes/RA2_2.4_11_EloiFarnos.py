# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Crea una llista amb 5 nombres i imprimeix el major i el menor.
# Especificacions d'entrada: Una llista de 5 nombres.

try:
    llista=[int(input("Introdueix el nombre {}: ".format(i+1))) for i in range(5)]

    major=max(llista)
    menor=min(llista)

    print("El nombre major és:", major)
    print("El nombre menor és:", menor)
except Exception as e:
    print("S'ha produït un error:", e)
