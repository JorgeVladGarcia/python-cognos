'''
Evaluar los datos de un archivo de texto
• Los datos se encuentran en el archivo “Datos-covid.txt”
• Leer la información del archivo
• Mostrar la sumatoria final del total de datos
• Mostrar el promedio de los datos del archivo
• Mostrar cual fue el mayor dato
• Mostrar cual fue el menor dato
'''
# leer el archivo
file = open("Datos-covid.txt")
# crear variables
cont = 0 
sum = 0
max = None
min = None 
# leer bucle
for linea in file:
    # convertir a integer
    linea = int(linea)
    # hallar suma total
    sum += linea
    # hallar num de lineas
    cont += 1
    # hallar dato mayor
    if min == None or linea < min:
        min = linea
    # hallar dato menor
    if max == None or linea > max:
        max = linea

# determinar promedio
avg = round(sum/cont,2)

# imprimir resultados
print("La suma total es:", sum) 
print("El promedio de datos del archivo es:", avg)
print("El mayor dato fue:", max)
print("El menor dato fue:", min) 

# cerrar archivoa
file.close()
