'''
Obtener un número aleatorio entre 2 valores extremos
• Estudiar en https://www.python.org/doc/ buscar Library Reference y ahí buscar
random en Numeric and Mathematical Modules.
• Pedir el valor menor del rango (entero), usando try – except
• Pedir el valor mayor del rango (entero), asegurando que este dato es mayor que el
valor anterior y usando try – except
• Procesar, obtener el valor al azar
• Mostrar en pantalla el mensaje final:
El valor al azar obtenido entre menor y mayor es: Num. aza
'''
import random
try:
    inf = int(input("Insertar el valor menor: "))
    sup = int(input("Insertar el valor mayor: "))

    if sup < inf:
        print("El valor mayor del rango debe ser superior a", inf)
    else:
        rndm = random.randint(inf, sup) 
        print("El valor al azar obtenido entre", inf,"y", sup, "es:", rndm)    

except:
    print("Los valores del rango deben ser números enteros.")

