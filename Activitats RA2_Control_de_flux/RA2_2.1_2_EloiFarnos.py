# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Fes un programa que donat un número et digui si és parell o imparell.
# Especificacions d'entrada: Un número enter

numero = int(input("Introdueix un número enter: "))
parell = numero % 2
if (parell == 0):
    print("El número és parell.")
else:
    print("El número és imparell.")
#En aquest programa el que fem es demanar un numero a l'usuari i comprovem si es parell o imparell fent una operacio de modulo amb 2 i si el resultat es 0 vol dir que es parell i si no es 0 vol dir que es imparell.
