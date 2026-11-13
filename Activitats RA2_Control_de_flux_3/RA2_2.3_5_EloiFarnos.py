# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​
# Pista:  Implementa una funció que comprovi si un nombre és primer i utilitza range(2, n+1) per iterar.​
# Excepció:  Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada: Número enter positiu introduït per l'usuari

try:
    num = int(input("Introdueix un número enter positiu: "))
    if num < 2:
        raise ValueError("El número ha de ser major o igual a 2.")
    
    def es_primer(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    print(f"Nombres primers des de 2 fins a {num}:")
    for i in range(2, num + 1):
        if es_primer(i):
            print(i, end=" ")
    print()
except ValueError as e:
    print(f"Error: {e}")
