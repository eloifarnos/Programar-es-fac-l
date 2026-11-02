# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari una frase i compta quantes vocals conté.
# Especificacions d'entrada: Cadena de text per comptar les vocals

frase = input("Introdueix una frase: ")
vocals = "aeiouàèéíïòóúü"
comptador = 0

for caracter in frase.lower():
    if caracter in vocals:
        comptador += 1

print("Nombre de vocals:", comptador)
