'''
1. Identificar la cantidad de vocales de un texto introducido por teclado
• Solicitar al usuario que escriba un refrán o adivinanza en una sola línea
• Analizar el mensaje tecleado por el usuario
• Contar la cantidad de veces que aparece cada una de las vocales
• Mostrar en pantalla resultados de este tipo para cada vocal:
La vocal X aparece NN veces
'''

oms = "Tres tristes tigres trigaban trigo en un trigal"
vocales = ["a", "e", "i", "o", "u"]

def cu_letra(cadena, letra):
    cont = 0
    for var1 in cadena:
        if var1 == letra:
            cont += 1 # aumentamos un valor al contador
    return cont 

for var2 in vocales:
    print("La letra", var2, "se repite", cu_letra(oms, var2), "veces")