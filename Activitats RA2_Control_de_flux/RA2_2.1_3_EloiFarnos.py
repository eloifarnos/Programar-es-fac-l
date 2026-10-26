# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Fes un programa que et demani tres números i surti per pantalla el número més gran.
# Especificacions d'entrada: Tres números enters

numero1 = int(input("Posa el 1r numero.: "))
numero2 = int(input("Posa el 2n numero.: "))
numero3 = int(input("Posa el 3r numero.: "))
if (numero1>numero2):
    if (numero1>numero3):
        print("El número més gran és: ", numero1)
else:
    if (numero2>numero3):
        print("El número més gran és: ", numero2)
    else:
        print("El número més gran és: ", numero3)
#En aquest programa el que fem es demanar tres numeros a l'usuari i comprovem quin es el mes gran fent una comparacio entre els tres i imprimint el mes gran.