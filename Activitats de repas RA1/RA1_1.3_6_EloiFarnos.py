# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana dos nombres decimals. Mostra amb etiquetes la suma, la resta del primer menys el segon, la multiplicació i la divisió del primer entre el segon. Pots donar per fet que el segon nombre no és zero.
# Especificacions d'entrada: Dades numèriques decimals.

a=float(input("Donem un numero decimal : "))
b=float(input("Donem un altre numero decimal : "))
suma=a+b
resta=a-b
multiplicacio=a*b
divisio=a/b
print("El resultat de la suma és: " + str(suma))
print("El resultat de la resta és: " + str(resta))
print("El resultat de la multiplicació és: " + str(multiplicacio))
print("El resultat de la divisió és: " + str(divisio))
