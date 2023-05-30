'''
1. Mostrar valores de trigonometría:
    • Estudiar en https://www.python.org/doc/ buscar Library Reference y ahí buscar
    math en Numeric and Mathematical Modules.
    • Pedir el grado deseado (x), usando try – except para manejar errores
    • Procesar, obtener el valor del seno, coseno y tangente del grado dado
    • Mostrar los valores (y) en mensajes, para: seno, coseno y tangente
    Para xxx grados, el valor del seno es yyy
'''
import math

def conver():
    try:
        grd = float(input("Insertar el valor del grado: "))

        grnd_rdn = math.radians(grd)
        sine = round(math.sin(grnd_rdn), 2)
        csne = round(math.cos(grnd_rdn), 2)
        tngt = round(math.tan(grnd_rdn), 2)

        print("\nPara", grd, "grado(s):")
        print("- El valor del seno es", sine )
        print("- El valor del coseno es", csne )
        print("- El valor de la tangente es", tngt)
    except:
        print("Insertar solo valores de punto flotante")

conver()