# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Llegeix una cadena de l'usuari i mostra-la tota en majúscules.
# Especificacions d'entrada: Una cadena de text introduïda per l'usuari.
try:
    cadena = input("Introdueix una cadena de text: ")
    print(cadena.upper())
except Exception as e:
    print("S'ha produït un error:", e)
