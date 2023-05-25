'''
Crear un diccionario de los Casos Comprobados Covid (CC-Covid) del mes de
junio 2020 de: Ecuador, Paraguay, Chile, Perú, Argentina y Colombia.
• Los datos se encuentran en el archivo “WHO-COVID-19-global-data.txt”
• Verificar el formato de los datos del archivo
• Leer la información del archivo
• Seleccionar los datos de los países en el período indicado
• Almacenar los datos en un diccionario Python que tenga la tupla:
✓ País - fecha = CC Covid diario (New_cases)
• Grabar los datos en el archivo Sudamerica.txt, colocando un elemento del diccionario
por línea, con el siguiente formato:
✓ país, fecha, cc-covi
'''
# abrir archivo
file = open("WHO-COVID-19-global-data.txt", encoding="latin")

# crear lista vacia
list1 = [] 
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

# leer data del texto
for line in file:
    # remover retorno de carro 
    line = line.rstrip()
    # separar elementos
    dato = line.split()
    if dato[2] == "Ecuador" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list2.append((dato[0:5]))
    if dato[2] == "Paraguay" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list3.append(dato[0:5])
    if dato[2] == "Chile" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list4.append(dato[0:5])
    if dato[2] == "Peru" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list5.append(dato[0:5])
    if dato[2] == "Argentina" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list6.append(dato[0:5])
    if dato[2] == "Colombia" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list7.append(dato[0:5])

# agregar elementos requeridos a una lista
ecuador = list()
for values in list2:
    ecuador.append((values[2], values[0], values[4]))

paraguay = list()
for values in list3:
    paraguay.append((values[2], values[0], values[4]))

chile = list()
for values in list4:
    chile.append((values[2], values[0], values[4]))

peru = list()
for values in list5:
    peru.append((values[2], values[0], values[4]))

argentina = list()
for values in list6:
    argentina.append((values[2], values[0], values[4]))

colombia = list()
for values in list7:
    colombia.append((values[2], values[0], values[4]))

# agregar tuplas en un solo elemento
sudamerica = []
sudamerica += ecuador
sudamerica += paraguay
sudamerica += chile
sudamerica += peru
sudamerica += argentina
sudamerica += colombia

# escribir archivo con datos
fout = open("Sudamerica.txt", "w")
for t in sudamerica:
  fout.write(' '.join(str(s) for s in t) + '\n')

file.close()
fout.close()
