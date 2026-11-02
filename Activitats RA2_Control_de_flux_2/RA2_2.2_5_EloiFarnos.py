# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un número enter positiu i determina si és un nombre primer o no
# Especificacions d'entrada: Demanar un numero 

numero = int(input("Introdueix un nombre enter positiu: "))

while numero <= 0:
    numero = int(input("Ha de ser positiu. Torna-ho a provar: "))

es_primer = numero > 1
divisor = 2

while es_primer and divisor * divisor <= numero:
    if numero % divisor == 0:
        es_primer = False
    divisor += 1

if es_primer:
    print(f"{numero} és un nombre primer.")
else:
    print(f"{numero} no és un nombre primer.")
