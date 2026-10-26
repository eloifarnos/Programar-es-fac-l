# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Fes un programa que donat un número et digui si és més gran o no que zero.
# Especificacions d'entrada: Un número enter

numero = int(input("Introdueix un número enter: "))
if (numero < 0):
    print("El número és negatiu.")
elif (numero == 0):
    print("El número és zero.")
else:
    print("El número és positiu.")
#En aquest programa el que fem es demanar un numero a l'usuari i comprovem si es mes gran o no que 0 fent una comparacio amb 0 i imprimint si es negatiu, zero o positiu.