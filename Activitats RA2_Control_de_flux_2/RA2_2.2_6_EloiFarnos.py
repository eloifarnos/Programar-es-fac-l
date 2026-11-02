# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 2/11/2026
# Versió: 1.0
#
# Descripció: Mostra els primers 10 termes de la seqüència de Fibonacci.
# Especificacions d'entrada: Mostra els primers 10 termes de la seqüència de Fibonacci.

a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

print()
