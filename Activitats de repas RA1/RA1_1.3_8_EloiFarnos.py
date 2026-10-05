# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 5/10/2026
# Versió: 1.0
#
# Descripció: Demana una temperatura en graus Celsius i mostra l’equivalent en Fahrenheit. Fórmula: F = C × 9 / 5 + 32.
# Especificacions d'entrada: Dades numèriques decimals.

temperatura=float(input("Donem la tempratura en graus Celsius : "))
temp_farenheit=(temperatura*9/5)+32
print("La temperatura en Fahrenheit és: " + str(temp_farenheit))
