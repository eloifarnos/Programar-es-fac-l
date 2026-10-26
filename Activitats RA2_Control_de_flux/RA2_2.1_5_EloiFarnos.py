# Administració de Sistemes Informàtics en Xarxa
# Autor: Eloi Farnós Gogoanta
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Fes un programa el qual donada la data de naixement et calculi la edat i et digui si ets o no major d’edat.
# Especificacions d'entrada: Una data de naixement en format dd/mm/aaaa

from datetime import date


dia_naixement = int(input("Quin dia vas neixer? ")) #Demanem la informació de naixament del usuari
mes_naixement = int(input("Quin mes vas neixer? "))
any_naixement = int(input("Quin any vas neixer? "))
data_avui = date.today()
anys= data_avui.year - any_naixement
if(anys == 18):
    if(data_avui.month < mes_naixement):
        print("No ets major d'edat")
    if(data_avui.month > mes_naixement):
        print("Ets major d'edat")
    if(data_avui.month == mes_naixement):
        if(data_avui.day() < dia_naixement):
            print("No ets major d'edat")
        if(data_avui.day() >= dia_naixement):
            print("Ets major d'edat")
        if(data_avui.month() == mes_naixement):
            print("Felicitats, avui és el teu aniversari!")
if(anys < 18):
    print("No ets major d'edat")
if(anys > 18):
    print("Ets major d'edat")
#En aquest codi el que fem es primer demanar la data de naixement del usuari i després amb la funció date.today() agafem la data d'avui, després fem una resta entre l'any d'avui i l'any de naixement per saber quants anys té el usuari, després fem una serie de condicions per saber si és major d'edat o no.