'''
Organizar y almacenar en una tabla Excel los datos de los Casos
Confirmados Covid de los países y regiones de América provenientes
de la Organización Mundial de la Salud (OMS).
• Revisar los datos del archivo “WHO-COVID-19-global-data.txt”.
• Leer los datos del archivo y seleccionar solo los países y regiones de América
(WHO_region = AMRO).
• Seleccionar solo el dato "Casos Confirmados Covid" (New_cases).
• Transformar los datos de una estructura secuencial a paralela.
• Adecuar los datos en un formato apropiado para Excel.
• Migrar la tabla resultante al programa Excel.
• Mostrar en Excel los datos completos (de enero 2020 a febrero 2021) de la
forma que se indica en “America_Ejemplo.xlsx”. En el ejemplo se muestran
solo los datos de abril 2020.
'''
# abrir archivo
march = open("WHO-COVID-19-global-data.txt", encoding= "latin")

# crear variables
lp = []

# interar data del archivo
for linea in march:
    # agregar elementos a una lista
    dato = linea.split()
    # encontrar elementos para crear titulos de columna
    if dato[0] == "Date_reported":
        lp.append((dato[2],(dato[0], dato[4])))
        #x = dato[0]+"\t"+dato[2]+"\t"+dato[4]+"\n"
#print(lp)
        #continue
    if dato[3] == "AMRO":
        lp.append((dato[2],(dato[0], dato[4])))

print(lp[1])
# crear lista de paises distintos 
country = []
for i in lp:
    if i[0] not in country:
        country.append(i[0])

print(country)
#    # initialize a null list
#    unique_list = []
#  
#    # traverse for all elements
#    for x in list1:
#        # check if exists in unique_list or not
#        if x not in unique_list:
#            unique_list.append(x)
#    # print list
#    for x in unique_list:
#        print x,
#
#list2 = [[x[0],letter] for x in lp for letter in x[1]]
#>>> wide_list = [[1,['a','b','c']],[2,['d','e']],[3, ['f']]]
#>>> long_list = [[k, v] for k, sublist in wide_list for v in sublist]
#>>> long_list
#[[1, 'a'], [1, 'b'], [1, 'c'], [2, 'd'], [2, 'e'], [3, 'f']]

#[[x[0],letter] for x in wide_list for letter in x[1]]
#[[1, 'a'], [1, 'b'], [1, 'c'], [2, 'd'], [2, 'e'], [3, 'f']]

#print(type(lp))
#print(list2[0])
march.close()

