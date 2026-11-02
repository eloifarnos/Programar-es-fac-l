# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Calcula la suma dels primers 100 nombres enters positius (de 1 a 100) i mostra el resultat.
# Especificacions d'entrada: Calcular una suma de nombres

suma = 0

for numero in range(1, 100):
    suma += numero

print("La suma és:", suma)  
