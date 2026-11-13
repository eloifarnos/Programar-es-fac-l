# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Utilitzant el range(),  escriu un programa que generi una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari. 
# Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter.

# Especificacions d'entrada: Número enter introduït per l'usuari

try:
    num = int(input("Introdueix un número enter: "))
    for i in range(num + 1):
        print(i, end=" ")
    print()
except ValueError:
    print("Error: Si us plau, introdueix un número enter vàlid.")
