'''
1. Evaluar los datos de los CC Covid en Bolivia de enero 2021
• Los datos se encuentran en el archivo “Bolivia-enero.txt”
• Leer la información del archivo
• Mostrar el total de nuevos casos presentados en el país durante ese mes
• Mostrar el promedio diario de los casos en ese mes
• Mostrar cual fue el mejor día y su dato CC Covid
• Mostrar cual fue el peor día y su dato CC Covid
'''
# abrir archivo
file = open("Bolivia-enero.txt")

# crear variable lista
d_enero = []

# iterar lineas en el archivo
for line in file:
    # remover retorno de carro
    line = line.strip()
    # convertir cada elemento/linea se converte en una sublista
    line = line.split()
    # incluir cada sublista en la lista general
    d_enero.append(line)

# remover primera sublista sin valores
del d_enero[0]

'''
convertir segundo elemento de cada sublista
en integer para hallar la suma total
'''
# crear variables 
sum = 0
min = None
max = None
indice = 0
lista_ind = [[0]] * len(d_enero)
lista_fec = [[0]] * len(d_enero) 

# iterar dentro de cada segundo elemento de cada sublista
for i in d_enero:
    # convertir segundo elemento de sublista en integer
    i[1] = int(i[1])
    # hallar suma
    sum += i[1]
    # hallar valor menor
    if min == None or i[1] < min:
        min = i[1]
        min_date = i[0]
    # hallar valor mayor
    if max == None or i[1] > max:
        max = i[1]
        max_date = i[0]
    # hallar indices en lista con valores
    lista_ind[indice] = i[1]
    # hallar indices en lista de fechas 
    lista_fec[indice] = i[0]
    indice += 1

# hallar promedio
avg = round(sum/len(d_enero),2)

# imprimir resultados
print("El promedio diario de los casos en ese mes es:", avg)
print("\nLos dias y valores que están por encima del promedio son:")
for n in range(len(lista_ind)):
	if lista_ind[n] > avg: print("-", lista_fec[n], "con:", lista_ind[n])
print("\nLos dias y valores que están por debjao del promedio son:")
for n in range(len(lista_ind)):
	if lista_ind[n] < avg: print("-", lista_fec[n], "con:", lista_ind[n])

# cerrar archivo
file.close()