# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari una cadena de text i mostra-la invertida.
# Especificacions d'entrada: Cadena de text per invertir

text = input("Introdueix una cadena de text: ")
invertit = ""

for caracter in text:
    invertit = caracter + invertit

print("Text invertit:", invertit)
