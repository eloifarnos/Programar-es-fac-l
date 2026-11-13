# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un nombre enter i imprimeix tots els nombres parells des de 0 fins a aquest nombre.
# Pista: Utilitza range(0, n+1, 2) per generar nombres parells.​
#Excepció:  Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada: Número enter positiu introduït per l'usuari

try:
    num = int(input("Introdueix un número enter positiu: "))
    if num < 0:
        raise ValueError("El número ha de ser positiu.")
    print(f"Nombres parells des de 0 fins a {num}:")
    for i in range(0, num + 1, 2):
        print(i, end=" ")
    print()
except ValueError as e:
    print(f"Error: {e}")
