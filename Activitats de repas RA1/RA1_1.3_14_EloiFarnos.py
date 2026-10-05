# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció:Demana el nom i el cognom, cadascun format per una sola paraula sense accents. Construeix un correu en minúscules amb el format nom.cognom@alumnes.cat.
# Especificacions d'entrada: Dades de text

nom = input("Quin és el teu nom? ") # Demana l'input del nom
cognom = input("Quin és el teu cognom? ") # Demana l'input del cognom
print("El teu correu és: " + nom + "." + cognom+ "@alumnes.cat") # Mostra el correu construït amb el format especificat