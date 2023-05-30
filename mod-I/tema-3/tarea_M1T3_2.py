'''
Insertar un “guardián” en la formula de la velocidad para evitar fallas
• La formula de la velocidad es: v = espacio/tiempo
• Pedir datos de punto flotante de espacio (km) y tiempo (horas) usando try – except
para evitar fallas
• Calcular la velocidad con un “guardián” que evite fallar al proporcionar tiempo = 0
• Mostrar la velocidad calculada con el mensaje:
Recorrer xx km en un tiempo de yy horas = zz km/hora
'''
try:
    spcio = float(input("Introduzca el valor del espacio en kms.: "))
    tempo = float(input("Introduzca el valor del tiempo en horas: "))
    if tempo != 0:
        vlcd = round(spcio / tempo, 2)
        print("La velocidad es", vlcd, "km/h")
    else:
        print("El valor del tiempo en horas debe ser distinto a 0")
except:
    print("Valor inválido. Por favor insertar valores numéricos")