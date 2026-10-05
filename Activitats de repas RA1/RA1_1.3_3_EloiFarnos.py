# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Afegeix un comentari a cada línia per explicar què fa.
# Especificacions d'entrada: Dades numèriques i de text.

preu = float(input("Preu: ")) # Demana l'input del preu i el converteix a float
 quantitat = int(input("Quantitat: ")) # Demana l'input de la quantitat i el converteix a int
 total = preu * quantitat # Calcula el total multiplicant preu per quantitat
 print("Total: " + str(total) + " euros") # Mostra el total en format de text