# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre.
# Pista: Utilitza range(1, n+1) per generar la seqüència i la funció sum() per obtenir la suma.
# Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada: Número enter positiu introduït per l'usuari

try:
    num = int(input("Introdueix un número enter positiu: "))
    if num < 1:
        raise ValueError("El número ha de ser positiu.")
    suma = sum(range(1, num + 1))
    print(f"La suma dels nombres des de 1 fins a {num} és: {suma}")
except ValueError as e:
    print(f"Error: {e}")
    
