# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10.
# Especificacions d'entrada: numero enter per generar la taula de multiplicar
numero = int(input("Introdueix un nombre enter: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
