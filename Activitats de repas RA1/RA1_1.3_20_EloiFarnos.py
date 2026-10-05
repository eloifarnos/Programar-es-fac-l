# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana el nom, el cognom, l’edat, la ciutat i el cicle formatiu. Genera una fitxa amb el nom complet en majúscules, l’edat que tindrà d’aquí a un any, la ciutat, el cicle i un correu en minúscules amb el format nom.cognom@alumnes.cat. Pots donar per fet que el nom i el cognom són paraules sense espais ni accents. Utilitza + per construir els missatges.
# Especificacions d'entrada: Dades de text

nom = input("Quin es el teu nom?")
cognom = input("Quin es el teu cognom?")
edat = input("Quants anys tens?")
ciutat = input("On vius?")
cicle = input("Quin es el teu cicle formatiu?")

print("La teva fitxa és: ")
print("Nom complet: " + nom.upper() + " " + cognom.upper())
edat_futura = int(edat) + 1
print("Edat d'aquí a un any: " + str(edat_futura))
print("Ciutat: " + ciutat)
print("Cicle formatiu: " + cicle)
print("Correu: " + nom.lower() + "." + cognom.lower() + "@alumnes.cat")
