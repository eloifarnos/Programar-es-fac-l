# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana una paraula i mostra-la quatre vegades seguides sense espais i, en una altra línia, tres vegades separades per espais, sense espai al final. Utilitza * almenys una vegada.
# Especificacions d'entrada: Dades de text

paraula = input("Donem una paraula: ") # Demana l'input de la paraula
print("La paraula repetida quatre vegades seguides és: " + paraula * 4)
print("La paraula repetida tres vegades separades per espais és: " + (paraula + " ") * 3) 
