'''
Construir un directorio en base al archivo provisto con datos
Covid de 5 países de Sudamerica
• Los datos se encuentran en el archivo “Sudamerica.txt”
• Leer la información del archivo
• Almacenar los datos en una estructura diciconario que tenga:
✓ En el primer registro como indice: "FECHA"
✓ Y como valor el listado de los paises que intervienen
✓ En el resto del directorio, como indice la fecha.
✓ Como valor el listado de valores Covid de ese día de cada pais
'''
# abrir archivo
file = open("Sudamerica.txt")
# crear diccionarios para cada pais
bol_dic = dict()
ecu_dic = dict()
ch_dic = dict()
pr_dic = dict()
py_dic = dict()
# crear variables de apoyo
val_bol = -1
val_ecu = -1
val_ch = -1
val_pr = -1
val_py = -1

for line in file:
    # remover retorno de carro
    line = line.rstrip()
    # separar elementos
    line = line.split()
    # BOLIVIA: separar datos
    bol = line[1]
    bol = bol.split()
    # agregar elementos a diccionario 
    for item in bol:
        val_bol += 1
        bol_dic[val_bol] = item
    # ECUADOR: separar datos
    ecu = line[2]
    ecu = ecu.split()
    # ECUADOR: agregar elementos a diccionario 
    for item in ecu:
        val_ecu += 1
        ecu_dic[val_ecu] = item
    # CHILE: separar datos
    ch = line[3]
    ch = ch.split()
    # CHILE: agregar elementos a diccionario 
    for item in ch:
        val_ch += 1
        ch_dic[val_ch] = item
    # PERU: separar datos
    pr = line[4]
    pr = pr.split()
    # PERU: agregar elementos a diccionario 
    for item in pr:
        val_pr += 1
        pr_dic[val_pr] = item
    # PARAGUAY: separar datos
    py = line[5]
    py = py.split()
    # PARAGUAY: agregar elementos a diccionario 
    for item in py:
        val_py += 1
        py_dic[val_py] = item

 
# eliminar primer elementos con string
del bol_dic[0]
del ecu_dic[0]
del ch_dic[0]
del pr_dic[0]
del py_dic[0]

# convertir keys a int
for keys in bol_dic:
        bol_dic[keys] = int(bol_dic[keys])
for keys in ecu_dic:
        ecu_dic[keys] = int(ecu_dic[keys])
for keys in ch_dic:
        ch_dic[keys] = int(ch_dic[keys])
for keys in pr_dic:
        pr_dic[keys] = int(pr_dic[keys])
for keys in py_dic:
        py_dic[keys] = int(py_dic[keys])

# Bolivia
# crear variables
tot_bol = sum(bol_dic.values())
avg_bol = round(sum(bol_dic.values())/len(bol_dic), 2)
above_bol = 0
below_bol = 0
# imprimir resultados
print("Bolivia")
print("- Total:", tot_bol)
print("- Promedio diario:", avg_bol)
for clave in bol_dic:
        if bol_dic[clave] > avg_bol:
                above_bol += 1
print("- Num. casos arriba del promedio:", above_bol)
for clave in bol_dic:
        if bol_dic[clave] < avg_bol:
                below_bol += 1
print("- Num. casos debajo del promedio:", below_bol)

# Ecuador
# crear variables
tot_ecu = sum(ecu_dic.values())
avg_ecu = round(sum(ecu_dic.values())/len(ecu_dic), 2)
above_ecu = 0
below_ecu = 0
# imprimir resultados
print("\nEcuador")
print("- Total:", tot_ecu)
print("- Promedio diario:", avg_ecu)
for clave in ecu_dic:
        if ecu_dic[clave] > avg_ecu:
                above_ecu += 1
print("- Num. casos arriba del promedio:", above_ecu)
for clave in ecu_dic:
        if ecu_dic[clave] < avg_ecu:
                below_ecu += 1
print("- Num. casos debajo del promedio:", below_ecu)

# Chile
# crear variables
tot_ch = sum(ch_dic.values())
avg_ch = round(sum(ch_dic.values())/len(ch_dic), 2)
above_ch = 0
below_ch = 0
# imprimir resultados
print("\nChile")
print("- Total:", tot_ch)
print("- Promedio diario:", avg_ch)
for clave in ch_dic:
        if ch_dic[clave] > avg_ch:
                above_ch += 1
print("- Num. casos arriba del promedio:", above_ch)
for clave in ch_dic:
        if ch_dic[clave] < avg_ch:
                below_ch += 1
print("- Num. casos debajo del promedio:", below_ch)

# Peru
# crear variables
tot_pr = sum(pr_dic.values())
avg_pr = round(sum(pr_dic.values())/len(pr_dic), 2)
above_pr = 0
below_pr = 0
# imprimir resultados
print("\nPeru")
print("- Total:", tot_pr)
print("- Promedio diario:", avg_pr)
for clave in pr_dic:
        if pr_dic[clave] > avg_pr:
                above_pr += 1
print("- Num. casos arriba del promedio:", above_pr)
for clave in pr_dic:
        if pr_dic[clave] < avg_pr:
                below_pr += 1
print("- Num. casos debajo del promedio:", below_pr)

# Paraguay
# crear variables
tot_py = sum(py_dic.values())
avg_py = round(sum(py_dic.values())/len(py_dic), 2)
above_py = 0
below_py = 0
# imprimir resultados
print("\nParaguay")
print("- Total:", tot_py)
print("- Promedio diario:", avg_py)
for clave in py_dic:
        if py_dic[clave] > avg_py:
                above_py += 1
print("- Num. casos arriba del promedio:", above_py)
for clave in py_dic:
        if py_dic[clave] < avg_py:
                below_py += 1
print("- Num. casos debajo del promedio:", below_py)

file.close()