# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana un nombre enter de minuts i converteix-lo en hores completes i minuts restants. Utilitza // i %.
# Especificacions d'entrada: Dades numèriques enters.

minuts = int(input("Donem un nombre enter de minuts: "))
hores = minuts // 60
minuts_restants = minuts % 60
print("tens " + str(hores) + " hores i " + str(minuts_restants) + " minuts.")
