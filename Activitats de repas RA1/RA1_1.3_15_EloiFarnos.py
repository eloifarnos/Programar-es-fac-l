# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana una paraula i mostra la paraula original i la paraula al revés, amb les etiquetes corresponents.
# Especificacions d'entrada: Dades de text

paraula = input("Donem una paraula: ") # Demana l'input de la paraula
paraula_reves = paraula[::-1] 
print("La paraula original és: " + paraula) # Mostra la paraula original
print("La paraula al revés és: " + paraula_reves) # Mostra la paraula al reves
