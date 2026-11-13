# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Demana una frase i compta quantes vocals conté.
# Especificacions d'entrada: Una frase introduïda per l'usuari.
try:
    frase = input("Introdueix una frase: ")
    vocal_count = 0
    for char in frase:
        if char.lower() in "aeiou":
            vocal_count += 1
    print(f"La frase conté {vocal_count} vocals.")
except Exception as e:
    print("S'ha produït un error:", e)
