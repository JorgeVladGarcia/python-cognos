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

# diccionario Bolivia
print(bol_dic)
# diccionario Ecuador
print(ecu_dic)
# diccionario Chile
print(ch_dic)
# diccionario Peru
print(pr_dic)
# diccionario Paraguay
print(py_dic)

file.close()
