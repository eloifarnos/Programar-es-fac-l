# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana el preu d’un producte sense IVA i el nombre d’unitats. Calcula i mostra l’import de la compra sense IVA, l’import de l’IVA del 21 % i el total amb IVA.
# Especificacions d'entrada: Dades numèriques decimals.

preu = float(input("Preu sense IVA: ")) 
unitats = int(input("Nombre d'unitats: "))
print("Aixo es el que val el producte sense IVA: ", preu)
preu_total = preu * unitats
print("Aixo es el que val tots els productes sense IVA: ", preu_total)
preu_iva = preu * 0.21
print("Aixo es el que val l'IVA del 21%: ", preu_iva)
preu_total_iva = preu_total + preu_iva
print("Aixo es el que val tots els productes amb IVA: ", preu_total_iva)

