'''
Mostrar el total de CC-Covid y el promedio diario del mes de junio 2020 de
los países indicados en el ejercicio 1.
• Los datos se encuentran en el archivo “WHO-COVID-19-global-data1.txt”
• Mostrar el total de CC-Covid y el promedio diario de cada uno de los países indicados en
el ejercicio 1
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
ctd = []
# leer data del texto
for line in file:
    # remover retorno de carro 
    line = line.rstrip()
    #line = line.startswith("2020-06")
    # separar elementos
    dato = line.split()
    if dato[2] == "Ecuador" and dato[0] >= "2020-06-01" and dato[0] <= "2020-06-30":
        list2.append((dato[0:5]))
    #print(list2)
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

# ecuador
sum = 0
for n in list2:
    val = int(n[4])
    sum += val
print("Total casos Ecuador:", sum, "- promedio:", round(sum/len(list2),2))
# Paraguay
sum = 0
for n in list3:
    val = int(n[4])
    sum += val
print("Total Paraguay:", sum, "- promedio:", round(sum/len(list3), 2))
# Chile
sum = 0
for n in list4:
    val = int(n[4])
    sum += val
print("Total Chile:", sum, "- promedio:", round(sum/len(list4), 2))
# Peru
sum = 0
for n in list5:
    val = int(n[4])
    sum += val
print("Total Peru:", sum, "- promedio:", round(sum/len(list5), 2))
# Argentina
sum = 0
for n in list6:
    val = int(n[4])
    sum += val
print("Total Argentina:", sum, "- proemdio", round(sum/len(list6), 2))
# Colombia
sum = 0
for n in list7:
    val = int(n[4])
    sum += val
print("Total Colombia:", sum, "- promedio", round(sum/len(list7), 2))

file.close()