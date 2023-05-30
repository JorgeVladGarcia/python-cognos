'''
Modulo 1, Ejercicios Extras 2
Generar y obtener Casos Comprobados Covid en los departamentos de Bolivia en un
        día generando los casos en forma aleatoria entre 150 y 700
    Crear los nombres de los departamentos en una lista
    Importar el módulo random
    Generar en forma aleatoria el dato CC Covid por cada departamento
    Mostrar cada departamento y su dato CC Covid
    Mostrar el total de los casos del país de ese día
    Mostrar el promedio de los casos de los departamentos
    Mostrar el mejor departamento y su dato del día
    Mostrar el peor departamento y su dato del día
    Mostrar los departamentos y sus datos que están por encima del promedio
    Mostrar los departamentos y sus datos que están por debajo del promedio
'''

ldpto = ['Santa Cruz', 'La Paz', 'Cochabamba', 'Tarija', 'Chuquisaca',\
    'Oruro', 'Potosi', 'Beni', 'Pando']
vdpto = [0,0,0,0,0,0,0,0,0]
import random

tot = 0
mejor = None
peor = None
indice = 0
for dpto in ldpto:
    dato = random.randint(150, 700)
    print("El valor de", dpto, "es:", dato)
    tot = tot + dato
    if mejor == None or dato < mejor:
        mejor = dato
        dmej = dpto
    if peor == None or dato > peor:
        peor = dato
        dpeor = dpto
    vdpto[indice] = dato
    indice += 1
prom = tot/9
print("El total de CC Covid del día es", tot)
print("El promedio de los departamentos es:", prom)
print("El mejor dpto es:", dmej, "con:", mejor)
print("El peor dpto es:", dpeor, "con:", peor)

print("Dptos que están por encima del promedio")
for n in range(9):
    if vdpto[n] > prom: print(ldpto[n], "con:", vdpto[n])
print("Dptos que están por abajo del promedio")
for n in range(9):
    if vdpto[n] < prom: print(ldpto[n], "con:", vdpto[n])
