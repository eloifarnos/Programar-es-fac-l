# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana una frase amb espais al principi i al final. Elimina aquests espais, conservant els espais interiors, i mostra el resultat entre claudàtors.
# Especificacions d'entrada: Dades de text

frase = input("Donem una frase amb espais al principi i al final: ") # Demana l'input de la frase
len_frase = len(frase) # Calcula la longitud de la frase
print(frase[1:len_frase-1]) # Mostra la frase amb els espais eliminats i entre claudàtors
