# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Utilitzant el range() escriu un programa que mostri la taula de multiplicar d'un número introduït per l'usuari.
# Pista: Utilitza range(1, 11) per generar els multiplicadors del 1 al 10.​
# Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter.

# Especificacions d'entrada: Número enter introduït per l'usuari

try:
    num = int(input("Introdueix un número enter: "))
    print(f"Taula de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Error: Si us plau, introdueix un número enter vàlid.")
