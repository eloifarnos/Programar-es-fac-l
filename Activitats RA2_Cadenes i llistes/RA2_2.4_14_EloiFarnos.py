# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 13/11/2026
# Versió: 1.0
#
# Descripció:Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.
# Especificacions d'entrada: 10 numeros enters.

try:
    llista=[int(input("Introdueix el nombre {}: ".format(i+1))) for i in range(10)]

    parells=[num for num in llista if num%2==0]
    senars=[num for num in llista if num%2!=0]

    print("La llista de nombres parells és:", parells)
    print("La llista de nombres senars és:", senars)
except Exception as e:
    print("S'ha produït un error:", e)
