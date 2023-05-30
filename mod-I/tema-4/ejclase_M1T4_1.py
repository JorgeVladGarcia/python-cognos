'''
Modulo 1, Curso 4, Ejercicio en Clase 1
Cálculo de los decibelios en relación a: señal / ruido
    Importar el módulo math
    Pedir el valor de la señal usando try – except para manejar errores
    Pedir el valor del ruido usando try – except para manejar errores
    Si no hay error, calcular el valor de los decibelios con la formula:
                decib = 10 * math.log10(señal/ruido)
    Mostrar en pantalla el valor calculado de los decibelios
'''

import math

try:
    senal = float(input("Dame el valor de la señal... "))
    try:
        ruido = float(input("Dame el valor del ruido... "))
        decib = 10 * math.log10(senal/ruido)
        print("El valor en decibelios es:", decib)
    except:
        print("El valor del ruido no es correcto")
except:
    print("El valor de la señal no es correcto")
