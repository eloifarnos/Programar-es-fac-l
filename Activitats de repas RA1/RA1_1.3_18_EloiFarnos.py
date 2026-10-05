# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana una frase i mostra la frase original, la frase en majúscules, la frase en minúscules i el nombre de caràcters, incloent-hi els espais.
# Especificacions d'entrada: Dades de text

frase = input("Donem una frase: ")
print("La frase original és: " + frase)
print("La frase en majúscules és: " + frase.upper())
print("La frase en minúscules és: " + frase.lower()) 
len_frase = len(frase) 
print("El nombre de caràcters, incloent-hi els espais, és: " + str(len_frase))
