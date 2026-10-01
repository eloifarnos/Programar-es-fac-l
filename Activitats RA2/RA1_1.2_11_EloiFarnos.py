# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 30/09/2026
# Versió: 1.0
#
# Descripció: Demana una frase que contingui espais al principi i al final i elimina aquests espais.
# Especificacions d'entrada: una frase amb espais al principi i al final.

frase= input("Posa una frase amb espais al principi i al final: ")
longitud = len(frase)
frase_nova= frase[1:longitud-1]
print(frase_nova)
