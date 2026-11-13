# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Fes un script que concateni dues cadenes separades per un guió "-".
# Especificacions d'entrada: Dues cadenes de text.

try:
    cadena1=input("Introdueix la primera cadena: ")
    cadena2=input("Introdueix la segona cadena: ")

    resultat=cadena1 + "-" + cadena2

    print("La cadena concatenada és:", resultat)
except Exception as e:
    print("S'ha produït un error:", e)