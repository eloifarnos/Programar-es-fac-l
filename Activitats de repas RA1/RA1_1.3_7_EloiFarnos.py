# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana el radi d’un cercle. Defineix PI = 3.1416 i calcula’n l’àrea. Fórmula: àrea = PI × radi × radi. Mostra el resultat i explica per què escrivim PI en majúscules.
# Especificacions d'entrada: Dades numèriques decimals.

PI=3.1416 # Defineix la constant PI amb el valor de 3.1416
radi=float(input("Donem el radi del cercle : ")) 
area_cercle=(PI*(radi**2)) 
print("L'àrea del cercle és: " + str(area_cercle))