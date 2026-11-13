# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció: Crea un programa que divideixi una frase en paraules i les mostri una per una.
# Especificacions d'entrada: frase amb paraules separades per espais.

try:
    frase=input("Introdueix una frase: ")

    paraules=frase.split()

    print("Les paraules de la frase són:")
    for paraula in paraules:
        print(paraula)
except Exception as e:
    print("S'ha produït un error:", e)
