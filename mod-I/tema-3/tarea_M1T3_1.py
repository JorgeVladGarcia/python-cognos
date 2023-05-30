'''
Nuevos casos Covid comprobados para los departamentos de La Paz,
Cochabamba, Santa Cruz y Tarija
• Pedir los datos de un día de cada departamento indicado y que no exceda de 950 en
cada caso. Usar try – except para evitar fallas.
• Mostrar el promedio de esos departamentos
• Mostrar el total de esos departamentos en el día
• Indicar cuál es el mejor departamento
• Indicar cuál es el peor departamento


• Indicar que departamentos están por encima del promedio
• Indicar que departamentos están por abajo del promedio
'''

band = True
try:
    lpaz = int(input("Introducir datos para La Paz: "))
    if lpaz > 950:
        print("El valor introducido no puede superar los 950 casos")
        band = False
    tot = lpaz
    mejor = "La Paz"
    peor = "La Paz"
    dmej = lpaz
    dpeor = lpaz
except:
    print("Datos para La Paz son inválidos")
    band = False
if band == True:
    try:
        cbba = int(input("Introducir datos para Cochabamba: "))
        if cbba > 950:
            print("El valor introducido no puede superar los 950 casos")
            band = False
        tot = tot + cbba
        if cbba > dpeor:
            dpeor = cbba
            peor = "Cochabamba"
        if cbba < dmej:
            dmej = cbba
            mejor = "Cochabamba"
    except:
        print("Datos para Cochabamba son inválidos")
        band = False
if band == True:
    try:
        sacz = int(input("Introducir datos para Santa Cruz: "))
        tot = tot + sacz
        if sacz > dpeor:
            dpeor = sacz
            peor = "Santa Cruz"
        if sacz < dmej:
            dmej = sacz
            mejor = "Santa Cruz"
    except:
        print("Datos para Santa Cruz son inválidos")
        band = False
if band == True:
    try:
        trja = int(input("Introducir datos para TarijaÑ "))
        tot = tot + trja
        if trja > dpeor:
            dpeor = trja
            peor = "Tarija"
        if trja < dmej:
            dmej = trja
            mejor = "Tarija"
    except:
        print("Datos para Tarija son inválidos")
        band = False

'''
datos estan stored en cada variable, se podria utilizar un if para agregar los deptos que estan debjo o encima del promedio
'''
if band == True:
    print("\nEl promedio de casos es:", tot/4)
    print("El total de casos en los departamentos es:", tot)
    print("El mejor departamento es", mejor, "con", dmej, "caso(s).")
    print("El peor departamento es", peor, "con", dpeor, "caso(s).")
            
