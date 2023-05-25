'''
Extraer y mostrar la sumatoria, el promedio, el mayor y el
menor de los números de punto flotante
• Los datos se encuentran en el archivo “correos.txt”
• Buscar los números que están en las líneas que empiezan con X-DSPAM
• Extraer esos datos y hacer una sumatoria de los mismos
• Asimismo, encontrar el promedio, el número mayor y el menor
• Mostrar en pantalla el texto:
• Sumatoria: xxxxxxxx Promedio: wwwww Mayor: yyyyyy Menor: zzzzzzz
'''

import re 
arch = open("correos.txt")
sum = 0 
num_it = 0
max = None
min = None

for linea in arch:
    linea = linea.rstrip()
    lista = re.findall("^X-\S*: ([0-9.]+)", linea)
    # convertir datos a integer
    for i in lista:
        i = float(lista[0])
        # hallar suma total
        sum += i
        # hallar numero de iteraciones
        num_it += 1
        # hallar dato mayor
        if max == None or i > max:
            max = i
        # hallar dato menor
        if min == None or i < min:
            min = i
        #print(i)

print("Sumatoria:", sum, "Promedio:", sum/num_it, "Mayor:", max, "Menor:", min)