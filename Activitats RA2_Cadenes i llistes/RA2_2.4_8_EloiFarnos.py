# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció:Escriu una funció que elimini tots els espais d'una cadena.
# Especificacions d'entrada: una cadena de text amb espais.
try:
    cadena=input("Introdueix una cadena amb espais: ")

    def eliminar_espais(cadena):
        return cadena.replace(" ", "")

    print("La cadena sense espais és:", eliminar_espais(cadena))
except Exception as e:
    print("S'ha produït un error:", e)


