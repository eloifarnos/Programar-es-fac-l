# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Escriu una funció que reverteixi una cadena.
# Especificacions d'entrada: Una cadena de text introduïda per l'usuari.

try:
    cadena = input("Introdueix una cadena de text: ")
    cadena_revertida = cadena[::-1]
    print("La cadena revertida és:", cadena_revertida)
except Exception as e:
    print("S'ha produït un error:", e)
