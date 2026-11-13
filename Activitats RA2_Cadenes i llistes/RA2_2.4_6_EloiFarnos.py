# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 9/11/2026
# Versió: 1.0
#
# Descripció: Demana una cadena i mostra la primera i l'última lletra.   
# Especificacions d'entrada: Una cadena de text introduïda per l'usuari.

try:
    cadena = input("Introdueix una cadena de text: ")
    if len(cadena) > 0:
        primera_lletra = cadena[0]
        ultima_lletra = cadena[-1]
        print(f"La primera lletra és: {primera_lletra}")
        print(f"L'última lletra és: {ultima_lletra}")
    else:
        print("La cadena està buida.")
except Exception as e:
    print("S'ha produït un error:", e)  