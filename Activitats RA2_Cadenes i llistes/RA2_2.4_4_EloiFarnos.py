# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).
# Especificacions d'entrada: Una paraula introduïda per l'usuari.
try:
    paraula= input("Introdueix una paraula: ")
    if paraula == paraula[::-1]:
        print("La paraula és un palíndrom.")
    else:
        print("La paraula no és un palíndrom.")
except Exception as e:
    print("S'ha produït un error:", e)