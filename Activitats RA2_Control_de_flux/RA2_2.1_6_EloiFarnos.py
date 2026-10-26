# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Fes un programa que demani una lletra i et digui si es vocal o consonant.
# Especificacions d'entrada: Una lletra

lletra = input("Introdueix una lletra: ")
vocals = "aeiou"
if (lletra in vocals):
    print("La lletra és una vocal.")
else:
    print("La lletra és una consonant.")

    #En aquest programa el que fem es demanar una lletra a el usuari i comprovem si es bocal o no fent una string en totes les vocals i que miri si la lletra que eh ficat l'usuari es repeteix a el string i per tant diem que es una vocal.
