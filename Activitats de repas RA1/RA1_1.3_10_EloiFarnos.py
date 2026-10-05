# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana tres notes, que poden tenir decimals, i mostra’n la mitjana.
# Especificacions d'entrada: Dades numèriques decimals.

a=float(input("Donem la primera nota: "))
b=float(input("Donem la segona nota: "))
c=float(input("Donem la tercera nota: "))
mitjana=(a+b+c)/3
print("La mitjana de les tres notes és: " + str(mitjana))
