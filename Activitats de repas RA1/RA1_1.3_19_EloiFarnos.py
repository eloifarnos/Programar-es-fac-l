# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana un nom d’usuari que pot contenir espais al principi i al final i lletres majúscules. Elimina els espais dels extrems, converteix-lo a minúscules i mostra el nom resultant i la seva longitud.
# Especificacions d'entrada: Dades de text

nom_usuari = input("Introdueix un nom d'usuari: ")
nom_usuari = nom_usuari.strip().lower()
print("El nom d'usuari resultant és: " + nom_usuari)
print("La longitud del nom d'usuari és: " + str(len(nom_usuari)))
