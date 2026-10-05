# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana una frase, una paraula que hi aparegui i una paraula nova. Substitueix totes les aparicions de la primera paraula per la segona.
# Especificacions d'entrada: Dades de text

frase = input("Donem una frase: ") 
paraula1 = input("Donem una paraula que aparegui a la frase: ") 
paraula2 = input("Donem una paraula nova: ") 
frase_substituida = frase.replace(paraula1, paraula2) 
print("La frase amb la paraula substituïda és: " + frase_substituida) 
