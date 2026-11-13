# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Demana una cadena i compta quantes vegades apareix una lletra concreta.
# Especificacions d'entrada: Dades que rep el programa

try:
    cadena=input("Introdueix una cadena: ")
    lletra=input("Introdueix una lletra: ")

    comptador=0

    for i in cadena:
        if i==lletra:
            comptador+=1

    print("La lletra", lletra, "apareix", comptador, "vegades a la cadena.")
except Exception as e:
    print("S'ha produït un error:", e)