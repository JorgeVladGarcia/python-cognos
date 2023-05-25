'''
Nuevos casos Covid comprobados de lunes a miercoles:

• Pedir los datos de esos días usando try – except para cada día
• Mostrar el promedio diario de los nuevos casos
• Mostrar el total de casos de los 3 días
• Indicar cuál es el mejor día
• Indicar cuál es el peor día
'''

band = True
try:
    lun = int(input("Dame el valor del lunes... "))
    tot = lun
    mejor = "Lunes"
    peor = "Lunes"
    dmej = lun
    dpeor = lun
except:
    print("El dato del lunes no fue correcto")
    band = False
if band == True:
    try:
        mar = int(input("Dame el valor del martes... "))
        tot = tot + mar
        if mar > dpeor:
            dpeor = mar
            peor = "Martes"
        if mar < dmej:
            dmej = mar
            mejor = "Martes"
    except:
        print("El dato del martes no fue correcto")
        band = False
if band == True:
    try:
        mie = int(input("Dame el valor del miercoles... "))
        tot = tot + mie
        if mie > dpeor:
            dpeor = mie
            peor = "Miercoles"
        if mie < dmej:
            dmej = mie
            mejor = "Miercoles"
    except:
        print("El dato del miercoles no fue correcto")
        band = False
if band == True:
    print("El total de casos en los 3 días es", tot)
    print("El promedio de casos en los 3 días es", tot/3)
    print("El mejor día es:", mejor, "con un valor de", dmej)
    print("El peor día es:", peor, "con un valor de", dpeor)

            
