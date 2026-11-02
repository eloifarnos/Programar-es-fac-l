# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Trobar el número màxim d’una llista de números introduïda per l’usuari
# Especificacions d'entrada: Llista de números introduïda per l’usuari

entrada = input("Introdueix nombres separats per espais: ")
numeros = [float(valor) for valor in entrada.split()]

if not numeros:
    print("No has introduït cap nombre.")
else:
    maxim = numeros[0]

    for numero in numeros[1:]:
        if numero > maxim:
            maxim = numero

    print("El màxim és:", maxim)
