# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 30/09/2026
# Versió: 1.0
#
# Descripció: Demana una frase i una paraula que vulguis substituir i després substitueix-la per una altra paraula.
# Especificacions d'entrada: una frase, una paraula a substituir i una paraula per substituir-la.

frase= input("Posa una frase: ")
paraula_sub= input("Quina paraula vols substituir?: ")
paraula_nova= input("Per quina paraula la vols substituir?: ")
frase_nova= frase.replace(paraula_sub, paraula_nova)
print(frase_nova)
